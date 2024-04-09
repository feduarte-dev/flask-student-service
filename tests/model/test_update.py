import pytest
from models.student_model import StudentModel


pytestmark = pytest.mark.dependency()


def test_if_update_is_overwritten_to_use_enrollment(seed_student):
    result = (
        StudentModel(
            {
                "name": "John",
                "enrollment_number": "2023123456",
            }
        )
        .save()
        .update(
            {
                "name": "Updated John",
                "enrollment_number": "2023123456",
            }
        )
    )

    assert isinstance(result, dict)
    assert result == {
        "name": "Updated John",
        "enrollment_number": "2023123456",
    }


@pytest.mark.dependency(
    depends=[
        "test_if_update_is_overwritten_to_use_enrollment",
    ]
)
def test_update_student_final():
    pass
