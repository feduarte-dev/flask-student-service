import pytest


pytestmark = pytest.mark.dependency()


def test_status_code(client):
    response = client.get("/students")
    assert response.status_code == 200


def test_amount_of_students(client, seed_student):
    response = client.get("/students")
    assert len(response.json) == 10


def test_random_student_in_response(client, seed_student, get_student):
    response = client.get("/students")

    assert get_student in response.json


@pytest.mark.dependency(
    depends=[
        "test_status_code",
        "test_amount_of_students",
        "test_random_student_in_response",
    ]
)
def test_get_all_students_final():
    pass
