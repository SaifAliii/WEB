accNum = "ATM000"

def registerAccount(accountNumber, accountBalance = 100):
    temp = int(accountNumber[3:])
    temp = temp + 1
    print(temp)
    if len(str(temp)) == 1:
        tempAccountNumber = "ATM00"+str(temp)
    elif len(str(temp)) == 2:
        tempAccountNumber = "ATM0" + str(temp)
    elif len(str(temp)) >= 3:
        tempAccountNumber = "ATM" + str(temp)
    accNum = tempAccountNumber
    flag = True
    while flag == True:
        try:
            password = input("Enter password: ")
            pswd = int(password)
            if len(str(pswd)) != 4:
                raise InvalidLength("Password should only contain 4 digits")
                flag = True
            else:
                flag = False
        except InvalidLength as e:
            print("Again take Password ")
            print(str(e))
        except Exception as e:
            print("Password should only contain numbers now again take password ")
            print(str(e))
    if int(accountBalance) < 0:
        raise NegativeAmount("Balanace cannot be negative")
    with open("atmData.txt", "a") as f:
        f.write(str(tempAccountNumber))
        f.write(",")
        f.write(str(pswd))
        f.write(",")
        f.write(str(accountBalance))
        f.write("\n")

def Login():
    flag = True
    listdata = []
    i = 0
    while flag == True:
        try:
            aNum = input("Enter Account number: ")
            with open("atmData.txt", "r+") as f:
                f.seek(0)
                for filedataRecord in f.readlines():
                    listdata.append(filedataRecord)
                    listfiledata = filedataRecord.split(",")
                    filedata = listfiledata[0]
                    print(aNum)
                    print(filedata)
                    if aNum == filedata:
                        pswd = input("Enter Password: ")
                        filedatapass = listfiledata[1]
                        if pswd == filedatapass:
                            print("Login succesfully ")
                            #Check Balance
                            print(listfiledata[2])
                            flag1 = True
                            while flag1 == True:
                                try:
                                    amount = print("Enter Amount to widthDarw")
                                    if amount < 0:
                                        raise InsufficientBalance("Balance is negative")
                                    elif amount > listfiledata[2]:
                                        raise InsufficientBalance("amount can not exceed from balance")
                                    else:
                                        listdata[i] = {aNum+",", pswd+",", listfiledata[2] - amount}
                                        flag = False
                                except InsufficientBalance as e:
                                    print(str(e))
                        else:
                            raise InvalidPin("Please Enter Correct Pin")
                        flag = False
                    else:
                        raise UserDoesNotExist("User does not exist")
        except UserDoesNotExist as e:
            print(str(e))
        except InvalidPin as e:
            print(str(e))
        i = i + 1


try:
    registerAccount(accNum)
except NegativeAmount as e:
    print(str(e))
