# Parallel Programming
# Full utilization of all cores 
# fastest execuetion  in parallel programming
# platform dependent
# 5 cores active here 

import os
import multiprocessing
import time

def Square(no):
    print("PID of worker process is {} for the input {}".format(os.getpid(),no))
    return (no*no)

def main():
    print("Process ID of our application is : ",os.getpid())
    data=[1,2,3,4,5]
    result=[]

    pobj=multiprocessing.Pool()  # Pool is like panychi Taki

    result=pobj.map(Square,data) #(kay kam , Konavr kraychy)

    print("Result after operation is : ",result)
    


if __name__=="__main__":
    start_time=time.process_time()
    main()
    end_time=time.process_time()

    print("Execution time is : ",end_time-start_time)