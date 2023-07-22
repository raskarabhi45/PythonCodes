def display(no):
    while(no>0):
        print(no)
        no=no-1

def displayR(no):  # from 4 to one
    if(no>0):
        print(no)
        no=no-1
        displayR(no)  #tail recursionN
"""
def displayR(no):
    if(no>0):
        print(no)
        displayR(no-1)
        """
def displayRX(no):  # from 1 to 4  backtracking  
    if(no>0):
        no=no-1
        displayR(no) #head recursion
        print(no)

displayR(4)      

#display(4)