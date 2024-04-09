import pytest


pytestmark = pytest.mark.dependency()


def test_status_code(client, seed_student, get_student):
    res = client.get(f"/students/{get_student['enrollment_number']}")
    assert res.status_code == 200


def test_not_found_status_code(client):
    res = client.get("/students/qualquercoisamenosumenrollment")
    assert res.status_code == 404


def test_student_data(client, seed_student, get_student):
    res = client.get(f"/students/{get_student['enrollment_number']}")
    assert res.json["name"] == get_student["name"]
    assert res.json["enrollment_number"] == get_student["enrollment_number"]


@pytest.mark.dependency(
    depends=[
        "test_status_code",
        "test_not_found_status_code",
        "test_student_data",
    ]
)
def test_get_by_enrollment_final():
    pass
