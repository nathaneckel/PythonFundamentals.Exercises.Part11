import self

dir(__builtins__)
['Deceased', 'Alive']
class AliveStatus:
    def __init__(self, Deceased as 0, Alive as 1):
        Deceased = self.Deceased
        Alive = self.Alive
        self.Deceased = Deceased
        self.Alive = Alive

class Person:
    def __init__(self, first_name, last_name, dob, Alive):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.Alive = Alive

    def update_first_name(self):
        return self.first_name

    def update_last_name(self):
        return self.last_name

    def update_dob(self):
        return self.dob

    def update_status(self):
        return self_status


import uuid

# make a random UUID
uuid.uuid4()
uuid.UUID('bd65600d-8669-4903-8a14-af88203add38')

# Convert a UUID to a string of hex digits in standard form
str(uuid.uuid4())
'f50ec0b7-f960-400d-91f0-c42a6d44e3d0'

# Convert a UUID to a 32-character hexadecimal string
uuid.uuid4().hex
'9fe2c4e93f654fdbb24c02b15259716c'


class Instructor(Person):
    def __init__(self, instructor_id, first_name, last_name, dob, Alive):
        super().__init__(first_name, last_name, dob, Alive)
        super().instructor_id = (f{"Instructor_"} + {uuid.UUID()})


class Student(Person):
    def __init__(self, student_id):
        super().student_id = (f{"Student_"} + {uuid.UUID()})

class ZipCodeStudent(Student):
    def __init__(self, snooty_prep_student_from_the_80s):

class Classroom:
    def __init__(self):

    def add_instructor(self):

    def remove_instructor(self):

    def add_student(self):

    def remove_student(self):

    def print_instructors(self):

    def print_students(self):