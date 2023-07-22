#Decorators in Python
# 6th nov 2022
#function within function is only possible in the python
#just a  simple code
#This is the example of inner function
#functions are first class objects in python
#powerful function inner function

def hello():
    print("inside hello")

    def demo():    #this function cannot be called from outside function
        print("Inside demo")

    demo()

hello()
# demo() and hello.demo() not possible


