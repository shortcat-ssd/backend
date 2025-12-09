import pytest

from django.http import Http404
from django.utils import timezone

from shorts.util import redirect_short


def test_redirect_short_raise_404_for_not_found():
    with pytest.raises(Http404):
        redirect_short(None, "test-invalid-code")


def test_redirect_short_raise_404_for_expired_short(factory_short):
    short = factory_short(code="test-expired-code", expired_at=timezone.now())

    with pytest.raises(Http404):
        redirect_short(None, short.code)


def test_redirect_short_raise_404_for_private_short(factory_short):
    short = factory_short(code="test-private-code", private=True)

    with pytest.raises(Http404):
        redirect_short(None, short.code)


def test_redirect_short_creates_click(factory_short):
    short = factory_short(code="test-click-code")
    initial_clicks = short.clicks.count()

    redirect_short(None, short.code)

    short.refresh_from_db()
    assert short.clicks.count() == initial_clicks + 1
