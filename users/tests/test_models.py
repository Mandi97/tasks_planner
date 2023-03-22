import pytest


@pytest.mark.slow
def test_create_user(user, django_user_model):
    users = django_user_model.objects.all()
    assert len(users) == 2


@pytest.mark.slow
def test_change_password(user, django_user_model):
    user_db = django_user_model.objects.get(email='test@user.pl')

    user_db.set_password('secret')
    assert user_db.check_password('secret') is True
