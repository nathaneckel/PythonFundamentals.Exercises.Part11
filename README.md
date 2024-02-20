# Part 11

## Accompanying resources
* Slide deck: https://zipcoder.github.io/reveal-slides.data-engineering/zcw_content/python/fundamentals-part11.html
* Enums: https://docs.python.org/3/library/enum.html
* UUID: https://docs.python.org/3.8/library/uuid.html#uuid.uuid4

## Exercise 1

Create a program called **shapes.py*

Declare a class called **Rectangle**

Rectangle class must have the following attributes:
* length
* width

Rectangle class must also have the following methods:
* area
* perimeter


Declare a class called **Square** 
* This class must inherit from the Rectangle class.


```python
import shapes
rect = shapes.Rectangle(2, 4)
rect.area()
# 8

square = shapes.Square(8)
square.area()
# 64

square.perimeter()
# 32
```

## Exercise 2 

Create a program called *gradebook.py*

Declare a **AliveStatus** class.

Requirements:
This class must inherit from Enum.
It must have two possible symbolic names:
* Deceased - associated with the value 0
* Alive - associated with the value 1


Declare a **Person** class.

Person class must have the following attributes:
* first_name
* last_name
* dob (date of birth)
* alive (of type AliveStatus)

Person class must also have the following methods:
* update_first_name
* update_last_name
* update_dob
* update_status

Declare an **Instructor** class.

* This class must inherit from the Person class. 
* This class must have an additional attribute called instructor_id.
* The instructor_id attribute must start with the string "Instructor_" followed by a UUID value.

Hint: Use super class calls.

Declare an **Student** class.

* This class must inherit from the Person class. 
* This class must have an additional attribute called student_id.
* The student_id attribute must start with the string "Student_" followed by a UUID value.

Declare a class called **ZipCodeStudent**.

* This class must inherit from the Student class.

Declare another type of student (prek, middle-school, college, etc).

* This class must inherit from the Student class.

Declare a class called **Classroom**:

Classroom class must have the following attributes:
* students - a container for students
* instructors - a container for instructors

Classroom class must also have the following methods:
* add_instructor
* remove_instructor
* add_student
* remove_student
* print_instructors
* print_students

As per usual, be sure to always be practicing TDD.

```
 python3 -m unittest test_gradebook.py
```