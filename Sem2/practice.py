# class Student:
#     # Class attribute to store student data
#     students = []

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         # Add the new student to the class attribute 'students'
#         Student.students.append(self)

#     @classmethod
#     def add_student(cls, name, age):
#         # Class method to add a new student
#         new_student = cls(name, age)
#         print(f"Student {name} added.")

#     @classmethod
#     def get_total_students(cls):
#         # Class method to get the total number of students
#         return len(cls.students)

#     @classmethod
#     def display_students(cls):
#         # Class method to display information of all students
#         print("List of Students:")
#         for student in cls.students:
#             print(f"Name: {student.name}, Age: {student.age}")

# # Creating instances of the Student class
# student1 = Student("Alice", 20)
# student2 = Student("Bob", 22)

# # Calling class method on the class to add a new student
# Student.add_student("Charlie", 21)

# # Calling class method on an instance to add another new student
# student3 = Student("David", 23)
# student3.add_student("Eva", 19)

# # Calling class method on the class to display total students
# total_students = Student.get_total_students()
# print(f"Total students: {total_students}")

# # Calling class method on an instance to display student information
# student1.display_students()


class Example:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def class_method(cls):
        print(f"Class method called. Class variable: {cls.class_variable}")

    def instance_method(self):
        print(f"Instance method called. Instance variable: {self.instance_variable}")

# Creating an instance of the Example class
obj = Example("I am an instance variable")

# Calling class method on the class and instance
Example.class_method()  # Output: Class method called. Class variable: I am a class variable
obj.class_method()      # Output: Class method called. Class variable: I am a class variable

# Calling instance method on the instance
obj.instance_method()   # Output: Instance method called. Instance variable: I am an instance variable


Example.instance_method()