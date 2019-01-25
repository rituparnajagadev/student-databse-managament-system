import pymysql.cursors

def start():
    print("1.new student")
    print("2.student")
    print("3.search student")
    print("4.remove student")
    x = int(input("please select your option:\t"))
    if x== 1:
        newStudent()
    elif x== 2:
        viewStudents()
    elif x== 3:
        searchStudent()
    elif x== 4:
        removeStudent()
    else:
        print("\tTry Again")
    return

def newStudent():
    # Connect to the database
    connection = pymysql.connect(host='127.0.0.1', user='root', password='onsi', db='projects', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    print("\tnew student")
    try:
        with connection.cursor() as cursor:
            # insert a student
            name=input("enter name: ")
            roll=input("enter roll: ")
            stream=input("enter stream: ")
            gender=input("enter gender:")
            mobileNumber = input("Enter mobile number : ")
            sql = "INSERT INTO  studentinformation values(null,'" + name + "'," + roll + ",'" + stream + "','" + gender + "'," + mobileNumber + ")"
            print(sql)
            cursor.execute(sql)
            connection.commit()
            # result = cursor.rowcount()
            # print(result,"row inserted")
    finally:
        connection.close()
        print("\nNew student task completed\n")
    return

def viewStudents():
    # Connect to the database
    connection = pymysql.connect(host='127.0.0.1', user='root', password='onsi', db='projects', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    print("\tview student")
    try:
        with connection.cursor() as cursor:
            # Read a all record
            sql = "SELECT * FROM projects.studentinformation"
            cursor.execute(sql)
            result = cursor.fetchall()
            connection.commit()
            print(result)
    finally:
        connection.close()
    print("\nview student task completed\n")
    return

def searchStudent():
    # Connect to the database
    connection = pymysql.connect(host='127.0.0.1', user='root', password='onsi', db='projects', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    print("\tsearch student")
    try:
        with connection.cursor() as cursor:
            # Read a single record
            myroll = input("Enter Roll no. : ")
            sql = "SELECT * FROM projects.studentinformation WHERE roll = " + myroll
            cursor.execute(sql)
            result = cursor.fetchall()
            connection.commit()
            print(result)
    finally:
        connection.close()
        print("\nSearch student task completed\n")
    return


def removeStudent():
    # Connect to the database
    connection = pymysql.connect(host='127.0.0.1', user='root', password='onsi', db='projects', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    print("\tremove student Area")
    try:
        with connection.cursor() as cursor:
            # Read a single record
            myroll = input("enter roll no: ")
            sql = "DELETE FROM projects.studentinformation WHERE roll = " + myroll
            print(sql)
            cursor.execute(sql)
            connection.commit()
            # result = cursor.rowcount()
            # print(result,"row deleted")
    finally:
        connection.close()
        print("\nstudent removed task completed\n")
    return


while True:   
    start()