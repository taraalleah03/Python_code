#teacher takes student's attendance
#teacher can remove students
#teacher should take attendance again
#program counts how many students there are in total

class Student:
    def __init__(self, name, seat_number, sound="here!"):
        self.name = name
        self.seat_number = seat_number
        self.sound = sound

    def attendance_check(self, count):
        for i in range(count):
            print(self.name + " is " + self.sound)
        return

class Teacher:
    def __init__(self):
        self.students = []

    def student_attendance(self, student):
        self.students.append(student)
        print(student.name + " is in class")
        return

    def student_removal(self, student):
        self.students.remove(student)
        print(student.name + " left")
        return

    def greet_students(self):
        print('Teacher: "Name check!"')
        for student in self.students:
            student.attendance_check(1)

# Main program

student1 = Student("Clary", 1)
student2 = Student("Princess", 2)
student3 = Student("Joshua", 3)
student4 = Student("Radin", 4)
student5 = Student("Amber", 5)

teacher = Teacher()

teacher.student_attendance(student1)
teacher.student_attendance(student2)
teacher.student_attendance(student3)
teacher.student_attendance(student4)
teacher.student_attendance(student5)
teacher.greet_students()
print(f"There are {len(teacher.students)} students in total.")

teacher.student_removal(student1)
teacher.greet_students()
print(f"There are {len(teacher.students)} students in total.")