import datetime
from abc import ABC, abstractmethod

class Employee(ABC):
    total = 0
    salary_raise = 1.1

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Employee.total += 1
        self.profile = None

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def _calculate_salary(self):
        pass

    @classmethod
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

class Salary:
    def __init__(self, salary):
        self.salary = salary


    def calculate_salary(self):
        return self.salary

@staticmethod
def is_workday(day):
  if day.weekday() == 4 or day.weekday() == 5:
    return False
  return True

date = datetime.date(2021, 5, 18)
print(Employee.is_workday(date))

