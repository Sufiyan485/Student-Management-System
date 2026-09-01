from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def show_details(self):
        pass


class Student(Person):
    def __init__(self, student_id, name, age, email, roll_no):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.roll_no = roll_no
        self.grades = {}

    def get_role(self):
        return "Student"

    def show_details(self):
        print(f"\n--- Student Details ({self.student_id}) ---")
        print(f"Student ID   : {self.student_id}")
        print(f"Name         : {self.name}")
        print(f"Age          : {self.age}")
        print(f"Email        : {self.email}")
        print(f"Roll No      : {self.roll_no}")
        print(f"Grades       : {self.grades}")

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def update_name(self, new_name):
        self.name = new_name

    def update_age(self, new_age):
        self.age = new_age

    def update_email(self, new_email):
        self.email = new_email

    def update_roll_no(self, new_roll_no):
        self.roll_no = new_roll_no


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
        print(f"\n--- Teacher Details ({self.emp_id}) ---")
        print(f"Employee ID   : {self.emp_id}")
        print(f"Name          : {self.name}")
        print(f"Age           : {self.age}")
        print(f"Email         : {self.email}")
        print(f"Subject       : {self.subject}")

    def update_name(self, new_name):
        self.name = new_name

    def update_age(self, new_age):
        self.age = new_age

    def update_email(self, new_email):
        self.email = new_email

    def update_subject(self, new_subject):
        self.subject = new_subject

class ManagementSystem:
    def __init__(self):
        self.students: dict[str, Student] = {}
        self.teachers: dict[str, Teacher] = {}
        self.next_student_id = 1
        self.next_teacher_id = 1

    def register_student(self):
        student_id = f"STD{self.next_student_id:03d}"
        name = input("Enter your name :- ")
        age = int(input("Enter your age :- "))
        email = input("Enter your mail :- ")
        roll_no = int(input("Enter your roll no :- "))

        new_student = Student(student_id, name, age, email, roll_no)
        self.students[student_id] = new_student
        self.next_student_id += 1

        print("Student Registered Successfully!")

    def show_student_details(self):
        std_id = input("Student ID :- ")

        if std_id in self.students:
            student = self.students[std_id]
            student.show_details()
        else:
            print("Student Not Found!")

    def add_student_grade(self):
        std_id = input("Student ID :- ")

        if std_id in self.students:
            subject = input("Subject :- ")

            while True:
                try:
                    grade = int(input("Grade (0-100) :- "))
                    if 0 <= grade <= 100:
                        break
                    else:
                        print("Please enter marks between (0-100)")
                except ValueError:
                    print("Enter a number")

            student = self.students[std_id]
            student.add_grade(subject, grade)
            print("Grade added successfully!")
        else:
            print("Student Not Found!")

    def update_student(self):
        std_id = input("Student ID :- ")

        if std_id in self.students:
            student = self.students[std_id]
            student.show_details()

            while True:
                print("\n--- Student Details Update Menu ---")
                print("press 1 to update name")
                print("press 2 to update age")
                print("press 3 to update email")
                print("press 4 to update roll_no")
                print("press 5 if you are done")

                while True:
                    try:
                        choice = int(input("Enter your choice :- "))
                        if 1 <= choice <= 5:
                            break
                        else:
                            print("Enter a choice between (1-5)")
                    except ValueError:
                        print("Enter a number")

                if choice == 1:
                    new_name = input("Enter new name :- ")
                    student.update_name(new_name)
                    print("Name updated successfully!")

                elif choice == 2:
                    new_age = int(input("Enter new age :- "))
                    student.update_age(new_age)
                    print("Age updated successfully!")

                elif choice == 3:
                    new_email = input("Enter new email :- ")
                    student.update_email(new_email)
                    print("Email updated successfully!")

                elif choice == 4:
                    new_roll_no = int(input("Enter new roll no :- "))
                    student.update_roll_no(new_roll_no)
                    print("Roll number updated successfully!")

                elif choice == 5:
                    print("Update completed!")
                    break
        else:
            print("Student Not Found!")

    def delete_student(self):
        std_id = input("Student ID :-")

        if std_id in self.students:
            student = self.students[std_id]
            student.show_details()
            while True: 
                confirm = input("Are you sure you want to delete this student? (yes/no): ")
                if confirm.lower() in ['yes', 'y']:
                    self.students.pop(std_id)
                    print("Student deleted successfully!")
                    break
                elif confirm.lower() in ['no', 'n']:
                    print("Deletion cancelled.")
                    break
                else:
                    print("Please enter 'yes' or 'no'.")
                    continue
        else:
            print("Student Not Found!")

    def register_teacher(self):
        emp_id = f"EMP{self.next_teacher_id:03d}"
        name = input("Enter your name :- ")
        age = int(input("Enter your age :- "))
        email = input("Enter your mail :- ")
        subject = input("Enter the subject you teach :- ")

        new_teacher = Teacher(emp_id, name, age, email, subject)
        self.teachers[emp_id] = new_teacher
        self.next_teacher_id += 1

        print("Teacher Registered Successfully!")

    def show_teacher_details(self):
        emp_id = input("Employee ID :- ")

        if emp_id in self.teachers:
            teacher = self.teachers[emp_id]
            teacher.show_details()
        else:
            print("Teacher not found!")

    def update_teacher(self):
        emp_id = input("Employee ID :- ")

        if emp_id in self.teachers:
            teacher = self.teachers[emp_id]
            teacher.show_details()

            while True:
                print("\n--- Teacher Details Update Menu ---")
                print("press 1 to update name")
                print("press 2 to update age")
                print("press 3 to update email")
                print("press 4 to update subject")
                print("press 5 if you are done")

                while True:
                    try:
                        choice = int(input("Enter your choice :- "))
                        if 1 <= choice <= 5:
                            break
                        else:
                            print("Enter a choice between (1-5)")
                    except ValueError:
                        print("Enter a number")

                if choice == 1:
                    new_name = input("Enter new name :- ")
                    teacher.update_name(new_name)
                    print("Name updated successfully!")

                elif choice == 2:
                    new_age = int(input("Enter new age :- "))
                    teacher.update_age(new_age)
                    print("Age updated successfully!")

                elif choice == 3:
                    new_email = input("Enter new email :- ")
                    teacher.update_email(new_email)
                    print("Email updated successfully!")

                elif choice == 4:
                    new_subject = input("Enter new subject :- ")
                    teacher.update_subject(new_subject)
                    print("Subject updated successfully!")

                elif choice == 5:
                    print("Update completed!")
                    break
        else:
            print("Teacher not found!")

    def delete_teacher(self):
        emp_id = input("Employee ID :- ")

        if emp_id in self.teachers:
            teacher = self.teachers[emp_id]
            teacher.show_details()
            while True: 
                confirm = input("Are you sure you want to delete this teacher? (yes/no): ")
                if confirm.lower() in ['yes', 'y']:
                    self.teachers.pop(emp_id)
                    print("Teacher deleted successfully!")
                    break
                elif confirm.lower() in ['no', 'n']:
                    print("Deletion cancelled.")
                    break
                else:
                    print("Please enter 'yes' or 'no'.")
                    continue
        else:
            print("Teacher not found!")

system = ManagementSystem()

while True:
    print("\n--- Management System Menu ---")
    print("press 1 to register a student")
    print("press 2 to register a teacher")
    print("press 3 to add grades ")
    print("press 4 to show a student details")
    print("press 5 to show a teacher details")
    print("press 6 to update student details")
    print("press 7 to delete a student")
    print("press 8 to update teacher details")
    print("press 9 to delete a teacher")
    print("press 10 to exit")

    while True:
        try:
            choice = int(input("Enter your choice :- "))
            if 1 <= choice <= 10:
                break
            else:
                print("Enter a choice between (1-10)")
        except ValueError:
            print("Enter a number")

    if choice == 1:
        system.register_student()

    elif choice == 2:
        system.register_teacher()

    elif choice == 3:
        system.add_student_grade()

    elif choice == 4:
        system.show_student_details()

    elif choice == 5:
        system.show_teacher_details()

    elif choice == 6:
        system.update_student()

    elif choice == 7:
        system.delete_student()

    elif choice == 8:
        system.update_teacher()

    elif choice == 9:
        system.delete_teacher()

    elif choice == 10:
        print("Exiting... Goodbye!")
        break