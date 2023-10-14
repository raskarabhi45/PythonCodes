##############################################revisee
# main file for the decorater in python
# design pattern in python
# this function is written by the other developer and we are not allowed to change in this function
# need to  study this more and more clearly for good clarification of the concept

def subtraction(no1,no2):
    ans=0
    ans=no1-no2
    return ans

def Decorated_Function(Function_Name):     #like updator 
    def Inner(A,B):
        if(A<B):
            A,B=B,A                        #multiassignment statement  #swap
        output=Function_Name(A,B)
        return output
    return Inner

    
def main():
    value1=int(input("Enter first number : "))
    value2=int(input("Enter second number : "))

    New_Funtion=Decorated_Function(subtraction)
    ret=New_Funtion(value1,value2)
    print("Subtracion is : ",ret)

if __name__ =="__main__":
    main()