#Application to find out maximum number

def Max(no1,no2):
    if(no1>no2):
        return no1
    else:
        return no2



def main():
    print("Enter first number\n")
    no1=int(input())

    print("Enter second number\n")
    no2=int(input())
    max=Max(no1,no2)
    
    print("Maximum number is : ",max)


    
if __name__=="__main__":
    main()