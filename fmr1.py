#filter() map() and reduce() functions
"""
Original data :  [2, 3, 1, 6, 4, 5, 11, 16, 20]   bhaji chi pishvi
Data after filter :  [2, 6, 4, 16, 20]       Nivadleli Bhaji
Data after map :  [4, 8, 6, 18, 22]         process keleli bhaji
Data after reduce :  58       noodle chi wati
"""

def CheckEven(no):
    return(no%2==0)


def Increment(no):
    return no+2

def filterX(arr,function_name):
    result=[]
    for no in arr:
        if(function_name(no)):
            result.append(no)
    return result

def mapX(arr,function_name):  #cut keleli bhaji
    result=[]
    for no in arr:
        value=function_name(no)
        result.append(value)
    return result

def reduceX(arr):
    sum=0
    for no in arr:
        sum=sum+no

    return sum





def main():
    data=[2,3,1,6,4,5,11,16,20]  #Bhaji pishavi

    print("Original data : ",data)

    data_filter=list(filterX(data,CheckEven))

    print("Data after filter : ",data_filter)

    data_map=list(mapX(data_filter,Increment))
    print("Data after map : ",data_map)

    ret=reduceX(data_map)
    print("Data after reduce : ",ret)


if __name__=="__main__":
    main()