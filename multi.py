# Multiprocessing in python

def displayEven(no):
    for i in range(1,no,1):
        if(i%2==0):
            print("Even number : ",i)


def displayOdd(no):
    for i in range(1,no,1):
        if(i%2!=0):
            print("Odd number  : ",i)



def main():
    print("Demonstartion of serial programming")
    displayEven(2000)
    displayOdd(2000)


if __name__=="__main__":
    main()
