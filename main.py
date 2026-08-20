from abc import ABC, abstractmethod


class Person(ABC):

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def show_details(self):
        pass

class Student(Person):
    def __init__(self,student_id, name, age, email, roll_no):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.roll_no = roll_no
        self.grades = {}

    def get_role(self):
        return "Student"

    def show_details(self):
        print(f"Student ID   : {self.student_id}")
        print(f"Name         : {self.name}")
        print(f"Age          : {self.age}")
        print(f"Email        : {self.email}")
        print(f"Roll No      : {self.roll_no}")
        print(f"Grades       : {self.grades}")


class Teacher(Person):
    def __init__(self, emp_id, name, age, email, subject):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.email = email
        self.subject = subject

    def get_role(self):
        return "Teacher"

    def show_details(self):
        print(f"Employee ID   : {self.emp_id}")
        print(f"Name          : {self.name}")
        print(f"Age           : {self.age}")
        print(f"Email         : {self.email}")
        print(f"Subject       : {self.subject}")

student1 = Student("STD101","Alex",19,"alex@gmail.com",21)
teacher1 = Teacher("EMP101","Bob",30,"bob@gmail.com","Maths")

student1.get_role()
student1.show_details()
        
teacher1.get_role()
teacher1.show_details()


print("press 1 to register a student")
print("press 2 to register a teacher")
print("press 3 to add grades ")
print("press 4 to show a student details")
print("press 5 to show a teacher details")

choice = int(input("Enter your choice :- "))

if choice == 1:
    pass

elif choice == 2:
    pass

elif choice == 3:
    pass

elif choice == 4:
    pass

elif choice == 5:
    pass

else:
    print("Invalid choice")