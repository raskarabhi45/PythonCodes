#Banking Application in OOP
#instance variable : Name,Amount,Address,AccountNo
#Instance method : CreateAccount() ,DisplayAccountInfo()

#class variable : Bank_Name,ROI_On_FD
#class method : DisplayBankInformation()

#Static method : DisplayKYCInfo()

class Bank_Account:
    Bank_Name="HDFC Bank PVT LTD"
    ROI_On_FD=6.7    #rate of interest on fixed deposit

    def __init__(self):
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


    def DisplayAccountInfo(self):  #self
        print("------------------------------------------------------------------")
        print("--------Your Account Information is as below --------")
        print("------------------------------------------------------------------")   
        print("Account Number            : ",self.AccountNo)
        print("Name of Account Holder    : ",self.Name)
        print("Address of Account Holder : ",self.Address)
        print("Current Amount in Account : ",self.Amount)

    @classmethod      #decorator   @classmethod and  @staticmethod  
    def DisplayBankInformation(cls):  #cls
        print("Welcome to Banking Console ")
        print("Name of our bank is : ",cls.Bank_Name)
        print("Rate of interest we offer on fixed deposite is : ",cls.ROI_On_FD)

    @staticmethod   #@staticmethod
    def DisplayKYCInfo():
        print("Please consider below KYC Information")
        print("According to the rules of government of India you have to submit below documents")
        print("1 : clear and recent passport size photo")
        print("2 : Photo of Aadhar card")
        print("3 : Photo of PAN card")

    def Deposit(self,value):
        self.Amount=self.Amount+value

    def Withdraw(self,value):
        self.Amount=self.Amount-value



def main():
    print("------------------------------------------------------------------")
    print("--------------Banking Application-----------------")
    print("------------------------------------------------------------------")

    print("------------------------------------------------------------------")
    print("-----------Calling Static Method to Display KYC info----------------")
    print("------------------------------------------------------------------")
    Bank_Account.DisplayKYCInfo()

    print("------------------------------------------------------------------")
    print("---------Accessing class variables from main---------------")
    print("------------------------------------------------------------------")
    print("Name of Bank : ",Bank_Account.Bank_Name)
    print("Rate of interest on fixed deposit : ",Bank_Account.ROI_On_FD)
    
    print("------------------------------------------------------------------")
    print("----------Calling the class method to display bank information -----------")
    print("------------------------------------------------------------------") 
    Bank_Account.DisplayBankInformation()

    print("------------------------------------------------------------------")
    print("----------Creating the object of class -----------")
    print("------------------------------------------------------------------") 
    User1=Bank_Account()
    User2=Bank_Account()

    print("Creating the first account")
    print("----------Enter the details for first account holder ------------")
    User1.CreateAccount()
    print("Creating the second account")
    print("----------Enter the details for second account holder -----------")
    User2.CreateAccount()

    print("------------------------------------------------------------------")
    print("----------Calling instance method to display information of first account -----------")
    print("------------------------------------------------------------------")    
    User1.DisplayAccountInfo()
    print("------------------------------------------------------------------")
    print("----------Calling instance method to display information of Second account -----------")
    print("------------------------------------------------------------------")   
    User2.DisplayAccountInfo()
    print("---------Depositing 500 in user1----------")
    User1.Deposit(500)
    print("---------Depositing 1200 in user1----------")
    User2.Deposit(1200)

    print("Amount of {} after deposit is {} : ".format(User1.Name,User1.Amount))
    print("Amount of {} after deposit is {} : ".format(User2.Name,User2.Amount))
    
    print("---------Withdraw 200 from user1----------")
    User1.Withdraw(200)
    print("---------Withdraw 3000 from user1----------")
    User2.Withdraw(3000)

    print("Amount of {} after deposit is {} : ".format(User1.Name,User1.Amount))
    print("Amount of {} after deposit is {} : ".format(User2.Name,User2.Amount))
    print("------------------------------------------------------------------")
    print("--------------End of Banking Application--------------")
    print("------------------------------------------------------------------")

if __name__=="__main__":
    main()

"""
Rate of interest we offer on fixed deposite is :  6.7
------------------------------------------------------------------
----------Creating the object of class -----------
------------------------------------------------------------------
Creating the first account
----------Enter the details for first account holder -----------
Enter your name :
Abhishek
Enter your initial amount : 
12000
Enter your Address
Pune
Enter your account number : 
12345
Creating the second account
----------Enter the details for second account holder -----------
Enter your name : 
Prasad  
Enter your initial amount : 
10000
Enter your Address
Satara
Enter your account number : 
23451
------------------------------------------------------------------
----------Calling instance method to display information of first account -----------
------------------------------------------------------------------
------------------------------------------------------------------
--------Your Account Information is as below --------
------------------------------------------------------------------
Account Number :  12345
Name of Account Holder :  Abhishek
Address of Account Holder :  Pune
Current Amount in Account :  12000
------------------------------------------------------------------
----------Calling instance method to display information of Second account -----------
------------------------------------------------------------------
------------------------------------------------------------------
--------Your Account Information is as below --------
------------------------------------------------------------------
Account Number :  23451
Name of Account Holder :  Prasad
Address of Account Holder :  Satara
Current Amount in Account :  10000
---------Depositing 500 in user1----------
---------Depositing 1200 in user1----------
Amount of Abhishek after deposit is 12500 :
Amount of Prasad after deposit is 11200 :
---------Withdraw 200 from user1----------
---------Withdraw 3000 from user1----------
Amount of Abhishek after deposit is 12300 :
Amount of Prasad after deposit is 8200 :
------------------------------------------------------------------
--------------End of Banking Application--------------
------------------------------------------------------------------"""