'''name = "Mohammad"
age = 33

print(name)
print(age)

name = "Ahmad"
print(name)
'''

"""
a = b = c = 18

print(a, b, c)

a = 10; b = 20; c = 30

print(a, b, c)
"""

'''
name = "Mohammad"
age = 33

print(type(name))
print(type(age))
'''

"""
x = 3.14
y = 2.178

print(type(x))
"""

'''
info = """ مرحبا! اسمي محمد وعمرى 32 عاما
أعمل مبرمجا وأستخد لغة بايثون """

print(info)

print("Mohammad " "Taher" )

First_name = "Mohammad"
last_name = "Taher"
full_name = First_name + last_name

print(full_name)
age = 24

print(full_name + age) #EROOR!
'''

"""
language = "Arabic"
print(language[0])
print(language[-1])
print(language[0:2])
print(language[:2])
print(language[4:])
print(len(language))
"""

'''
First_name = "Abdallah"
last_name = "Mohammad"
# Extract the first letters
first_initial = First_name[0]
last_initial = last_name[0]

# Concatenate the initials
initials = first_initial + last_initial

print(initials)
'''

"""
name = input("Enter your name:")
if len(name) > 0:
  print('Hello, ' + name + ', Welcome to our programA.')
else:
    print('Sorry, you did not write your name.')
"""

'''
for x in range(0, 100):
  print(x)
'''

"""
def decorator(function):
  def inner(*args, **kwargs):
    print("=" * 20)
    function(*args, *kwargs)
    print("=" * 20)
  return inner

@decorator
def write(name):
  print(name)

write('Mohammad')
"""

