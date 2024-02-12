
# class Calculator:
#     def __init__(self):
#         print('Calculator initiated')
#     def add(self, num1, num2):
#         return num1 + num2
#     def subtract(self, num1, num2):
#         return num1 - num2
#     def multiply(self, num1, num2):
#         return num1 * num2
#     def divide(self, num1, num2):
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "Error: Division by zero."
#     def __del__(self):
#         print('Ended')
    
# object1=Calculator()
# print(object1.add(4,2),
#       object1.subtract(4,2),
#       object1.multiply(4,2),
#       object1.divide(4,2))



# class Student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#     def tellname(self):
#         return self.name
#     def tellrollno(self):
#         return self.rollno

# student1=Student('Rupam',43)
# print(f"{student1.tellname()} and {student1.tellrollno()}")

# class Employee:
#     def __init__(self, name, employee_id, hourly_rate):
#         self.name = name
#         self.employee_id = employee_id
#         self.hourly_rate = hourly_rate
#         self.hours_worked = 0

#     def record_hours_worked(self, hours):
#         self.hours_worked += hours

#     def calculate_salary(self):
#         salary = self.hours_worked * self.hourly_rate
#         return salary

# askname=input("Enter employee name: ")
# askid=input("Enter employee id: ")
# askrate=eval(input("Enter hourly pay rate for total salary evaluation: "))
# emp1 = Employee(askname, askid, askrate)

# askhours=eval(input("Enter number of hours worked by employee: "))
# emp1.record_hours_worked(40)

# salary = emp1.calculate_salary()
# print(f"{emp1.name}'s salary is ${salary:.2f}")

# class ToDo:
#     def __init__(self):
#         self.tasklist=[]
#     def add_tasks(self,task):
#         self.tasklist.append(task)
#     def show_tasks(self):
#         # count=1
#         # for task in self.tasklist:
#         #     print(f'{count}. {task}')
#         #     count+=1
#         for task_num, task in enumerate(self.tasklist, start=1):
#             print(f"{task_num}. {task}")

#     def finish_tasks(self):
#         pass

# mylist=ToDo()

# mylist.add_tasks('Wake up')
# mylist.add_tasks('Brush teeth')
# mylist.add_tasks('Go to college')

# mylist.show_tasks()

# finished=int(input("Enter the task number which has been completed"))
# if 0 < finished <= len(mylist.tasklist) and finished

# class ToDo:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, task, completed=False):
#         task_dict = {"task": task, "completed": completed}
#         self.tasks.append(task_dict)
#         print(f"Task '{task}' added successfully.")

#     def mark_as_completed(self, task_number):
#         if 1 <= task_number <= len(self.tasks):
#             task = self.tasks[task_number - 1]
#             if not task["completed"]:
#                 task["completed"] = True
#                 print(f"Task '{task['task']}' marked as completed.")
#             else:
#                 print(f"Task '{task['task']}' is already completed.")
#         else:
#             print("Invalid task number. Please enter a valid task number.")

#     def display_tasks(self):
#         print("Tasks:")
#         for i, task in enumerate(self.tasks, start=1):
#             status = "Completed" if task["completed"] else "Not Completed"
#             print(f"{i}. {task['task']} - {status}")

# todo_list = ToDo()

# todo_list.add_task("Complete project")
# todo_list.add_task("Read a book", completed=True)
# todo_list.display_tasks()

# while True:
#     task_number = int(input("Enter the task number to mark as completed: "))
#     todo_list.mark_as_completed(task_number)
#     todo_list.display_tasks()
#     if input("Wish to exit?")=='y':
#         break
#     else:
#         print("Running again")
    
# class Car:
#     def __init__(self, model, color, daily_rate):
#         self.model = model
#         self.color = color
#         self.daily_rate = daily_rate
#         self.total_days_rented = 0

#     def rent(self, days):
#         if days > 0:
#             self.total_days_rented += days
#             print(f"Rented {self.color} {self.model} for {days} days.")
#         else:
#             print("Invalid rental duration. Please rent for at least one day.")

#     def calculate_rental_cost(self):
#         return self.total_days_rented * self.daily_rate

#     def return_car(self):
#         if self.total_days_rented > 0:
#             print(f"Returned {self.color} {self.model}. Rental cost: ${self.calculate_rental_cost():.2f}")
#             self.total_days_rented = 0
#         else:
#             print("Car not rented yet.")


# car1 = Car(model="Toyota Camry", color="Blue", daily_rate=30.0)

# car1.rent(5)  # Rent the car for 5 days
# car1.return_car()

# car2 = Car(model="Honda Accord", color="Red", daily_rate=25.0)

# car2.rent(3)  # Rent the car for 3 days
# car2.return_car()


class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient funds for withdrawal.")

    def check_balance(self):
        print(f"Current balance for {self.account_holder}: ${self.balance:.2f}")

# Example usage:
if __name__ == "__main__":
    account1 = BankAccount(account_holder="John Doe", balance=1000.0)

    account1.check_balance()

    account1.deposit(500.0)
    account1.withdraw(200.0)
    account1.check_balance()

# import math

# class Shape:
#     def calculate_area(self):
#         pass  # This method will be overridden by specific shape classes

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def calculate_area(self):
#         return self.side ** 2

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         return self.length * self.width

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return math.pi * self.radius ** 2

# # Example usage:
# if __name__ == "__main__":
#     square = Square(side=5)
#     rectangle = Rectangle(length=4, width=6)
#     circle = Circle(radius=3)

#     print(f"Area of square: {square.calculate_area()}")
#     print(f"Area of rectangle: {rectangle.calculate_area()}")
#     print(f"Area of circle: {circle.calculate_area():.2f}")


# class Time:
#     def __init__(self, seconds=0):
#         self.seconds = seconds

#     def seconds_to_minutes(self):
#         return self.seconds / 60

#     def minutes_to_hours(self):
#         return self.seconds / 3600

#     def minutes_to_seconds(self, minutes):
#         return minutes * 60

#     def hours_to_minutes(self, hours):
#         return hours * 60

#     def hours_to_seconds(self, hours):
#         return hours * 3600

# # Example usage:
# if __name__ == "__main__":
#     time_obj = Time(seconds=3600)

#     # Convert seconds to minutes and hours
#     print(f"{time_obj.seconds} seconds is equal to {time_obj.seconds_to_minutes():.2f} minutes.")
#     print(f"{time_obj.seconds} seconds is equal to {time_obj.minutes_to_hours():.2f} hours.")

#     # Convert minutes to seconds and hours
#     minutes_value = 30
#     print(f"{minutes_value} minutes is equal to {time_obj.minutes_to_seconds(minutes_value)} seconds.")
#     print(f"{minutes_value} minutes is equal to {time_obj.hours_to_minutes(minutes_value):.2f} hours.")

#     # Convert hours to minutes and seconds
#     hours_value = 2.5
#     print(f"{hours_value} hours is equal to {time_obj.hours_to_minutes(hours_value):.2f} minutes.")
#     print(f"{hours_value} hours is equal to {time_obj.hours_to_seconds(hours_value)} seconds.")

# import random

# class Dice:
#     def roll(self):
#         return random.randint(1, 6)

# # Example usage:
# if __name__ == "__main__":
#     dice = Dice()

#     # Roll the die multiple times
#     for _ in range(5):
#         result = dice.roll()
#         print(f"The die rolled: {result}")


# class LibraryBook:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.available = True

#     def borrow_book(self):
#         if self.available:
#             print(f"Book '{self.title}' by {self.author} has been borrowed.")
#             self.available = False
#         else:
#             print(f"Sorry, the book '{self.title}' is currently not available.")

#     def return_book(self):
#         if not self.available:
#             print(f"Book '{self.title}' by {self.author} has been returned.")
#             self.available = True
#         else:
#             print(f"This book is already available. No need to return.")

# # Example usage:
# if __name__ == "__main__":
#     book1 = LibraryBook(title="The Great Gatsby", author="F. Scott Fitzgerald")
#     book2 = LibraryBook(title="To Kill a Mockingbird", author="Harper Lee")

#     book1.borrow_book()
#     book1.return_book()

#     book2.borrow_book()
#     book2.borrow_book()
#     book2.return_book()
