class Remote:
    pass

class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveTop(self):
        pass
    def moveDown(self):
        pass

remote1 = Remote()
player1 = Player()

if(remote1.isLeftPressed()):
    player1.moveLeft()


# Abstraction : - without revealing implementation details
# Incapsulation : - One entity things rap in one cap. or you can say same entity thing put into same class for example remote related things are putted in remote class or player related things putted in player class


#  Modeling a problem in OOPS
# Name ---> Class ---> Employee
# Adjective ---> Attributes ---> name, age, salary
# Verbs ---> Methods ---> getsalary(), increament()


# There are two types of attributes
# 1 - Class Attributes
# 2 - Instance Attributes


#  An attribute that belongsd to the class rather than a particular object.
#  Example ===> 
    #           Class Employee:
        #           company = "Google"
            #   harry = Employee()
            #   nehal = Employee()
            #   Employee.company = "YouTube"