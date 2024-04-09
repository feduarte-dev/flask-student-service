from models.student_model import StudentModel
import pytest


pytestmark = pytest.mark.dependency()


def test_if_collection_is_correctly_defined():
    assert StudentModel._collection.name == "students"


@pytest.mark.dependency(
    depends=[
        "test_if_collection_is_correctly_defined",
    ]
)
def test_collection_final():
    pass
