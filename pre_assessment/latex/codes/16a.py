## base.py
class Parent():
    def __init__(self):
        print('in init')


## inherit.py
import base
class Visitor(base):
    pass
instance = Visitor()