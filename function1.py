#fundamental of functions in Python
"""
inside Demo1
Inside Demo2 with argument :  11
Inside Demo3 with argument  10
Return value of Demo3 is :  12
Inside Demo4
Return value is :  21
Inside Demo5
First written value  21
second written value :  1
"""
# 1 function which accept nothing and returns nothing
def Demo1():
    print("inside Demo1")

# 2 function accept one parameter and returns nothing
def Demo2(no):
    print("Inside Demo2 with argument : ",no)

# 3 function which accept one parameter and return one parameter 
def Demo3(no):
    print("Inside Demo3 with argument ",no)
    return no+2

# 4 function accept two parameter and return one parameter
def Demo4(no1,no2):
    print("Inside Demo4")
    add=no1+no2
    return add

# 5 function accept two parameter and return two parameter
def Demo5(no1,no2):
    print("Inside Demo5")
    add=no1+no2
    sub=no1-no2
    return add,sub

def main():
    Demo1()
    Demo2(11)
    ans=Demo3(10)
    print("Return value of Demo3 is : ",ans)
    ans=Demo4(10,11)
    print("Return value is : ",ans)

    ans1,ans2=Demo5(11,10)
    print("First written value ",ans1)
    print("second written value : ",ans2)



if __name__=="__main__":
    main()