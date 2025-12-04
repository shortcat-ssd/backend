import pytest
from mixer.backend.django import mixer
from unittest.mock import patch
from rest_framework.test import APIClient, APIRequestFactory

from shorts.models import ShortClick
from shorts.permissions import IsOwner
from shorts.serializers import ShortSerializer


@pytest.fixture(autouse=True)
def enable_db_access(db):
    """Enable database access for all tests."""
    pass


@pytest.fixture
def factory_user():
    """Factory for auth.User."""

    def create_user(**kwargs):
        return mixer.blend("auth.User", **kwargs)

    return create_user


@pytest.fixture
def factory_short():
    """Factory for shorts.Short."""

    def create_short(**kwargs):
        return mixer.blend("shorts.Short", **kwargs)

    return create_short


@pytest.fixture
def factory_click(factory_short):
    """Factory for ShortClick."""

    def create_click(**kwargs):
        if "short" not in kwargs:
            kwargs["short"] = factory_short()
        return mixer.blend(ShortClick, **kwargs)

    return create_click


@pytest.fixture
def api_client():
    """APIClient DRF base."""
    return APIClient()


@pytest.fixture
def auth_client(api_client, factory_user):
    """Authenticated APIClient with user."""
    user = factory_user()
    api_client.force_authenticate(user=user)
    return api_client, user


@pytest.fixture
def mock_token_urlsafe():
    """Mock of secrets.token_urlsafe used in generate_code."""
    with patch("shorts.models.secrets.token_urlsafe") as mock:
        yield mock


@pytest.fixture
def factory():
    """APIRequestFactory for low-level permission tests."""
    return APIRequestFactory()


@pytest.fixture
def owner_permission():
    """Instance of IsOwner to reuse in tests."""
    return IsOwner()


@pytest.fixture
def short_serializer():
    """Instance of ShortSerializer for validation tests."""
    return ShortSerializer()
