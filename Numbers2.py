#problemns on n numbers
from os import access


class Numbers:
    def __init__(self):
        self.arr=list()
        self.size=0

    def Accept(self):
        print("Enter how many elements you want to store ")
        self.size=int(input())

        print("Enter the elements")
        value=0
        for i in range(0,self.size):
            value=int(input())
            self.arr.append(value)

    def Display(self):
        print("Elements from the list")
        for i in range(0,self.size):
            print(self.arr[i])

    def Summation(self):
        sum=0
        for i in range(0,self.size):
            sum=sum+self.arr[i]

        return sum


    def Average(self):
        sum=0
        for i in range(0,self.size):
            sum=sum+self.arr[i]

        return (sum/self.size)

    def Min(self):
        min=self.arr[0]
        for i in range(0,self.size):
            if(self.arr[i]>min):
                min=self.arr[i]

        return min

    def Max(self):
        max=self.arr[0]
        for i in range(0,self.size):
            if(self.arr[i]<max):
                max=self.arr[i]

        return max




def main():
    obj=Numbers()
    obj.Accept()
    obj.Display()

    ans=obj.Summation()
    print("Summation is ",ans)

    ans=obj.Average()
    print("Average value  is ",ans)

    ans=obj.Max()
    print("Max value  is ",ans)

    ans=obj.Min()
    print("min value  is ",ans)
   



if __name__=="__main__":
    main()