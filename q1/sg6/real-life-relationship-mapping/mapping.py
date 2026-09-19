class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
course_name = input("Enter course name: ")
course = Course(course_name)

num = int(input("How many students? "))

for i in range(num):
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    student = Student(name, student_id)
    course.add_student(student)
print("\nEnrolled Students in", course.course_name + ":")
for n in course.students:
    print("-", n.name)
