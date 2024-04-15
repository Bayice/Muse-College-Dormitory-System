import random
import string
import pymysql

class MySQL:
    def __init__(self, host, user, password, database):
        # 初始化数据库连接
        self.connection = pymysql.connect(
            host = host,
            user = user,
            password = password,
            database = database,
            autocommit = False
        )
        self.cursor = self.connection.cursor()

    def close_connection(self):
        # 关闭数据库连接
        self.cursor.close()
        self.connection.close()

    def drop_db(self, db_name):
        # 删除数据库
        drop_db_query = "DROP DATABASE IF EXISTS {}".format(db_name)
        self.cursor.execute(drop_db_query)
        self.connection.commit()
        print("Database '{}' dropped successfully.".format(db_name))

    def show_all_dbs(self):
        # 显示所有数据库
        self.cursor.execute("SHOW DATABASES")
        result = self.cursor.fetchall()
        if result:
            print("All databases:")
            for db in result:
                print(db[0])
        else:
            print("No databases found.")

    def show_db_tables(self):
        # 显示数据库中的所有表
        use_db_query = "USE {}".format(database)
        self.cursor.execute(use_db_query)
        self.cursor.execute("SHOW TABLES")
        result = self.cursor.fetchall()
        if result:
            print("Tables in database '{}':".format(database))
            for table in result:
                print(table[0])
        else:
            print("No tables found in database '{}'.".format(database))

    def create_table(self, table_name, columns):
        # 创建表
        use_db_query = "USE {}".format(database)
        self.cursor.execute(use_db_query)
        create_table_query = "CREATE TABLE IF NOT EXISTS {} ({})".format(table_name, columns)
        try:
            self.cursor.execute(create_table_query)
            self.connection.commit()
            print("Table '{}' created successfully.".format(table_name))
        except pymysql.err.ProgrammingError as err:
            print("Error creating table: {}".format(err))

    def drop_table(self, table_name):
        # 删除表
        use_db_query = "USE {}".format(database)
        self.cursor.execute(use_db_query)
        drop_table_query = "DROP TABLE IF EXISTS {}".format(table_name)
        try:
            self.cursor.execute(drop_table_query)
            self.connection.commit()
            print("Table '{}' dropped successfully.".format(table_name))
        except pymysql.err.ProgrammingError as err:
            print("Error dropping table: {}".format(err))

    def describe_table(self, table_name):
        # 描述表结构
        use_db_query = "USE {}".format(database)
        self.cursor.execute(use_db_query)
        describe_query = "DESCRIBE {}".format(table_name)
        self.cursor.execute(describe_query)
        result = self.cursor.fetchall()
        if result:
            print("Structure of table '{}':".format(table_name))
            for row in result:
                print(row)
        else:
            print("Table '{}' does not exist.".format(table_name))

    def insert_into_table(self, table_name, values):
        # 向表中插入数据
        columns = ', '.join(values.keys())
        placeholders = ', '.join(['%s'] * len(values))
        insert_query = "INSERT INTO {} ({}) VALUES ({})".format(table_name, columns, placeholders)
        try:
            self.cursor.execute(insert_query, list(values.values()))
            self.connection.commit()
            print("Data inserted into '{}' successfully.".format(table_name))
        except pymysql.err.ProgrammingError as err:
            print("Error inserting data into table: {}".format(err))

    def select_from_table(self, table_name, columns='*', condition=None):
        # 从表中查询数据
        select_query = "SELECT {} FROM {}".format(columns, table_name)
        if condition:
            select_query += " WHERE {}".format(condition)
        try:
            self.cursor.execute(select_query)
            result = self.cursor.fetchall()
            if result:
                print("Data from table '{}':".format(table_name))
                for row in result:
                    print(row)
            else:
                print("No data found in table '{}'.".format(table_name))
        except pymysql.err.ProgrammingError as err:
            print("Error selecting data from table: {}".format(err))

    def clear_table(self, table_name):
        # 清空表中数据
        truncate_query = "TRUNCATE TABLE {}".format(table_name)
        try:
            self.cursor.execute(truncate_query)
            print("Table '{}' data cleared successfully.".format(table_name))
        except pymysql.err.ProgrammingError as err:
            print("Error truncating table '{}': {}".format(table_name, err))

    def drop_all(self):
        self.drop_table("Student")
        self.drop_table("Bed")
        self.drop_table("Room")
        self.drop_table("Floor")
        self.drop_table("Floor_Tutor")
        self.drop_table("Dormitory")
        self.drop_table("Dormitory_Supervisor")

if __name__ == '__main__':
    host = "10.30.102.224"#这是远程连接数据库的ip，连接学校网络可以查询，更改为localhost可以连接到自己本地数据库
    user = "root"
    password = "123456"
    database = "csc3170"
    db = MySQL(host, user, password, database)
    
    # db.drop_all()

    # 创建 Dormitory_Supervisor 表格
    dormitory_supervisor_columns = (
        "Supervisor_ID INT PRIMARY KEY, "
        "Name VARCHAR(50)"
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
        "Name VARCHAR(50)"
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
        "PRIMARY KEY (Room_ID, Dormitory_ID, Bed_Number), "
        "FOREIGN KEY (Room_ID, Floor_Number,Dormitory_ID) REFERENCES Room(Room_ID, Floor_Number,Dormitory_ID)"
    )
    db.create_table("Bed", bed_columns)

    # 创建 Student 表格
    student_columns = (
        "Student_ID INT PRIMARY KEY, "
        "Name VARCHAR(50), "
        "Gender VARCHAR(10), "
        "Age_Class VARCHAR(50), "
        "Type  VARCHAR(50), "
        "Contact VARCHAR(50), "
        "Room_ID VARCHAR(50), "
        "Bed_Number INT, "
        "Dormitory_ID VARCHAR(50), "
        "FOREIGN KEY (Room_ID, Dormitory_ID, Bed_Number) REFERENCES Bed(Room_ID, Dormitory_ID, Bed_Number)"
    )
    db.create_table("Student", student_columns)

    db.show_db_tables()
