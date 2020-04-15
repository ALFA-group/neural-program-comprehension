def foo1(x):
    def foo(*args, **kwargs):
        print("*"* 2)
        x(*args, **kwargs)
        print("*"* 2)
    return foo

def foo2(x):
    def foo(*args, **kwargs):
        print("%"* 2)
        x(*args, **kwargs)
        print("%"* 2)
    return foo

@foo1
@foo2
def foo3(m):
    print(m)

foo3("hello")