import pytest


pytestmark = pytest.mark.dependency()


def test_correct_status_code(client):
    res = client.post(
        "/students",
        json={"name": "John", "enrollment_number": 2023123456},
    )
    assert res.status_code == 201


def test_missing_name_status_code(client):
    res = client.post(
        "/students",
        json={"enrollment_number": 2023123456},
    )
    assert res.status_code == 400


def test_missing_enrollment_number_status_code(client):
    res = client.post(
        "/students",
        json={"name": "John"},
    )
    assert res.status_code == 400


def test_correct_db_insertion(client):
    before_insertion = len(client.get("/students").json)
    res = client.post(
        "/students",
        json={"name": "John", "enrollment_number": 2023123456},
    )
    after_insertion = len(client.get("/students").json)
    assert after_insertion - before_insertion == 1
    assert res.json["name"] == "John"
    assert res.json["enrollment_number"] == 2023123456


@pytest.mark.dependency(
    depends=[
        "test_correct_status_code",
        "test_missing_name_status_code",
        "test_missing_enrollment_number_status_code",
        "test_correct_db_insertion",
    ]
)
def test_create_student_final():
    pass
