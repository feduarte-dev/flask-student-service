import pytest


pytestmark = pytest.mark.dependency()


def test_correct_update_status_code(client, seed_student, get_student):
    res = client.put(
        f"/students/{get_student['enrollment_number']}",
        json={"name": "John", "enrollment_number": 2023123456},
    )
    assert res.status_code == 200


def test_not_found_status_code(client):
    res = client.put(
        "/students/qualquercoisamenosumnumerodematricula",
        json={"name": "John", "enrollment_number": 2023123456},
    )
    assert res.status_code == 404
    assert res.data == b""


def test_correct_db_updating(client, seed_student, get_student):
    before_enrollment_number = get_student["enrollment_number"]

    res = client.put(
        f"/students/{get_student['enrollment_number']}",
        json={"name": "John", "enrollment_number": 2023123456},
    )
    after_insertion = res.json["enrollment_number"]

    assert before_enrollment_number != after_insertion
    assert after_insertion == 2023123456


@pytest.mark.dependency(
    depends=[
        "test_correct_update_status_code",
        "test_not_found_status_code",
        "test_correct_db_updating",
    ]
)
def test_update_endpoint_student_final():
    pass
