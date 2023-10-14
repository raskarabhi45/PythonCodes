#Multitasking 
#Parallel programming
import multiprocessing

def main():
    print("Numbers of cores are : ",multiprocessing.cpu_count())  # 8 cores


if __name__=="__main__":
    main()
