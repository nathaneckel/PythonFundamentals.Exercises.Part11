import unittest

from gradebook import Person, AliveStatus, Classroom, Instructor, Student


class TestPerson(unittest.TestCase):
    def test_update_first_name(self):
        person = Person("John", "Doe", "1990-01-01", AliveStatus.Alive)
        person.update_first_name("Jack")
        self.assertEqual(person.first_name, "Jack")

    def test_update_last_name(self):
        person = Person("John", "Doe", "1990-01-01", AliveStatus.Alive)
        person.update_last_name("Smith")
        self.assertEqual(person.last_name, "Smith")

    def test_update_dob(self):
        person = Person("John", "Doe", "1990-01-01", AliveStatus.Alive)
        person.update_dob("1995-05-05")
        self.assertEqual(person.dob, "1995-05-05")

    def test_update_status(self):
        person = Person("John", "Doe", "1990-01-01", AliveStatus.Alive)
        person.update_status(AliveStatus.Deceased)
        self.assertEqual(person.deceased, AliveStatus.Deceased)

class TestClassroom(unittest.TestCase):
    def setUp(self):
        self.classroom = Classroom()
        self.instructor = Instructor("John", "Doe", "1990-01-01", AliveStatus.Alive)
        self.student = Student("Alice", "Johnson", "2000-06-10", AliveStatus.Alive)

    def test_add_instructor(self):
        self.classroom.add_instructor(self.instructor)
        self.assertIn(self.instructor, self.classroom.instructors)

    def test_remove_instructor(self):
        self.classroom.add_instructor(self.instructor)
        self.classroom.remove_instructor(self.instructor)
        self.assertNotIn(self.instructor, self.classroom.instructors)

    def test_add_student(self):
        self.classroom.add_student(self.student)
        self.assertIn(self.student, self.classroom.students)

    def test_remove_student(self):
        self.classroom.add_student(self.student)
        self.classroom.remove_student(self.student)
        self.assertNotIn(self.student, self.classroom.students)

if __name__ == '__main__':
    unittest.main()
