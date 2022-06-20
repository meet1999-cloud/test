# from secrets import choice
import mysql.connector as connector
class DBHelper:
    def __init__(self):
        self.con=connector.connect(host="192.168.29.208",
                                    user="monty",
                                    password="some_pass",
                                    database="test")
        query='create table if not exists user(userId int primary key, userName varchar(200), phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("Database is created")



    def insert_user(self,userid,username,phone):
        query="insert into user (userId,userName,phone) values({},'{}',{})".format(userid, username, phone)
        print(query)
        my_var = self.con.cursor()
        my_var.execute(query)
        self.con.commit()
        print("Inserting into database")

    def fetch_all1(self):
        query="select * from user"
        my_var1 = self.con.cursor()
        my_var1.execute(query)
        for row in my_var1:
            print("user id :",row[0])
            print("user name :",row[1])
            print("user phone :",row[2])

    def delete_user(self,userId):
        query="delete from user where userId={}".format(userId)
        print(query)
        cur_1 = self.con.cursor()
        cur_1.execute(query)
        self.con.commit()
        print("deleted")

    def update_user(self,userId, newName, newPhone):   
        query="update user set userName='{}', Phone='{}' where userId={}".format(newName,newPhone,userId)
        print(query)
        my_len = self.con.cursor()
        my_len.execute(query)
        self.con.commit()
        print("Your data will be updated in some time")

    def myfunction(self):
        print()
        print("*****Welcome to DataBase*****")
        print("Please select 1 to insert data")
        print("Please select 2 to fetch data")
        print("Please select 3 to delete data")
        print("Please select 4 to update data")
        print("Please select 5 to exit from database")
        print()
        choice = int(input())
        
        if choice==1:
            uid=int(input("Enter a userid : "))
            username=input("Enter a username : ")
            phone=input("Enter a phonenumber : ")
            self.insert_user(uid,username,phone)

        elif choice==2:
            self.fetch_all1()

        elif choice==3:
             uid=int(input("Enter a userid you want to delete  : "))
            #  username=input("Enter a username : ")
             self.delete_user(uid)

        elif choice==4:
            uid=int(input("Enter a userid : "))
            username=input("Enter a username : ")
            phone=input("Enter a phonenumber : ")
            self.update_user(uid,username,phone)

        elif choice==5:
            print("You cannot upload any database here")
        
        else:
            exit()
            

x = DBHelper()  
x.myfunction()                              


    
        

