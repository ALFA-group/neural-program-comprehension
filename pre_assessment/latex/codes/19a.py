class MyClass:
  def __init__(self, i):
    self.i = i

  def get(self):
    func_name = 'function'+str(self.i)
    self.func_name()

  def function1(self):
    print("Hello")

  def function2(self):
    print("There")

obj = MyClass(1)
obj.get()