import pytest
from mixer.backend.django import mixer


@pytest.fixture(autouse=True)
def enable_db_access(db):
    """Fixture to enable database access in tests."""
    pass


@pytest.fixture
def factory_user():
    """Fixture to create a user factory for tests."""

    def create_user(**kwargs):
        return mixer.blend("auth.User", **kwargs)

    return create_user


@pytest.fixture
def factory_short():
    """Fixture to create a short URL factory for tests."""

    def create_short(**kwargs):
        return mixer.blend("shorts.Short", **kwargs)

    return create_short
