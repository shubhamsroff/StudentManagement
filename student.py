import mysql.connector

# Establish connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="student2",
    auth_plugin='mysql_native_password'
)

# Create cursor object
conn = mydb.cursor()

def main():
    print("#"*30)
    print("#"*5 + "Crud Operations:-")
    print("""
            1. Register
            2. Login
            3. Exit
    """)
    choice = input("Choose an option 1/2/3 to process: ")
    print(choice)
    if choice == '1':
        register()
    elif choice == '5':
        login()
    elif choice == '6':
        exitt()    
    else:
        print("Please enter coorect option")
        main()

def register():
    name = input("Enter Your Name: ")
    enrollment = input("Enter Your Enrollment: ")
    college = input("Enter Your College Name: ")
    password = input("Enter  Password: ")
    contact = input("Enter Your Contact Number: ")
    data = (name,enrollment,college,password,contact)
    sql = "insert into student (name, enrollment, college, password, contact) values(%s,%s,%s,%s,%s)"

    conn.execute(sql,data)
    mydb.commit()
    print("You Want to login: Y/N-")
    choice2=input("Enter your choice")
    if choice2[0]=='Y':
             login()
    
    else:
        exit()
    
   
   


def showProfile(data,log):
    if log:
        conn.execute("SELECT * FROM student where enrollment= %s" ,(username,))
        studentData = conn.fetchone()
        
        print(studentData)    

def updateProfile(data,log):
      if log: 
            name=input("Enter Your Name:-")
            contact=input("Enter Your Contact Number:-")
            sql = "UPDATE student SET name = %s, contact = %s WHERE enrollment = %s"
            val = (name, contact, username)
            conn.execute(sql, val)
            mydb.commit()
            print("Student record updated successfully.")  

def deleteProfile(data,log):
    if log:
        mycursor = mydb.cursor()
        sql = "DELETE FROM student WHERE enrollment = %s"
        val = (username,)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Student record deleted successfully.")

def exitt():
    print("Thanks foer visiting!!!")
    exit() 
           

from mysql.connector import Error

def login():
    global username
    global logged_in
    uname = input("Enter username: ")
    conn.execute('select * from student where enrollment = %s',(uname,))
    data = conn.fetchone() 
    
    if data is not None:
        try:
            pass
        except:
            pass
        pwd = input("Enter password: ")
        if data[3] == pwd:
            print(f"Welcome {data[0]}")
            username = uname
            logged_in = True
        else:
            print("Wrong password!!!")
    else:
        print("Wrong Username or you didn't registered with us!!!")
        ch = input("do you want to register!!! y/n")
        if ch=='y' or ch == 'Y':
            register()
        else:
            login()

    print("""
        Choose 1 for Show Your Profile
        Choose 2 for Update Your Profile
        Choose 3 for Delete Profile
        Choose 4 for Exit
    """)
    ch = input("Enter your choice: ")
    
    if ch == '1':
        showProfile(data,logged_in)
    elif ch == '2':
        updateProfile(data,logged_in)
    elif ch == '3':
        deleteProfile(data,logged_in) 
        register()   
    else:
        exitt()


      


if __name__ == "__main__":
    main()

