import pytest

from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('test', 'test@test.com', 'test')
    count = User.objects.all().count()
    print(f'There is {count} user in count.')
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_user_create1():
    count = User.objects.all().count()
    print(f'In this test is {count} users.')
    assert count == 0


# @pytest.fixture(scope='session')
# def fixture_1():
#     print('ran fixture-1')
#     return 1


# def test_example1(fixture_1):
#     print('ran example1')
#     num = fixture_1
#     assert num == 1


# def test_example2(fixture_1):
#     print('ran example2')
#     num = fixture_1
#     assert num == 1


# @pytest.mark.skip
# def test_ex():
#     print('test1')
#     assert 1 == 1


# @pytest.mark.skip
# def test_ex2():
#     assert 1 == 2
