class calculator:
    def __init__(self,n):
        self.n=n

    def add(self):
        print(f"the square is {self.n*self.n} ")
    def cube(self):
        print(f"the cube is {self.n*self.n*self.n} ")
    def squareroot(self):
        print(f"the square is {self.n**0.5} ")

a=calculator(4)
a.add()
a.cube()
a.squareroot()