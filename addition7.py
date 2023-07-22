#accepting input in python
#best code of addition in python

def Addition(value1,value2):
    ans=value1+value2
    return ans

def main():
    print("Enter first number : ")
    no1=int(input())
    print("Enter second number : ")
    no2=int(input())

    ans=Addition(no1,no2)
    print("Addition is : ",ans)

#starter
if __name__=="__main__":
    main()