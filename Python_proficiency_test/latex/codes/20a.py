## fib.py
def fib(n):
    if n < 2:
        return n
    else: 
        return fib(n-1) + fib(n-2)

fib(35)
fib(35)
print("Done")

## fib_parallel.py
from threading import Thread
def fib(n):
    if n < 2:
        return n
    else: 
        return fib(n-1) + fib(n-2)

t1 = Thread(target=fib, args=(5, ))
t1.start()

t2 = Thread(target=fib, args=(5, ))
t2.start()

t1.join()
t2.join()
print("Done")