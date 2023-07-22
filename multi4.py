#multiprocessing
# ethe 3 process run zalya ek ya application chi and 2 ya 2 method sathi
import multiprocessing
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
    # parallel Programming in java
    print("Demonstartion of Parallel programming using multiple process")
    number=2000

    p1=multiprocessing.Process(target=displayEven,args=(number,))
    p2=multiprocessing.Process(target=displayOdd,args=(number,))

    p1.start()
    p2.start()
    # without join method is like  mall la n jata prt magari 
    p1.join()
    p2.join()

    print("End of main")


if __name__=="__main__":
    
    start_time=time.process_time()
    main()
    end_time=time.process_time();

    print("Execution time is : ",end_time-start_time)