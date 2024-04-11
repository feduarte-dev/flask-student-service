from flask import Blueprint, jsonify, request
from models.student_model import StudentModel

student_controller = Blueprint("students", __name__)


def _get_all_students():
    students = StudentModel.find()
    return [student.to_dict() for student in students]


# essa funcao cria a estrutura para a response?


def _get_student(enrollment_number: str):
    return StudentModel.find_one({"enrollment_number": enrollment_number})


@student_controller.route("/", methods=["GET"])
def get_all_students():
    students = _get_all_students()
    if students is None:
        return jsonify([]), 200
    return jsonify(students), 200


@student_controller.route("/<enrollment_number>", methods=["GET"])
def get_student(enrollment_number: str):
    student = _get_student(enrollment_number)
    if student is None:
        return jsonify(), 404
    return jsonify(student.to_dict()), 200


@student_controller.route("/", methods=["POST"])
def create_student():
    if "name" not in request.json or "enrollment_number" not in request.json:
        return 400
    new_student = StudentModel(request.json)
    new_student.save()
    return jsonify(new_student.to_dict()), 201


# sem eu passar o status code, ele está retornando um 200. como consegue?
