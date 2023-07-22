#function inside function and return value of inner function
"""
inside outer
inside inner
"""

def outer(): # 100
    print("inside outer")

    def inner():     # 100 
        print("inside inner")

    return inner  #300

    
ret=outer()   # ret=100()
print(type(ret))
print(id(ret))
ret()  #200

