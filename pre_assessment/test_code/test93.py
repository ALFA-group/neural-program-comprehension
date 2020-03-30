class MyFloat(object):
  def __init__(self, a):
    self.a = a

  def __mul__(self, other):
    return MyFloat(self.a * other.a)

  def __repr__(self):
    return str(self.a)


class MyFloatExt(MyFloat):
  def __init__(self, a):
    MyFloat.__init__(self, a)

  def __add__(self, other):
    return MyFloatExt(self.a + other.a)

  def __mul__(self, other):
    pass

a = MyFloatExt(0.5)
b = MyFloatExt(1.5)

c = a + b
print(c)

d = a * b
print(d)

e = d * c
print(e)

f = e * 0.5
print(f)