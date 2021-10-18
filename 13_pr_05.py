
class Train:
    def __init__(self, name, fare, seats,):
        self.name = name
        self.fare = fare
        self.seats = seats
    
    def Status(self):
        print(f"The name of the train is: {self.name}")
        print(f"The seats available in the train is: {self.seats}")
    
    def fareInfo(self):
        print(f"The ticket of the train is : {self.fare}")



fare = {"Mumbai":"400", "Latur":"150", "Pune":"250", "Hyderabad":"300"}
seats = {"Mumbai":"60", "Latur":"100", "Pune":"150", "Hyderabad":"90"}
n = input("Enter the trian name: ")
n = n.capitalize()

Express = Train(n,(fare[f"{n}"]),(seats[f"{n}"]))
Express.Status()
Express.fareInfo()


"added this line for checking git branch and it is adding to new_branch_test"