
from re import A

class Arithmetic:
    #Constructor 
    def __init__(self,A,B):#like this keyword from cpp and java same as self keyward in python
        print("Inside init method")
        self.no1=A
        self.no2=B

    def Addition(self):
         ans=self.no1+self.no2
         return ans

    def Subtraction(self):
         ans=self.no1-self.no2
         return ans
   



def main():
    print("Inside main method")

    obj=Arithmetic(11,10)
    output=obj.Addition()
    print("Addition is ",output)
    output=obj.Subtraction()
    print("Subtraction is ",output)

    objX=Arithmetic(21,20)


if __name__=="__main__":
    print("Inside Starter")
    main()