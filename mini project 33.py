# Base class 1: Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Base class 2: Learner
class Learner:
    def __init__(self, student_id, course):
        self.student_id = student_id
        self.course = course

    def display_learner_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")


# Derived class: Student
class Student(Person, Learner):
    def __init__(self, name, age, student_id, course):
        # Initialize both parent classes
        Person.__init__(self, name, age)
        Learner.__init__(self, student_id, course)

    def display_student_info(self):
        print("Student Details:")
        self.display_person_info()
        self.display_learner_info()


# Example usage
if __name__ == "__main__":
    # Create a student instance
    student = Student(name="Alice", age=20, student_id="S12345", course="Computer Science")

    # Display student details
    student.display_student_info()
