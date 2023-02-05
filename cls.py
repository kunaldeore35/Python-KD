class Mycls:
    def __init__(self,name,age):
        self.name= name
        self.age= age
    def call(self):
        return f"Name is:{self.name} \nAge is:{self.age}"
        # return f"{self.name}, {self.age}"
        # print("Name is : ",self.name)
        # print("Age is : ",self.age)
cl = Mycls("Kunal",23)
print(cl.call())