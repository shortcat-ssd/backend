def test_superuser_has_permission(
    factory, owner_permission, factory_user, factory_short
):
    user = factory_user(is_superuser=True)
    short = factory_short(user=user)

    request = factory.get("/")
    request.user = user

    assert owner_permission.has_object_permission(request, None, short)


def test_owner_has_permission(factory, owner_permission, factory_user, factory_short):
    user = factory_user()
    short = factory_short(user=user)

    request = factory.get("/")
    request.user = user

    assert owner_permission.has_object_permission(request, None, short)


def test_non_owner_no_permission(
    factory, owner_permission, factory_user, factory_short
):
    owner = factory_user()
    non_owner = factory_user()
    short = factory_short(user=owner)

    request = factory.get("/")
    request.user = non_owner

    assert not owner_permission.has_object_permission(request, None, short)
