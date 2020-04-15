class X():
  def foo(self):
    print("a")

class Y(X):
  def foo(self):
    super(Y, self).foo()
    print("b")

yobj = Y()
yobj.foo()