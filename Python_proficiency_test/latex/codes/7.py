class A:
    def __init__(self):
        self.calcI(30)
        
    def calcI(self, i):
        self.i = 2 * i;

class B(A):
    def __init__(self):
        super().__init__()
        print("i from B is", self.i)
        
    def calcI(self, i):
        self.i = 3 * i;

b = B()