class calculator:
    def __init__(self, a, b):
        self.x = a
        self.y = b 
    
    def summ(self):
        zx = self.x + self.y 
        print(f"the sum of {self.x} and {self.y} is : {zx}")
    
    def subb(self):
        zx = self.x - self.y 
        print(f"the subtraction of {self.x} and {self.y} is : {zx}")
    
    def multi(self):
        zx = self.x * self.y 
        print(f"the multiplication of {self.x} and {self.y} is : {zx}")
    
    def division(self):
        zx = self.x / self.y 
        print(f"the division of {self.x} and {self.y} is : {zx}")
    
    def modulus(self):
        zx = self.x % self.y 
        print(f"the modulus of {self.x} and {self.y} is : {zx}")
    
    def exponantional(self):
        zx = self.x ** self.y
        print(f"the exponantional of {self.x} and {self.y} is : {zx}")