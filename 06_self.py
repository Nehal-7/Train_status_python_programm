class Employee:
    company = "Google"
    def getSalar(self):
        print("Salary is 100k")
        print(f"Name is{self.name} \n Salary is {self.salary}")
        print(f"Salary for this employee working in {self.company} is {self.salary}")

harry = Employee()
harry.salary = 10000
harry.name = " Harry"
harry.getSalar()




# def funcname(self, parameter_list):


