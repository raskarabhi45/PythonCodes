#command line argument in python
#python command1.py 12 Hello 21

#  python command1.py hello jiii kaisehoApp
# Total number of argument :  4
# Name of application :  command1.py
# first argument :  hello
# second argument :  jiii
# third argument :  kaisehoApp
from sys import *

def main():
    print("Total number of argument : ",len(argv))
    print("Name of application : ",argv[0])

    print("first argument : ",argv[1])
    print("second argument : ",argv[2])
    print("third argument : ",argv[3])



if __name__=="__main__":
    main()
