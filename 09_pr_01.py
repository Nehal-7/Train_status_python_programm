class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} Programmer is  {self.name} and the product is {self.product}")


nehal = Programmer("Nehal", "Skype")
ayaz = Programmer("Ayaz", "app")
faizan = Programmer("Faizan", "GitHub")
nehal.getInfo()
ayaz.getInfo()
faizan.getInfo()