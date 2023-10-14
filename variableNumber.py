# 4 th type of argument
# 4 variable number of argument
# need to study it again more carefully
#    * operator 
def Add(*values):
    print(type(values))  #tuple
    print("Number of arguments are : ",len(values))
    
    sum=0
    for no in values:     #for each loop
        sum=sum+no

    return sum


def AddX(*values):
    print(type(values))  #tuple
    print("Number of arguments are : ",len(values))
    
    sum=0
    for i in range(0,len(values),1):
        sum=sum+values[i]

    return sum

def main():
    ans=Add(1,7,9,4,6,5)
    print("Addition is : ",ans)

  
if __name__=="__main__":
    main()

    