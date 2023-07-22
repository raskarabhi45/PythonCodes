#OOP Approach in python
#accpet number and perform addition and subtraction of it

#kay kraych aahe  Behaviours(functions)
#addition and subtraction

#te krayla kay lagnar aahe  characteristics(data)
# 2 numbers

# class = Characteristics + Behaviours
# class = Data + Functions

# this pointer = self in python

class Arithmetic:
    def __init__(self,A,B):
        self.no1=A
        self.no2=B

    def Add(self):
        return self.no1+self.no2

    def Sub(self):
        return self.no1-self.no2


def main():
    print("Enter first number")
    value1=int(input())

    print("Enter second number")
    value2=int(input())

    obj=Arithmetic(value1,value2)

    Ans=obj.Add()
    print("Addition is : ",Ans)

    Ans=obj.Sub()
    print("Subtraction is : ",Ans)


if __name__=="__main__":
    main()