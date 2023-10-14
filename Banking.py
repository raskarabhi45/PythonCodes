#Banking Application in OOP
#instance variable : Name,Amount,Address,AccountNo
#Instance method   : CreateAccount() ,DisplayAccountInfo() 

# output of this code 
"""
--------Your Account Information is as below --------

Account Number            :  12465
Name of Account Holder    :  Abhishek
Address of Account Holder :  Pune
Current Amount in Account :  10000

--------Your Account Information is as below --------

Account Number            :  12543
Name of Account Holder    :  Rohit
Address of Account Holder :  Natepute
Current Amount in Account :  1200

"""

class Bank_Account:
    #here self is like this keyword
    def __init__(self):  #obously all instance variable are intialized in constructor  def __init__(self):
        self.Name=""
        self.Amount=0
        self.Address=""
        self.AccountNo=0

    def CreateAccount(self):

        print("Enter your name : ")
        self.Name=input()

        print("Enter your initial amount : ")
        self.Amount=int(input())

        print("Enter your Address")
        self.Address=input()

        print("Enter your account number : ")
        self.AccountNo=int(input())


    def DisplayAccountInfo(self):
        print()
        print("--------Your Account Information is as below --------")
        print()
        print("Account Number            : ",self.AccountNo)
        print("Name of Account Holder    : ",self.Name)
        print("Address of Account Holder : ",self.Address)
        print("Current Amount in Account : ",self.Amount)
       


def main():
    User1=Bank_Account()  #in java and c++ Bank_Account obj=new Bank_Account()
    User2=Bank_Account()

    User1.CreateAccount()
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

if __name__=="__main__":
    main()

