class MyClass:
    def __init__(self, i):
          self.i = i

    def get(self):
          #func_name = 'function' + str(self.i)
          #self.func_name()
      func_name = 'function' + str(self.i)
      func = getattr(self,func_name) 
      func()

    def function1(self):
          # do something
          pass

    def function2(self):
          # do something
          pass

obj = MyClass(1)
obj.get()