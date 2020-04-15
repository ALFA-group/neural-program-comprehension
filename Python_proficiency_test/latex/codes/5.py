## file one.py
def func():
  print("1") # func() in one.py

print("2") # top-level in one.py

if __name__ == "__main__":
  print("3") # one.py is being run directly
else:
  print("4") # one.py imported into another module


## file two.py
import one
print("5") # top-level in two.py
one.func()

if __name__ == "__main__":
  print("6") # two.py is being run directly
else:
  print("7") # two.py imported into another module
