# function parameters in python
"""
# 1 Positional Arguments 
def add1(no1,no2):
    print("Value of no1 : ",no1)
    print("Value of no2 : ",no2)
    return no1+no2

# 2 keyword arguments
def sub1(no1,no2):
    print("Value of no1 : ",no1)
    print("Value of no2 : ",no2)
    return no1-no2
"""
# 3 Default arguments
def Area(Radius,PI=3.14):
    result=PI*Radius*Radius
    return result

def main():
    RValue=10.5
    PIValue=3.14

    #positional argument
    ans=Area(RValue,PIValue)  # ans=Area(10.5,3.14) 
    print("Area of circle is : ",ans)
    
    #keyward argument
    ans=Area(PI=PIValue,Radius=RValue)  #ans=Area(3.14,10.5)
    print("Area of circle is : ",ans)

    #positional argument and second is default
    ans=Area(10.5)     #positional argument  ans=Area(10.5)
    print("Area of circle is : ",ans)

    #keyward argument and second is default
    ans=Area(Radius=10.5)              # ans=Area(10.5)
    print("Area of circle is : ",ans)

    #keyward argument
    ans=Area(PI=7.10,Radius=10.5)  #default argemnt with keyward
    print("Area of circle is : ",ans)
  
  


if __name__=="__main__":
    main()