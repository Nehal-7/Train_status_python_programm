class Employee:
    company = "Google"
    salary = 100
    location = "osmanabad"

harry = Employee()
nehal = Employee()
print(harry.company)
print(nehal.company)
Employee.company = "YouTube"
print(harry.company)
print(nehal.company)


#  Instance Attribute :-> An attribute that belong to the Instance (object) Assuming the class from the previous example:

# harry.salary = 300
# nehal.salary = 400

print(harry.salary)
print(nehal.salary)
# nehal.location = "Mumbai"
harry.location = "uttarpardesh"
print(nehal.location)
print(harry.location)
# print(harry.address)     # First it search address in Intance Attribute if not present then it go to Class Attribute if not present it will throw error if present it will written address


#  WHAT IS MEAN BY self ?  ===>  self reference to the instance of the class It is automatically passed with a function call from an object
#  For example ===>    nehal.getSalary() ---> here self is nehal
#                                      above parenthesis () equivalent to Employee getSalary(self)