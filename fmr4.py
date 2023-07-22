#filter()  map()  and reduce()  in python
from functools import reduce

CheckEven=lambda no: (no%2==0)

Doubles=lambda no:  no*2

Sum=lambda A,B:  A+B



def main():
    print("Enter number of elements you want to enter : ")
    iSize=int(input())

    Data_Input=[] 
    print("Please enter the data")                                    
    for i in range(0,iSize,1):
        Value=int(input())
        Data_Input.append(Value)
    print("Data is : ",Data_Input)

    Data_Filter=list(filter(CheckEven,Data_Input))
    print("Data after filter : ",Data_Filter)

    Data_Map=list(map(Doubles,Data_Filter))
    print("Data after map is : ",Data_Map)

    Output=reduce(Sum,Data_Map)
    print("Data after reduce : ",Output)


if __name__=="__main__":
    main()