from models.abstract_model import AbstractModel
from database.db import db


class StudentModel(AbstractModel):
    _collection = db["students"]

    def __init__(self, data):
        super().__init__(data)

    def to_dict(self):
        return {
            "name": self.data["name"],
            "enrollment_number": self.data["enrollment_number"],
        }
