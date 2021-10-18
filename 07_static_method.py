class Employee:
    company = "Google"
    def getSalar(self, signature):
        print("Salary is 100k")
        print(f"Name is{self.name} \n Salary is {self.salary}")
        print(f"Salary for this employee working in {self.company} is {self.salary} \n {signature}")
    @staticmethod
    def greet(name):      #  without giving self arrgument to the function we use @staticmethod  here name is paramater just like above example
        print("Good Morning, Sir",f"{name}")




harry = Employee()
harry.salary = 10000
harry.name = " Harry"
harry.getSalar("Thanks!")
harry.greet("nehal shaikh")



# def funcname(self, parameter_list):

