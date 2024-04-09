import pytest


pytestmark = pytest.mark.dependency()


def test_correct_status_code(client, seed_student, get_student):
    res = client.delete(
        f"/students/{get_student['enrollment_number']}",
    )
    assert res.status_code == 204


def test_not_found_status_code(client, seed_student):
    res = client.delete(
        "/students/qualquercoisamenosumnumerodematricula",
    )
    assert res.status_code == 404


def test_correct_db_deletion(client, seed_student, get_student):
    before_insertion = len(client.get("/students").json)
    client.delete(
        f"/students/{get_student['enrollment_number']}",
    )
    after_insertion = len(client.get("/students").json)
    assert before_insertion - after_insertion == 1


@pytest.mark.dependency(
    depends=[
        "test_correct_status_code",
        "test_not_found_status_code",
        "test_correct_db_deletion",
    ]
)
def test_delete_student_final():
    pass
