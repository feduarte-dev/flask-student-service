from models.abstract_model import AbstractModel
from database.db import db

from pymongo.collection import ReturnDocument


class StudentModel(AbstractModel):
    _collection = db["students"]

    def __init__(self, data):
        super().__init__(data)

    def update(self, data):
        result = self._collection.find_one_and_update(
            {"enrollment_number": self.data["enrollment_number"]},
            {"$set": data},
            return_document=ReturnDocument.AFTER,
        )

        self.data = result
        return {
            "name": self.data["name"],
            "enrollment_number": self.data["enrollment_number"],
        }

    def to_dict(self):
        return {
            "name": self.data["name"],
            "enrollment_number": self.data["enrollment_number"],
        }
