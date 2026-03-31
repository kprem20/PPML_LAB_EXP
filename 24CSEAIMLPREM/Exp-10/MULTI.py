class father():
    def skill1(self):
        print("Father Skill 1")
class Mother(father):
    def skill2(self):
        print("Mother Skill 2")
class Child(Mother):
    def skill3(self):
        print("Child IS......")
        
d=Child()
d.skill1()
d.skill2()
d.skill3()
