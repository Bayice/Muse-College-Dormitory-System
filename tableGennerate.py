from sql_class import MySQL
import random
import string
import pymysql

if __name__ == '__main__':
    host = "10.31.106.177"#这是远程连接数据库的ip不固定，连接学校网络可以查询，更改为localhost可以连接到自己本地数据库
    user = "root"
    password = "123456"
    database = "csc3170"
    db = MySQL(host, user, password, database)
    
    # db.drop_all()

    # 创建 Dormitory_Supervisor 表格
    dormitory_supervisor_columns = (
        "Supervisor_ID INT PRIMARY KEY, "
        "Name VARCHAR(50),"
        "Password INT"
    )
    db.create_table("Dormitory_Supervisor", dormitory_supervisor_columns)
    
    # 创建 Dormitory 表格
    dormitory_columns = (
        "Dormitory_ID VARCHAR(50) PRIMARY KEY, "
        "Dormitory_Supervisor_ID INT, "
        "FOREIGN KEY (Dormitory_Supervisor_ID) REFERENCES Dormitory_Supervisor(Supervisor_ID)"
    )
    db.create_table("Dormitory", dormitory_columns)

    # 创建 Floor_Tutor 表格
    floor_tutor_columns = (
        "Tutor_ID INT PRIMARY KEY, "
        "Name VARCHAR(50),"
        "Password INT"
    )
    db.create_table("Floor_Tutor", floor_tutor_columns)

    # 创建 Floor 表格
    floor_columns = (
        "Floor_Number INT, "
        "Dormitory_ID VARCHAR(50), "
        "Gender VARCHAR(10), "
        "Tutor_ID INT, "
        "PRIMARY KEY (Floor_Number, Dormitory_ID), "
        "FOREIGN KEY (Dormitory_ID) REFERENCES Dormitory(Dormitory_ID), "
        "FOREIGN KEY (Tutor_ID) REFERENCES Floor_Tutor(Tutor_ID)"
    )
    db.create_table("Floor", floor_columns)

    # 创建 Room 表格
    room_columns = (
        "Room_ID VARCHAR(50), "
        "Room_Type VARCHAR(50), "
        "Room_Tag VARCHAR(100), "
        "StudentType VARCHAR(50), "
        "Floor_Number INT, "
        "Dormitory_ID VARCHAR(50), "
        "PRIMARY KEY (Room_ID, Floor_Number, Dormitory_ID), "
        "FOREIGN KEY (Floor_Number, Dormitory_ID) REFERENCES Floor(Floor_Number, Dormitory_ID)"
    )
    db.create_table("Room", room_columns)

    # 创建 Bed 表格
    bed_columns = (
        "Room_ID VARCHAR(50), "
        "Dormitory_ID VARCHAR(50), "
        "Bed_Number INT, "
        "Floor_Number INT, "
        "PRIMARY KEY (Room_ID, Dormitory_ID, Floor_Number, Bed_Number), "
        "FOREIGN KEY (Room_ID, Floor_Number,Dormitory_ID) REFERENCES Room(Room_ID, Floor_Number,Dormitory_ID)"
    )
    db.create_table("Bed", bed_columns)

    # 创建 Student 表格
    student_columns = (
        "Student_ID INT PRIMARY KEY, "
        "Name VARCHAR(50), "
        "Type  VARCHAR(50), "
        "Dormitory_ID VARCHAR(50), "
        "Floor_Number INT, "
        "Room_ID VARCHAR(50), "
        "Gender VARCHAR(10), "
        "Age_Class VARCHAR(50), "
        "Contact VARCHAR(50), "
        "Bed_Number INT, "
        "Password INT,"
        "FOREIGN KEY (Room_ID, Dormitory_ID, Floor_Number, Bed_Number) REFERENCES Bed(Room_ID, Dormitory_ID, Floor_Number, Bed_Number)"
    )
    db.create_table("Student", student_columns)

    db.show_db_tables()
