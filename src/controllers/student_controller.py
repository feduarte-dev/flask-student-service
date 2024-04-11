from flask import Blueprint, jsonify
from models.student_model import StudentModel

student_controller = Blueprint("students", __name__)


def _get_all_students():
    students = StudentModel.find()
    return [student.to_dict() for student in students]


# essa funcao cria a estrutura para a response?


@student_controller.route("/", methods=["GET"])
def get_all_students():
    students = _get_all_students()
    return jsonify(students), 200


# sem eu passar o status code, ele está retornando um 200. como consegue?
