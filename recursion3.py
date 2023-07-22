"""
Enter number
10
55
55
"""
def display(no):
    sum=0
    while(no>0):
        sum=sum+no
        no=no-1
    return sum


def displayR(no):
    if(no<=0):
       return 0
    else:
        return(no+displayR(no-1))

def fact(no):
    if(no<=0):
       return 1
    else:
        return(no*fact(no-1))




def main():
    print("Enter number")
    no=int(input())
    ret=display(no)
    print(ret)
    ret=displayR(no)
    print(ret)
    ret=fact(no)
    print(ret)


if __name__=="__main__":
    main()
