#POP Approach in python
def Add(A,B):
    return A+B

def Sub(A,B):
    return A-B

def main():
    print("Enter first number")
    no1=int(input())

    print("Enter second number")
    no2=int(input())

    Ans=Add(no1,no2)
    print("Addition is : ",Ans)

    Ans=Sub(no1,no2)
    print("Subtraction is : ",Ans)


if __name__=="__main__":
    main()