#check whether number is even or odd
def CheckEven(no):
    if(no%2==0):
        return True
    else:
        return False


def CheckEvenX(no):
    return(no%2==0)

even=lambda no:no%2==0

ret=CheckEvenX(15)
ret1=even(11)

if(ret1==True):
    print("Its Even")
else:
    print("Its Odd")
