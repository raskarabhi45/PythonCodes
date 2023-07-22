#with the better complexity and less number of iterations

def fact(no):
    i=1
    while(i<=no):
        if(no%i==0):
            print(i)
        i=i+1 
        
        

def main():
    print("Enter number to find factors : ")
    no=int(input())

    print("Factors are :")

    fact(no)


if __name__=="__main__":
    main()
    
