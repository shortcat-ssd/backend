from django.utils import timezone
from rest_framework import status

from shorts.models import Short


def test_shorts_list_requires_authentication(api_client):
    response = api_client.get("/api/v1/shorts/")

    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_shorts_list_returns_only_current_user_shorts(
    auth_client, factory_user, factory_short
):
    api_client, user = auth_client
    other_user = factory_user()

    short_1 = factory_short(user=user)
    short_2 = factory_short(user=other_user)

    response = api_client.get("/api/v1/shorts/")

    assert response.status_code == status.HTTP_200_OK

    codes = {item["code"] for item in response.data}

    assert short_1.code in codes
    assert short_2.code not in codes


def test_shorts_create_creates_short_for_authenticated_user(auth_client):
    api_client, user = auth_client

    future = timezone.now() + timezone.timedelta(days=1)
    payload = {
        "target": "https://example.com/",
        "label": "test label",
        "private": False,
        "expired_at": future.isoformat(),
    }

    response = api_client.post("/api/v1/shorts/", payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED

    short = Short.objects.get(code=response.data["code"])
    assert short.user == user
    assert short.target == payload["target"]


def test_short_detail_returns_404_for_non_owner(
    auth_client, factory_user, factory_short
):
    api_client, _ = auth_client
    owner = factory_user()
    short = factory_short(user=owner)

    response = api_client.get(f"/api/v1/shorts/{short.code}/")

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_short_clicks_returns_clicks_for_owner(
    auth_client, factory_short, factory_click
):
    api_client, user = auth_client
    short = factory_short(user=user)

    factory_click(short=short)
    factory_click(short=short)

    response = api_client.get(f"/api/v1/shorts/{short.code}/clicks/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2


def test_short_clicks_returns_404_for_non_owner(
    auth_client, factory_user, factory_short, factory_click
):
    api_client, _ = auth_client
    owner = factory_user()
    short = factory_short(user=owner)

    factory_click(short=short)

    response = api_client.get(f"/api/v1/shorts/{short.code}/clicks/")

    assert response.status_code == status.HTTP_404_NOT_FOUND
