#something gets wrong
#multithreading
#in case of multithreading and multiprocessing we cant get return value from another  function bt there is solution create global variable
#direct function and call back function
#Check it 
import threading
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
    print("Demonstartion of Parallel programming using multiple threads")
    number=2000

    p1=threading.Thread(target=displayEven,args=(number,))
    p2=threading.Thread(target=displayOdd,args=(number,))

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