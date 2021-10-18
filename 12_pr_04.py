print("*******Entering into the calculator*******\n")
name = input("Plz, Sir ---> Write your name first to enter the calculator: ")

class Calculator:
    def __init__(self, num):
        self.number = num
        

    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")

    def squareRoot(self):
        print(f"The value of {self.number} squareRoot is {self.number **0.5}")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number **3}")
    @staticmethod
    def greet():
        print(f"\tHellow there <{name}> welcome to the calculato\n")


z = Calculator("name")   
z.greet()


num1 = int(input("Enter the number to get square of that number: "))
num2 = int(input("Enter the number to get squareRoot of that number: "))
num3 = int(input("Enter the number to get cube of that number: "))

a = Calculator(num1)
a.square()

b = Calculator(num2)
b.squareRoot()

c = Calculator(num3)
c.cube()




