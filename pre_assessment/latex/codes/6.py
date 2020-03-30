def foo(param1, *param2):
    print(param1)
    print(param2)
def bar(param1, **param2):
    print(param1)
    print(param2)
foo(1,2,3,4,5)
bar(6,a=7,b=8)
