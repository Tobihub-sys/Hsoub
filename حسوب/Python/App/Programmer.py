from Employee import Employee
from Roles import *
from Payments import *

class Programmer(Employee, ProgrammerRole, Salary):
    def __init__(self, first_name, last_name, salary, lang, projects=None):
        salary.__init__(self, salary)
        ProgrammerRole.__init__(self, lang, projects)
        Employee.__init__(first_name, last_name)
        self.__salary = salary
        self.lang = lang
        if projects is None:
            projects = []
        self.projects = projects

    def info(self):
        return f'Name: {self.first_name} {self.last_name}; Job Title: {self.__class__.__name__}'

    def calculate_salary(self):
        return Salary.calculate_salary(self)

    @classmethod
    def from_string(cls, string):
        first_name, last_name, title, salary, lang = string.split('-')
        salary = int(salary)
        return cls(first_name, last_name, salary, lang)

    def assign_project(self, project):
        self.projects.append(project)

        def get_projects(self):
            print("Projects:")
            print("=" * 10)
            projects_list = []
            for number, project in enumerate(self.projects):
                projects_list.append(f"{number + 1}. {project}")
            return '\n'.join(projects_list)

    class FreelancerProgrammer(Employee, ProgrammerRole, HourlyPayment):
        def __init__(self, first_name, last_name, hour_rate, work_hours, lang, projects):
           HourlyPayment.__init__(self, work_hours, hour_rate)
           ProgrammerRole.__init__(self, lang, projects)
           Employee.__init__(self, first_name, last_name)

        def info(self):
            return f'Name: {self.first_name} {self.last_name}; Job Title: {self.__class__.__name__}; Work Hours: {self.work_hours}'

        def calculate_salary(self):
            return HourlyPayment.calculate_salary(self)