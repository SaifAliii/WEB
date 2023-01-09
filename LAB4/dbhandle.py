import pymysql
from Student import student
class dbHandle:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    def insertStudent(self, s1):
        mydb = None
        mycursor = None
        try:
            mydb = pymysql.connect(host = self.host, user = self.user, password = self.password, database=self.database)
            mycursor = mydb.cursor()
            query = "insert into ayeshadata values(%s, %s, %s, %s)"
            args = (s1.rollNo, s1.name, s1.semester, s1.cgpa)
            mycursor.execute(query, args)
        except Exception as e:
            print(str(e))
        finally:
            mydb.commit()
            if mycursor != None:
                mycursor = None
            if mydb != None:
                mydb = None
    def updateAddress(self, address):
        mydb = None
        myCursor = None
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            myCursor = mydb.cursor()
            query = "UPDATE ayeshadata set address = %s where id = 2"
            args = (address)
            myCursor.execute(query, args)
        except Exception as e:
            print(str(e))
        finally:
            mydb.commit()
            if myCursor != None:
                myCursor = None
            if mydb != None:
                mydb = None
    def deleteColumn(self, phoneNum):
        mydb = None
        mycursor = None
        try:
            mydb = pymysql.connect(host = self.host, user = self.user, password = self.password, database=self.database)
            mycursor = mydb.cursor()
            query = "alter table ayeshadata drop column address"
            args = (phoneNum)
            mycursor.execute(query)
        except Exception as e:
            print(str(e))
        finally:
            if mycursor != None:
                mycursor = None
            if mydb != None:
                mydb = None
    def displayStudent(self):
        mydb = None
        mycursor = None
        try:
            mydb = pymysql.connect(host = self.host, user = self.user, password = self.password, database=self.database)
            mycursor = mydb.cursor()
            query = "select * from ayeshadata"
            mycursor.execute(query)
            print(mycursor.fetchall())
        except Exception as e:
            print(str(e))
        finally:
            if mycursor != None:
                mycursor = None
            if mydb != None:
                mydb = None
db = dbHandle("localhost", "root", "sunnyiam1()X", "ayeshabase")
s1 = student(2, "ayesha", "Wapda towsn", "03407409504")
db.displayStudent()
db.insertStudent(s1)
db.updateAddress("wapda town lahore")
db.deleteColumn("phone num")
db.displayStudent()