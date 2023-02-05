class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        sum = self.num1+self.num2
        return sum
    def subtraction(self):
        # if self.num1 <= self.num2:
        #     return self.num2-self.num1
        # else:
        return self.num1-self.num2
    def multiplication(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num1 / self.num2

cal = Calculator(1,3)

print("Addition is : ",cal.addition())
print("Subtraction is : ",cal.subtraction())
print("Multiplication is : ",cal.multiplication())
print("Division is : ",cal.divide())