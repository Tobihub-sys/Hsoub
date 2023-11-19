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

    @classmethod
    def from_string(cls, string):
        first_name, last_name, title, salary, lang = string.split('-')
        salary = int(salary)
        return cls(first_name, last_name, salary, lang)


