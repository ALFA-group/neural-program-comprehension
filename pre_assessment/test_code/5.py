## file two.py
import one
print("5") # top-level in two.py
one.func()

if __name__ == "__main__":
  print("6") # two.py is being run directly
else:
  print("7") # two.py imported into another module
