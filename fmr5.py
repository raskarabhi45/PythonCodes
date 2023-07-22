#filter()  map()  and  reduce() in python
from functools import reduce

def main():
    print("Enter number of elements you want to enter : ")
    iSize=int(input())

    Data_Input=[]
    print("Please enter the data")
    for i in range(0,iSize,1):
        Value=int(input())
        Data_Input.append(Value)
    print("Data is : ",Data_Input)

    Data_Filter=list(filter(lambda no: (no%2==0),Data_Input))
    print("Data after filter : ",Data_Filter)

    Data_Map=list(map(lambda no:  no*2,Data_Filter))
    print("Data after map is : ",Data_Map)

    Output=reduce(lambda A,B:  A+B,Data_Map)
    print("Data after reduce : ",Output)
    
if __name__=="__main__":
    main()