"""
PID of current process :  12248   for this process
PID of parent process :  24552   #this one is cmd PID  this same
"""
import os

def main():
    print("PID of current process : ",os.getpid()) 
    print("PID of parent process  : ",os.getppid())


if __name__=="__main__":
    main()

