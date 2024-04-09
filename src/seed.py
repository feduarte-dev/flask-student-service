from models.student_model import StudentModel

students = [
    {"name": "Ana", "enrollment_number": "201500123"},
    {"name": "Carlos", "enrollment_number": "200810456"},
    {"name": "Beatriz", "enrollment_number": "201912789"},
    {"name": "Daniel", "enrollment_number": "201201234"},
    {"name": "Eduarda", "enrollment_number": "200503567"},
    {"name": "Felipe", "enrollment_number": "201710890"},
    {"name": "Gabriela", "enrollment_number": "201104123"},
    {"name": "Henrique", "enrollment_number": "200402456"},
    {"name": "Isabela", "enrollment_number": "201606789"},
    {"name": "João", "enrollment_number": "200909012"},
]


def seed():
    StudentModel.drop()

    for student in students:
        StudentModel(student).save()


if __name__ == "__main__":
    print("Carregando estudantes...")
    seed()
