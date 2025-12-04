from datetime import timedelta

from django.utils import timezone

from shorts.models import generate_code, CODE_LENGTH


def test_generate_code_returns_value_when_no_collision(mock_token_urlsafe):
    expected_code = "A" * CODE_LENGTH
    mock_token_urlsafe.return_value = expected_code

    code = generate_code()

    assert code == expected_code


def test_generate_code_retries_and_returns_new_value_on_collision(
    mock_token_urlsafe, factory_short
):
    existing_code = "A" * CODE_LENGTH
    new_code = "B" * CODE_LENGTH

    factory_short(code=existing_code)
    mock_token_urlsafe.side_effect = [existing_code, new_code]

    code = generate_code()

    assert code == new_code


def test_short_str(factory_short):
    short = factory_short()
    assert str(short) == f"{short.code} -> {short.target}"


def test_is_expired_returns_false_when_expired_at_is_none(factory_short):
    short = factory_short(expired_at=None)
    assert short.is_expired is False


def test_short_is_expired_returns_false_when_expired_at_is_in_the_future(factory_short):
    future_time = timezone.now() + timedelta(days=1)
    short = factory_short(expired_at=future_time)
    assert short.is_expired is False


def test_short_is_expired_returns_true_when_expired_at_is_in_the_past(factory_short):
    past_time = timezone.now() - timedelta(days=1)
    short = factory_short(expired_at=past_time)
    assert short.is_expired is True


def test_short_is_expired_returns_true_when_expired_at_is_now(factory_short):
    now_time = timezone.now()
    short = factory_short(expired_at=now_time)
    assert short.is_expired is True


def test_short_click_str(factory_short):
    short = factory_short()
    short_click = short.clicks.create()
    assert str(short_click) == f"{short.code} ({short_click.created_at})"
