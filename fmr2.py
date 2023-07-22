#filter()  map()  and reduce()  in python
def CheckEven(no):
    return (no%2==0)

def Doubles(no):
    return no*2

def Sum(A,B):
    return A+B

def reduceX(Helper_Function,Data):
    Ans=0
    for no in Data:
        Ans=Helper_Function(Ans,no)
    
    return Ans

def filterX(Helper_Function,Data):
    Result=[]
    for no in Data:
        if(Helper_Function(no)==True):
            Result.append(no)

    return Result

def mapX(Helper_Function,Data):
    Result=[]
    for no in Data:
        Value=Helper_Function(no)
        Result.append(Value)

    return Result


def main():
    print("Enter number of elements you want to enter : ")
    iSize=int(input())

    Data_Input=[]
    print("Please enter the data")
    for i in range(0,iSize,1):
        Value=int(input())
        Data_Input.append(Value)
    print("Data is : ",Data_Input)

    Data_Filter=filterX(CheckEven,Data_Input)
    print("Data after filter : ",Data_Filter)

    Data_Map=mapX(Doubles,Data_Filter)
    print("Data after map is : ",Data_Map)

    Output=reduceX(Sum,Data_Map)
    print("Data after reduce : ",Output)


if __name__=="__main__":
    main()