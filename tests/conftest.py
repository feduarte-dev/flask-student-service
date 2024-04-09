import pytest
from app import app


@pytest.fixture()
def client():
    return app.test_client()


@pytest.fixture()
def seed_student():
    from seed import seed

    seed()


@pytest.fixture()
def get_student():
    from random import randint
    from seed import students

    return students[randint(0, 9)]
