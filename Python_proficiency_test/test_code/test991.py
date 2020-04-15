def foo(x,y,z):
    print("x=" + str(x))
    print("y=" + str(y))
    print("z=" + str(z))

mydict = {'p':1,'q':2,'r':3}
foo(**mydict)