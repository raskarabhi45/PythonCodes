from sys import *
#  input from cmd as python addition_command.py 12 12
def Addition(a,b):
    ans=0
    ans=a+b
    return ans

def main(): 
    #this is validation
    if(len(argv)!=3):
        print("Invalid number of argument ")
        exit()

    ret=Addition(int(argv[1]),int(argv[2]))   #here we typecast string to int
    print("Addition is : ",ret)


if __name__=="__main__":
    main()
