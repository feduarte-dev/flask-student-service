from models.abstract_model import AbstractModel
from database.db import db


class StudentModel(AbstractModel):
    _collection = db["students"]
