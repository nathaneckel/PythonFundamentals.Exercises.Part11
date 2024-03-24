import self
from enum import Enum
from uuid import uuid4

# dir(__builtins__)
# ['Deceased', 'Alive']
class AliveStatus(Enum):
    Deceased = 0
    Alive = 1

class Person:
    def __init__(self, first_name, last_name, dob, alive):
        self.deceased = None
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = alive

    def update_first_name(self, new_first_name):
        self.first_name = new_first_name

    def update_last_name(self, new_last_name):
        self.last_name = new_last_name

    def update_dob(self, new_dob):
        self.dob = new_dob

    def update_status(self, new_update_status):
        self.deceased = new_update_status


class Instructor(Person):
    def __init__(self, first_name, last_name, dob, alive):
        super().__init__(first_name, last_name, dob, alive)
        self.instructor_id = "Instructor_" + str(uuid4())


class Student(Person):
    def __init__(self, first_name, last_name, dob, alive):
        super().__init__(first_name, last_name, dob, alive)
        self.student_id = "Student_" + str(uuid4())

class ZipCodeStudent(Student):
    pass

class SnootyPrepStudentFromThe80s:
    pass

class Classroom:
    def __init__(self):
        self.students = []
        self.instructors =[]

    def add_instructor(self, instructor):
        self.instructors.append(instructor)

    def remove_instructor(self, instructor):
        if instructor in self.instructors:
            self.instructors.remove(instructor)
        else:
            print("Instructor not found in the classroom")

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
        else:
            print("Student not found in the classroom")

    def print_instructors(self):
        print("Instructors in the classroom:")
        for instructor in self.instructors:
            print(instructor.first_name, instructor.last_name)

    def print_students(self):
        print("Students in the classroom:")
        for student in self.students:
            print(student.first_name, student.last_name)