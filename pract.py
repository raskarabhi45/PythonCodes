from sys import *

def Addition(a,b):
    ans=0
    ans=a+b
    return ans

def main(): 
    #this is validation
    if(len(argv)!=3):
        print("Invalid number of argument ")
        exit()

    ret=Addition(int(argv[1]),int(argv[2]))
    print("Addition is : ",ret)


if __name__=="__main__":
    main()