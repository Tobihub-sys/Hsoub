'''
class Employee:
  pass

ahmad = Employee()
yasameen = Employee()

print(ahmad)
print(yasameen)

print(ahmad == yasameen)
'''


"""
class Employee:
  pass

ahmad = Employee()
yasameen = Employee()

ahmad.full_name = 'Ahmad Kamal'
ahmad.title = 'Accountant'
ahmad.salary = 3000

yasameen.full_name = 'Yasameen Hasan'
yasameen.title = 'Archive'
yasameen.salary = 3200

print(ahmad.full_name)
print(ahmad.title)
print(yasameen.salary)
"""


import datetime
from abc import ABC, abstractmethod

class Employee(ABC):
    total = 0
    salary_raise = 1.1

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Employee.total += 1

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def calculate_salary(self):
        pass

    @classmethod
    @abstractmethod
    def from_string(cls, string):
        first_name, last_name, title, salary = string.split('-')
        salary = int(salary)
        return cls(first_name, last_name, salary)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 4 or day.weekday() == 5:
            return False
        return True

class Manager(Employee):
    def __init__(self, first_name, last_name, salary, employees=None):
        super().__init__(first_name, last_name)
        self.__salary = salary
        if employees is None:
            employees = []
        self.employees = employees

    def get_employees(self):
        print("Employees:")
        print("=" * 10)
        employees_list = []
        for number, employee in enumerate(self.employees):
            employees_list.append(f"{number + 1 }. {employee.info()}")
        return '\n'.join(employees_list)

    def info(self):
        return f'Name: {self.first_name} {self.last_name}; Job Title: {self.__class__.__name__}'

    def calculate_salary(self):
        return self.__salary

anwar = Manager('Anwar', 'Khaled', 5000)

class Programmer(Employee):
    def __init__(self, first_name, last_name, salary, lang, projects=None):
        super().__init__(first_name, last_name)
        self.__salary = salary
        self.lang = lang
        if projects is None:
            projects = []
        self.projects = projects

    def info(self):
        return f'Name: {self.first_name} {self.last_name}; Job Title: {self.__class__.__name__}'

    def calculate_salary(self):
        return self.__salary

    @classmethod
    def from_string(cls, string):
        first_name, last_name, title, salary, lang = string.split('-')
        salary = int(salary)
        return cls(first_name, last_name, salary, lang)

    def assign_project(self, project):
        self.projects.append(project)

class Accountant(Employee):
    pass

class Programmer(Employee):
    pass

date = datetime.date(2021, 5, 18)
print(Employee.is_workday(date))


"""
class Profile:
  def __init__(self, adress, phone_number, email, married):
    self.adress = adress
    self.phone_number = phone_number
    self.email = email
    self.married = married

  def __str__(self):
    return f'{self.address}, {self.phone_number}, Email: {self.email}. Marital Status: {"Married" if self.married else "single"}'
"""


"""
class Wishlist:
  def __init__(self, items):
    self.items = list(items)

  def __len__(self):
    return len(self.items)

my_wishlist = Wishlist(['Python 3 Object-Oriented Programming', 'How to make mistakes in python', 'python Essential Reference'])

print(len(my_wishlist  ))
"""