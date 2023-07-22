
def add(A,B):
    return A+B

def sub(A,B):
    return A-B


def calculator(target,value1,value2):
    return target(value1,value2)

ret=calculator(target=add,value1=10,value2=11)
print("Addition is : ",ret)

ret=calculator(target=sub,value1=10,value2=11)
print("Subtraction is : ",ret)
