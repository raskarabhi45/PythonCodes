
# execution time of process
#best method
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
    displayEven(2000)
    displayOdd(2000)


if __name__=="__main__":
    start_time=time.process_time()
    main()
    end_time=time.process_time();

    print("Execution time is : ",end_time-start_time)