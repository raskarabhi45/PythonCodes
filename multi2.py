# # execution time of Application
import time

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
    displayEven(1000)
    displayOdd(1000)


if __name__=="__main__":
    start_time=time.time()
    main()
    end_time=time.time();

    print("Execution time is : ",end_time-start_time)