class Point:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y, self.z + other.z)

  def __str__(self):
    return f'x: {self.x}, y: {self.y}, z: {self.z}'

point1 = point(3, 4, -5)
point2 = point(-4, 1, 3)

point3 = point1 + point2

print(point3)