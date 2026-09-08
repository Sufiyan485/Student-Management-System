from abc import ABC, abstractmethod
import json

class Person(ABC):
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def show_details(self):
        pass

    def update_name(self, new_name):
        self.name = new_name

    def update_age(self, new_age):
        self.age = new_age

    def update_email(self, new_email):
        self.email = new_email


class Student(Person):
    def __init__(self, student_id, name, age, email, roll_no):
        super().__init__(name, age, email)
        self.student_id = student_id
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

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "roll_no": self.roll_no,
            "grades": self.grades
        }
    
    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def update_roll_no(self, new_roll_no):
        self.roll_no = new_roll_no

class Teacher(Person):
    def __init__(self, emp_id, name, age, email, subject):
        super().__init__(name, age, email)
        self.emp_id = emp_id
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

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "subject": self.subject
        }

    def update_subject(self, new_subject):
        self.subject = new_subject

class ManagementSystem:
    def __init__(self):
        self.students: dict[str, Student] = {}
        self.teachers: dict[str, Teacher] = {}
        self.next_student_id = 1
        self.next_teacher_id = 1

    @staticmethod
    def get_valid_int(prompt, min_value, max_value):
        while True:
            try:
                value = int(input(prompt))
                if min_value <= value <= max_value:
                    return value
                else:
                    print(f"Please enter a value between {min_value} and {max_value}")
            except ValueError:
                print("Enter a number")

    @staticmethod
    def get_valid_text(prompt):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            else:
                print("Input cannot be empty. Please enter a valid text.")

    @staticmethod
    def get_valid_email(prompt):
        while True:
            email = ManagementSystem.get_valid_text(prompt)
            if "@" in email:
                return email
            else:
                print("Please enter a valid email address.")

    def register_student(self):
        student_id = f"STD{self.next_student_id:03d}"
        name = ManagementSystem.get_valid_text("Enter your name :- ")
        age = ManagementSystem.get_valid_int("Enter your age :- ", 5, 100)
        email = ManagementSystem.get_valid_email("Enter your email :- ")
        roll_no = ManagementSystem.get_valid_int("Enter your roll_no :- ", 1, 9999)

        new_student = Student(student_id, name, age, email, roll_no)
        self.students[student_id] = new_student
        self.next_student_id += 1

        print("Student Registered Successfully!")
        print(f"Student ID :- {student_id}")

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
            subject = ManagementSystem.get_valid_text("Subject :- ").capitalize()
            grade = ManagementSystem.get_valid_int("Grade (0-100) :- ", 0, 100)
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

                choice = ManagementSystem.get_valid_int("Enter your choice :- ", 1, 5)
                
                if choice == 1:
                    new_name = ManagementSystem.get_valid_text("Enter new name :- ")
                    student.update_name(new_name)
                    print("Name updated successfully!")

                elif choice == 2:
                    new_age = ManagementSystem.get_valid_int("Enter new age :- ", 5, 100)
                    student.update_age(new_age)
                    print("Age updated successfully!")

                elif choice == 3:
                    new_email = ManagementSystem.get_valid_email("Enter new email :- ")
                    student.update_email(new_email)
                    print("Email updated successfully!")

                elif choice == 4:
                    new_roll_no = ManagementSystem.get_valid_int("Enter new roll_no :- ", 1, 9999)
                    student.update_roll_no(new_roll_no)
                    print("Roll number updated successfully!")

                elif choice == 5:
                    print("Update completed!")
                    break
        else:
            print("Student Not Found!")

    def delete_student(self):
        std_id = input("Student ID :- ")

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
        name = ManagementSystem.get_valid_text("Enter your name :- ")
        age = ManagementSystem.get_valid_int("Enter your age :- ", 5, 100)
        email = ManagementSystem.get_valid_email("Enter your email :- ")
        subject = ManagementSystem.get_valid_text("Enter the subject you teach :- ").capitalize()

        new_teacher = Teacher(emp_id, name, age, email, subject)
        self.teachers[emp_id] = new_teacher
        self.next_teacher_id += 1

        print("Teacher Registered Successfully!")
        print(f"Employee ID :- {emp_id}")

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

                choice = ManagementSystem.get_valid_int("Enter your choice :- ", 1, 5)

                if choice == 1:
                    new_name = ManagementSystem.get_valid_text("Enter new name :- ")
                    teacher.update_name(new_name)
                    print("Name updated successfully!")

                elif choice == 2:
                    new_age = ManagementSystem.get_valid_int("Enter new age :- ", 5, 100)
                    teacher.update_age(new_age)
                    print("Age updated successfully!")

                elif choice == 3:
                    new_email = ManagementSystem.get_valid_email("Enter new email :- ")
                    teacher.update_email(new_email)
                    print("Email updated successfully!")

                elif choice == 4:
                    new_subject = ManagementSystem.get_valid_text("Enter new subject :- ").capitalize()
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
    
    def get_students_data(self):
        students_data = {}
        for student_id, student in self.students.items():
            students_data[student_id] = student.to_dict()
        return students_data

    def get_teachers_data(self):
        teachers_data = {}
        for emp_id, teacher in self.teachers.items():
            teachers_data[emp_id] = teacher.to_dict()
        return teachers_data

    def get_data(self):
        data = {
            "students": self.get_students_data(),
            "teachers": self.get_teachers_data()
        }
        return data

    def save_data_to_file(self, filename):
        data = self.get_data()
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_students_data(self, data):
        for student_id, student_info in data.items():
            student = Student(
                student_id=student_info["student_id"],
                name=student_info["name"],
                age=student_info["age"],
                email=student_info["email"],
                roll_no=student_info["roll_no"]
            )
            for subject, grade in student_info.get("grades", {}).items():
                student.add_grade(subject, grade)
            self.students[student_id] = student

    def load_teachers_data(self, data):
        for emp_id, teacher_info in data.items():
            teacher = Teacher(
                emp_id=teacher_info["emp_id"],
                name=teacher_info["name"],
                age=teacher_info["age"],
                email=teacher_info["email"],
                subject=teacher_info["subject"]
            )
            self.teachers[emp_id] = teacher

    def load_data_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.load_students_data(data.get("students", {}))
                self.load_teachers_data(data.get("teachers", {}))

                self.recalculate_next_ids()
        except FileNotFoundError:
            print("\nNo saved data found. Starting fresh!")
        except json.JSONDecodeError:
            print("\nError reading data file. Starting fresh!")

    def recalculate_next_ids(self):
        students_ids = []
        for student_id in self.students.keys():
            students_ids.append(int(student_id[3:]))
        highest_student_id = max(students_ids) if students_ids else 0
        self.next_student_id = highest_student_id + 1

        teachers_ids = []
        for emp_id in self.teachers.keys():
            teachers_ids.append(int(emp_id[3:]))
        highest_teacher_id = max(teachers_ids) if teachers_ids else 0
        self.next_teacher_id = highest_teacher_id + 1

system = ManagementSystem()
system.load_data_from_file("data.json")

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
    print("press 0 to exit")

    choice = ManagementSystem.get_valid_int("Enter your choice :- ", 0, 9)

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

    elif choice == 0:
        system.save_data_to_file("data.json")
        print("Exiting... Goodbye!")
        break