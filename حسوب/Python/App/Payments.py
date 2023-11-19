class Salary:
  def __init__(self, salary):
    self.salary = salary

  def calculate_salary(self):
    return self.salary

class HourlyPayment:
  def __init__(self, work_hours, hour_rate):
    self.work_hours = work_hours
    self.hour_rate = hour_rate

  def _calculate_salary(self):
    return self.work_hours * self.hour_rate