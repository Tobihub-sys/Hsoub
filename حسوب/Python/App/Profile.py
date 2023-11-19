class Profile:
  def __init__(self, address, phone_number, email, married):
    self.address = address
    self.phone_number = phone_number
    self.email = email
    self.married = married

  def __str__(self):
    return f'{self.address}, {self.phone_number}. Email: {self.email}. Martial Status: {"Married" if self.married else "Single"}'