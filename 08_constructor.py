class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):                   # constructor __init__ it automatically run withou we call it
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")
    
    def getDetails(self):
        print(f"The name of the employee is  {self.name}")
        print(f"The salary of the employee is  {self.salary}")
        print(f"The subunit of the employee is  {self.subunit}")


    def getSalar(self, signature):
        print("Salary is 100k")
        print(f"Name is{self.name} \n Salary is {self.salary}")
        print(f"Salary for this employee working in {self.company} is {self.salary} \n {signature}")
    @staticmethod
    def greet(name):      #  without giving self arrgument to the function we use @staticmethod  here name is paramater just like above example
        print("Good Morning, Sir",f"{name}")



harry = Employee("Harry", 100, "YouTube")
# harry = Employee()
harry.salary = 10000
harry.name = " Harry"
harry.getSalar("Thanks!")
harry.greet("nehal shaikh")
harry.getDetails()




# def funcname(self, parameter_list):

