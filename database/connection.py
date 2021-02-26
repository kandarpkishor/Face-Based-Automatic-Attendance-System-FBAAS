import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection
conn=create_connection("attendance_db.SQLite")
# def execute_query(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         connection.commit()
#         print("Query executed successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")
# # create_users_table = """
# # CREATE TABLE IF NOT EXISTS student ( 
# # 	ID INTEGER PRIMARY KEY AUTOINCREMENT,
# #     FACE_ID VARCHAR(20) UNIQUE, 
# # 	NAME VARCHAR(60) NOT NULL,
# #     F_NAME VARCHAR(60) NOT NULL, 
# # 	GENDER VARCHAR(15), 
# #     DOB DATE,
# #     ROLL_NO VARCHAR(20), 
# #     SEMESTER VARCHAR(20) NOT NULL,
# #     DEPARTMENT VARCHAR(60) NOT NULL,
# #     EMAIL_ID TEXT NOT NULL,
# #     MOBILE VARCHAR (13) NOT NULL,
# #     ENROLLMENT_DATE DATE
# # );"""
# create_attendance_table = """
# CREATE TABLE IF NOT EXISTS attendance ( 
#   ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     ROLL_ID VARCHAR(20), 
#   NAME VARCHAR(60) NOT NULL,
#     DOA DATE,
#     TOA TIME,
#     DEPARTMENT VARCHAR(60) NOT NULL
# );"""


# execute_query(conn, create_attendance_table)
# create_users = """
# INSERT INTO
#   student (FACE_ID, NAME, F_NAME, GENDER, DOB, ROLL_NO, SEMESTER, DEPARTMENT, EMAIL_ID, MOBILE, ENROLLMENT_DATE)
# VALUES
#   ('180309', 'Kandarp Kishor Jha ', 'Dinesh Kumar Jha', 'Male', '1995-06-17', '180309', '4th', 'MCA', 'kandarpkishor@gmail.com', '8298444957', '2020-07-18')
# """
# execute_query(conn, create_users)


# update_users = """
# UPDATE STUDENT
#   SET FACE_ID=''
# WHERE NAME ='Keshav Kishor Jha'
# """
# execute_query(conn, update_users)



# def execute_read_query(connection, query):
#     cursor = connection.cursor()
#     #result = None
#     try:
#         cursor.execute(query)
#         result = cursor.fetchall()
#         return result
#     except Error as e:
#         print(f"The error '{e}' occurred")
# select_users = "SELECT *FROM attendance"
# # select_users= "SELECT *FROM sqlite_master WHERE "

# users = execute_read_query(conn, select_users)
# # print(users)
# # print("hi")
# for user in users:
#     print(user)
#     print("hi")


#     ('table', 'attendance', 'attendance', 7, 'CREATE TABLE attendance ( \n  ID INTEGER PRIMARY KEY AUTOINCREMENT,\n    ROLL_ID VARCHAR(20), \n  NAME VARCHAR(60) NOT NULL,\n    DOA DATE,\n    TOA TIME,\n    DEPARTMENT VARCHAR(60) NOT NULL\n)')