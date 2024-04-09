from models.student_model import StudentModel
import pytest


pytestmark = pytest.mark.dependency()


def test_if_model_converts_to_dict_correctly():
    student = StudentModel({"name": "John", "enrollment_number": 2023123456})

    result = student.to_dict()

    assert "name" in result
    assert "enrollment_number" in result

    assert result["name"] == "John"
    assert result["enrollment_number"] == 2023123456

    assert len(result) == 2


def test_if_model_initializes_correctly():
    student = StudentModel({"name": "John", "enrollment_number": 2023123456})
    student.save()
    assert student.data["name"] == "John"
    assert student.data["enrollment_number"] == 2023123456

    assert student.id is not None


@pytest.mark.dependency(
    depends=[
        "test_if_model_initializes_correctly",
        "test_if_model_converts_to_dict_correctly",
    ]
)
def test_init_to_dict_final():
    pass
