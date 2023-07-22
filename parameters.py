# function parameters in python

# 1 Positional Arguments 
def add1(no1,no2):
    print("Value of no1 : ",no1)
    print("Value of no2 : ",no2)
    return no1+no2

# 2 keyword arguments
def sub1(no1,no2):
    print("Value of no1 : ",no1)
    print("Value of no2 : ",no2)
    return no1-no2

# 3 Default arguments

def main():
    ans=add1(10,11)
    print("Addition is : ",ans)

    ans=sub1(no2=10,no1=11)
    print("Subtraction is : ",ans)

    ans=sub1(no1=10,no2=11)
    print("Subtraction is : ",ans)


if __name__=="__main__":
    main()