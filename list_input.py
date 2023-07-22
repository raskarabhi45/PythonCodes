
from sys import api_version

def main():
    #object of list class
    arr=list()  #empty list in python
    print("Enter how many elements you want to store")
    size=int(input())
    
    print("Please enter the values")
     
    for i in range(0,size):
        no=int(input())
        arr.append(no)  #arr.insert(i,no)

    print(arr)

if __name__=="__main__":
    main()
