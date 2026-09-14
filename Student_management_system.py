class Student:

    students = [] #This list will store all student objects.
    
   #  #This defines what each individual student object contains. so kind of object behaviour
    # A class serves as a blueprint or template that defines the properties (attributes) and 
     # behavior (methods) for objects, while an object is a specific instance created from that class 
      #that follows these defined rules """
    def __init__(self, student_id, name, age, student_class, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.student_class = student_class
        self.marks = marks

    # Add student . classmethod is a method that belong to the class . it is for the class not for 
    #particular object  
    # cls is a argument of class itself means it is student itself ..
    @classmethod
    def add_student(cls):
        print("\n--- Add Student ---")

        student_id = input("Enter Student ID: ")

        # Check duplicate ID
        for student in cls.students:
            if student.student_id == student_id:
                print("Student ID already exists!")
                return

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        student_class = input("Enter Class: ")
        marks = float(input("Enter Marks: "))
# 'student' is a variable that stores the newly created Student object.
        student = cls(
            student_id,
            name,
            age,
            student_class,
            marks
        )

        cls.students.append(student)
        # student = cls(...) means student = Student(...)
# because cls refers to the Student class.
        # here student = cls(...) means student=student(...)
        # now cls.students means student class connecting with students[] and there we 
        #appending student variable which contain std id , name , age, student class, marks
        

        print("Student added successfully!")

    # View all students
    @classmethod
    def view_students(cls):
        print("\n--- All Students ---")

        if not cls.students:
            print("No students found.")
            return

        for student in cls.students:
            print("-------------------------")
            print("ID:", student.student_id)
            print("Name:", student.name)
            print("Age:", student.age)
            print("Class:", student.student_class)
            print("Marks:", student.marks)

    # Search student 
    @classmethod
    def search_student(cls):
        print("\n--- Search Student ---")

        student_id = input("Enter Student ID: ")

        for student in cls.students:
            if student.student_id == student_id:

                print("\nStudent Found!")
                print("-------------------------")
                print("ID:", student.student_id)
                print("Name:", student.name)
                print("Age:", student.age)
                print("Class:", student.student_class)
                print("Marks:", student.marks)

                return

        print("Student not found.")

    # Update student
    @classmethod
    def update_student(cls):
        print("\n--- Update Student ---")

        student_id = input("Enter Student ID: ")

        for student in cls.students:

            if student.student_id == student_id:

                print("Student found.")

                student.name = input("Enter new name: ")
                student.age = int(input("Enter new age: "))
                student.student_class = input("Enter new class: ")
                student.marks = float(input("Enter new marks: "))

                print("Student updated successfully!")

                return

        print("Student not found.")

    # Delete student
    @classmethod
    def delete_student(cls):
        print("\n--- Delete Student ---")

        student_id = input("Enter Student ID: ")

        for student in cls.students:

            if student.student_id == student_id:

                cls.students.remove(student)

                print("Student deleted successfully!")

                return

        print("Student not found.")

    # Calculate result
    @classmethod
    def calculate_result(cls):
        print("\n--- Student Result ---")

        student_id = input("Enter Student ID: ")

        for student in cls.students:

            if student.student_id == student_id:

                marks = student.marks

                if marks >= 80:
                    grade = "A+"
                elif marks >= 70:
                    grade = "A"
                elif marks >= 60:
                    grade = "B"
                elif marks >= 50:
                    grade = "C"
                elif marks >= 40:
                    grade = "D"
                else:
                    grade = "F"

                if marks >= 40:
                    result = "PASS"
                else:
                    result = "FAIL"

                print("\n-------------------------")
                print("Name:", student.name)
                print("Marks:", marks)
                print("Grade:", grade)
                print("Result:", result)
                print("-------------------------")

                return

        print("Student not found.")




# python code work from top to down ......suddenly after seeing def function python dont 
# start executing that unless that function is not called 

def main():
  while True:

    print("\n==============================")
    print("    STUDENT MANAGEMENT SYSTEM")
    print("==============================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Result")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        Student.add_student()

    elif choice == "2":
        Student.view_students()

    elif choice == "3":
        Student.search_student()

    elif choice == "4":
        Student.update_student()

    elif choice == "5":
        Student.delete_student()

    elif choice == "6":
        Student.calculate_result()

    elif choice == "7":
        print("Program ended.")
        break

    else:
        print("Invalid choice!")
        
        # -----------------------------
# Main Program
#  program start working from here ..-----------------------------
        
  if __name__ == "__main__":
  # __name__ is a special variable automatically created by Python for every file.
    # If we run this file directly, Python sets __name__ to "__main__".
    # So, main() will be called and the program will start
    main()
    