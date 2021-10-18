class RailwayForm:
    FormType = "Railwayform"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

harrysapplication = RailwayForm()
harrysapplication.name = "Harry"
harrysapplication.train = "Rajdhani Express"
harrysapplication.printData()
