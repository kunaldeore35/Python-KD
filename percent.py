class Per:
    def __init__(self,physics,chemistry,bio,math):
        self.physics = physics
        self.chemistry = chemistry
        self.bio = bio
        self.math = math
    def percent(self):
        total = self.physics+self.chemistry+self.bio+self.math
        perc = total / 4
        return perc
    def pr(self):
        print("Your percentage is : ",self.percent())

cl = Per(70,80,90,70)
cl.pr()
