import pymysql
class ATMException(Exception):
    pass
def accountNumberGenerator(accNum):
    temp = int(accNum[3:])
    temp = temp + 1
    print(temp)
    if len(str(temp)) == 1:
        tempAccountNumber = "ATM00"+str(temp)
    elif len(str(temp)) == 2:
        tempAccountNumber = "ATM0" + str(temp)
    elif len(str(temp)) >= 3:
        tempAccountNumber = "ATM" + str(temp)
    return tempAccountNumber
def passwordVerifier(password):
    pswd = int(password)
    valid = True
    try:
        if len(str(pswd)) != 4:
            raise ATMException("Password should only contain 4 digits")
    except ATMException as e:
        print(str(e))
        valid = False
    except Exception as e:
        print(str(e))
        valid = False
    return valid
class Account:
    def __init__(self, accNum, pswd, acctype, intRate, NumOfTrans, balance = 100):
        self.accountNumber = accNum
        self.password = pswd
        self.accountBalance = balance
        self.accountType = acctype
        self.intersetRate = intRate
        self.numberOfTransactions = 0
        self.recievingAcountNumber = "ATM001"
        self.recieverAmount = 0
   
class Login:
    def __init__(self, Account1):
        self.Account = Account(Account1.accountNumber, Account1.password, Account1.accountType, Account1.interestrate, Account1.numberOfTransactions, Account1.accountBalance)
        self.loginStatus = False
        self.count = 0;
    def login(self, accNum, pswd):
        if self.count == 0:
            if self.Account.accountNumber == accNum:
                if self.Account.password == pswd:
                    self.count = self.count + 1
                    self.loginStatus = True
                else:
                    self.loginStatus = False
            else:
                self.loginStatus = False
    def checkBalance(self):
        if self.loginStatus == True:
            print(self.Account.accountBalance)
    def withdraw(self, bal):
        try:
            if bal > self.Account.accountBalance:
                raise ATMException("Amount to withdraw cannot be greater Account Balance ")
            elif bal < 0:
                raise Exception("Amount can not be negative ")
        except ATMException as e:
            print(str(e))
        except Exception as e:
            print(str(e))
            return
        withdraw = self.Account.accountBalance
        if self.loginStatus == True:
            if self.Account.accountType == "Basic Bank Account":
                if self.Account.numberOfTransactions <= 4:
                    self.Account.accountBalance = self.Account.accountBalance - bal
                    self.Account.numberOfTransactions = self.Account.numberOfTransactions + 1
                else:
                    self.Account.accountBalance = self.Account.accountBalance - (bal + 100)
                    self.Account.numberOfTransactions = self.Account.numberOfTransactions + 1
            elif self.Account.accountType == "Current Account":
                self.Account.accountBalance = self.Account.accountBalance - bal
                self.Account.numberOfTransactions = self.Account.numberOfTransactions + 1
            elif self.Account.accountType == "Saving Account":
                self.Account.accountBalance = self.Account.accountBalance - bal
                self.Account.numberOfTransactions = self.Account.numberOfTransactions + 1
                self.Account.intersetRate = self.Account.accountBalance * 0.04
            elif self.Account.accountType == "Fixed Deposit Account":
                self.Account.accountBalance = self.Account.accountBalance - bal
                self.Account.numberOfTransactions = self.Account.numberOfTransactions + 1
                self.Account.intersetRate = self.Account.accountBalance * 0.0824
        else:
            print("first creat account if you want to withdraw ")
    def deposit(self, bal):
        try:
            if bal < 0:
                raise Exception("amount to deposit can not be negative")
        except Exception as e:
            print(str(e))
            return
        deposit = self.Account.accountBalance
        if self.loginStatus == True:
            self.Account.accountBalance = deposit + bal
        else:
            print("First create an amount if you want to deposit ")
    def transferAmount(self, amount, accountNumber):
        if self.loginStatus == True:
            if self.Account.accountType == "Fixed Deposit Account":
                return
            elif self.Account.accountType == "Basic Bank Account":
                self.Account.accountBalance = self.Account.accountBalance - amount
                self.Account.numberOfTransactions = self.Account.numberOfTransactions + 1
                self.Account.recievingAcountNumber = accountNumber 
            elif self.Account.accountType == "Current Account":
                self.Account.accountBalance = self.Account.accountBalance - amount
                self.Account.numberOfTransactions = self.Account.numberOfTransactions + 1
                self.Account.recievingAcountNumber = accountNumber 
            elif self.Account.accountType == "Saving Account":
                self.Account.accountBalance = self.Account.accountBalance - amount
                self.Account.numberOfTransactions = self.Account.numberOfTransactions + 1
                self.Account.intersetRate = self.Account.accountBalance * 0.04
                self.Account.recievingAcountNumber = accountNumber 
        else:
            print("You have to creat amount in order to transfer amount")
            
def registerAccount():
    accountNumber = "ATM000"
    accountNumber = accountNumberGenerator(accountNumber)
    status = False
    while status == False:
        pswd = input("Enter the password for user")
        status = passwordVerifier(pswd)
    a1 = Account(accountNumber, pswd, "Current Account", 4.2, 0)

execution = True
while execution:
    print("Welcome to ATM service!!")
    print("1. to register as a user")
    print("2. to login")
    num = input("Enter choice")
    if num == 2:
        u1 = Login(a1)
        print("3. check balance")
        print("4. withdraw balance")
        print("5. deposit balance")
        print("6. Transfer amount")
        num = input("Enter operation of ATM")
        if num == 3:
            u1.checkBalance()
        elif num == 4:
            u1.withdraw(50)
        elif num == 5:
            u1.deposit(100)
        elif num == 6:
            recieverAcc = input("Enter reciever accountNumber ")
            u1.transferAmount(100, recieverAcc)
        else:
            execution = False
    elif num == 1:
        a1 = registerAccount()

