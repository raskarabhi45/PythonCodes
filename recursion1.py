import sys
print(sys.getrecursionlimit()) #number of stack frames 1000 for recursion call

sys.setrecursionlimit(3001)
print(sys.getrecursionlimit())



def displayR(no):
    if(no>0):
        print("hello")
        no=no-1
        displayR(no)  # recursive function call

displayR(4) # normal function call

