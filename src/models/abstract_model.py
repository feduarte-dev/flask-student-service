from pymongo.collection import ReturnDocument


class AbstractModel:
    _collection = None

    def __init__(self, data):
        self.data = data.copy()

    def save(self):
        result = self._collection.insert_one(self.to_dict())
        inserted_document = self._collection.find_one(
            {"_id": result.inserted_id},
        )
        self.data = inserted_document
        self.id = str(inserted_document["_id"])
        return self

    def update(self, data):
        self.data = self._collection.find_one_and_update(
            {"enrollment_number": self.data["enrollment_number"]},
            {"$set": data},
            return_document=ReturnDocument.AFTER,
        )

        return {
            "name": self.data["name"],
            "enrollment_number": self.data["enrollment_number"],
        }

    def delete(self):
        self._collection.delete_one({"_id": self.data["_id"]})

    @classmethod
    def find(cls, query={}):
        data = cls._collection.find(query)
        return [cls(d) for d in data]

    @classmethod
    def find_one(cls, query={}):
        data = cls._collection.find_one(query)
        return cls(data) if data else None

    @classmethod
    def drop(cls):
        cls._collection.drop()
