class Person:
  def __init__(self, first_name, last_name):
    self.first = first_name
    self.last = last_name

  def speak(self):
    print("My name is  "+ first + " " + last)

me = Person("Brandon", "Walsh")
you = Person("Ethan", "Reed")

me.speak()
