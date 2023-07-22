
# Normal functions / Named Functions
# def function_name(function_parameters):
#    function_body

def Add(no1,no2):
    return no1+no2

#anonymous function the function without name
#Lambda functions / Unnamed function
#lambda parameters : body

#it works like inline function in c++
addfunction=lambda A,B: A+B

ans1=Add(10,11)
ans2=addfunction(10,11)

print("Addition using normal function : ",ans1)
print("Addition using lambda function : ",ans2)

print("type of lambda function is ",type(addfunction))


