#recursion in python
#function will display 4 times hello on screen by recursion

def display(no):
    cnt=0
    while(cnt<no):
        print("Hello")
        cnt=cnt+1

def displayR(no):
    cnt=0
    if(cnt<no):
        print("hello")
        cnt=cnt+1
        displayR(no)

#display(4)
displayR(4)
