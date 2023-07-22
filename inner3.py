#Decorators in Python
"""
inside hello
Inside demo
inside hello
Inside fun
"""

def demo():    
        print("Inside demo")

def fun():
    print("Inside fun")

def hello(FPTR):
    print("inside hello")
    FPTR()


hello(demo)
hello(fun)
#hello(11) error

