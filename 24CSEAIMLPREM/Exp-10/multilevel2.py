class Grandparents():
    def property(self):
        print("Grandparents Property")
class Parents(Grandparents):
    def bussines(self):
        print("Bussiness for child ")
class Child(Parents):
    def Education(self):
        print("Educationn with father money ")
obj=Child()
obj.property()
obj.bussines()
obj.Education()