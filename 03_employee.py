class Employee:
    company = "Google"
    salary = 100

harry = Employee()
nehal = Employee()
print(harry.company)
print(nehal.company)
Employee.company = "YouTube"
print(harry.company)
print(nehal.company)


#  Instance Attribute :-> An attribute that belong to the Instance (object) Assuming the class from the previous example:

harry.salary = 300
nehal.salary = 400

print(harry.salary)
print(nehal.salary)