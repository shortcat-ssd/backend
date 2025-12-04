import pytest

from django.utils import timezone
from rest_framework.exceptions import ValidationError

from shorts.serializers import ShortSerializer


@pytest.fixture
def short_serializer():
    return ShortSerializer()


def test_short_serializer_raises_error_when_expired_at_in_past(short_serializer):
    past = timezone.now() - timezone.timedelta(days=1)

    with pytest.raises(ValidationError):
        short_serializer.validate_expired_at(past)


def test_short_serializer_accepts_expired_at_in_future(short_serializer):
    future = timezone.now() + timezone.timedelta(days=1)
    result = short_serializer.validate_expired_at(future)
    assert result == future


def test_short_serializer_accepts_null_expired_at(short_serializer):
    result = short_serializer.validate_expired_at(None)
    assert result is None


def test_short_serializer_raises_error_when_target_is_empty(short_serializer):
    with pytest.raises(ValidationError):
        short_serializer.validate_target("")


def test_short_serializer_accepts_valid_target(short_serializer):
    valid_url = "https://example.com/"
    result = short_serializer.validate_target(valid_url)
    assert result == valid_url
