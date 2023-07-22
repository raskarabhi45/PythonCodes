#Decorators in Python
# 6th nov 2022
#function within function is only possible in the python
#just a  simple code

def demo():
    print("Inside demo")

def hello():
    print("inside hello")
    demo()

hello()
demo()
