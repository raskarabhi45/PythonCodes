
        #i=i+1 when we  use for loop without the range function
        
#import Numbers
#from Numbers import fact
#from numbers import *
import Numbers as NUM               #(nickname)

def main():
    print("Enter number to find factors : ")
    no=int(input())

    print("Factors are :")

    #Numbers.fact(no)
    NUM.fact(no)


if __name__=="__main__":
    main()