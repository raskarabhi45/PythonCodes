#with the better complexity and less number of iterations

def fact(no):
    for i in range(1,int((no/2))+1):
        if(no%i==0):
            print(i)
        #i=i+1 when we  use for loop without the range function
        

def main():
    print("Enter number to find factors : ")
    no=int(input())

    print("Factors are :")

    fact(no)


if __name__=="__main__":
    main()