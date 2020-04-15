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

  def __mul__(self, other):
    #Complete this method

















a = MyFloatExt(0.5)
b = MyFloatExt(1.5)

d = a * b
f = d * 0.5
g = 0.5 * a
h = 0.5 * 0.5