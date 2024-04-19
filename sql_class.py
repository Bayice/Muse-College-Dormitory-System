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
        use_db_query = "USE csc3170"
        self.cursor.execute(use_db_query)
        self.cursor.execute("SHOW TABLES")
        result = self.cursor.fetchall()
        if result:
            print("Tables in database csc3170 :")
            for table in result:
                print(table[0])
        else:
            print("No tables found in database csc3170")

    def create_table(self, table_name, columns):
        # 创建表
        use_db_query = "USE csc3170"
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
        use_db_query = "USE csc3170"
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
        use_db_query = "USE csc3170"
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

            
    def insert_into_table_bi(self, data, column_indices, table_name, column_names):
        if len(column_indices) != len(column_names):
            print("Error: Number of column indices does not match number of column names.")
            return

        for index, row in data.iterrows():
            value1 = row.iloc[column_indices[0]]
            value2 = row.iloc[column_indices[1]]

            select_query = "SELECT {}, {} FROM {} WHERE {} = '{}' AND {} = '{}'".format(column_names[0], column_names[1], table_name, column_names[0], value1, column_names[1], value2)
            self.cursor.execute(select_query)
            result = self.cursor.fetchone()

            if result is not None and result[0] == value1 and result[1] == value2:
                continue

            insert_query = "INSERT INTO {} ({}, {}) VALUES ('{}', '{}') ON DUPLICATE KEY UPDATE {} = '{}', {} = '{}'".format(table_name, column_names[0], column_names[1], value1, value2, column_names[0], value1, column_names[1], value2)
            try:
                self.cursor.execute(insert_query)
                self.connection.commit()
                print("Data inserted successfully.")
            except pymysql.Error as e:
                print("Error inserting data:", e)

                    
    def insert_into_table_tri(self, data, column_indices, table_name, column_names):
        if len(column_indices) != len(column_names):
            print("Error: Number of column indices does not match number of column names.")
            return

        for index, row in data.iterrows():
            value1 = row.iloc[column_indices[0]]
            value2 = row.iloc[column_indices[1]]
            value3 = row.iloc[column_indices[2]]

            select_query = "SELECT {}, {}, {} FROM {} WHERE {} = '{}' AND {} = '{}' AND {} = '{}'".format(column_names[0], column_names[1], column_names[2], table_name, column_names[0], value1, column_names[1], value2, column_names[2], value3)
            self.cursor.execute(select_query)
            result = self.cursor.fetchone()

            if result is not None and result[0] == value1 and result[1] == value2 and result[2] == value3:
                continue

            insert_query = "INSERT INTO {} ({}, {}, {}) VALUES ('{}', '{}', '{}') ON DUPLICATE KEY UPDATE {} = '{}', {} = '{}', {} = '{}'".format(table_name, column_names[0], column_names[1], column_names[2], value1, value2, value3, column_names[0], value1, column_names[1], value2, column_names[2], value3)
            try:
                self.cursor.execute(insert_query)
                self.connection.commit()
                print("Data inserted successfully.")
            except pymysql.Error as e:
                print("Error inserting data:", e)

    
    def insert_into_table_tetra(self, data, column_indices, table_name, column_names):
        if len(column_indices) != len(column_names):
            print("Error: Number of column indices does not match number of column names.")
            return

        for index, row in data.iterrows():
            value1 = row.iloc[column_indices[0]]
            value2 = row.iloc[column_indices[1]]
            value3 = row.iloc[column_indices[2]]
            value4 = row.iloc[column_indices[3]]
        
            select_query = "SELECT {}, {}, {}, {} FROM {} WHERE {} = '{}' AND {} = '{}' AND {} = '{}' AND {} = '{}'".format(column_names[0], column_names[1], column_names[2], column_names[3], table_name, column_names[0], value1, column_names[1], value2, column_names[2], value3, column_names[3], value4)
            self.cursor.execute(select_query)
            result = self.cursor.fetchone()

            if result is not None and result[0] == value1 and result[1] == value2 and result[2] == value3 and result[3] == value4:
                continue

            insert_query = "INSERT INTO {} ({}, {}, {}, {}) VALUES ('{}', '{}', '{}', '{}') ON DUPLICATE KEY UPDATE {} = '{}', {} = '{}', {} = '{}', {} = '{}'".format(table_name, column_names[0], column_names[1], column_names[2], column_names[3], value1, value2, value3, value4, column_names[0], value1, column_names[1], value2, column_names[2], value3, column_names[3], value4)
            try:
                self.cursor.execute(insert_query)
                self.connection.commit()
                print("Data inserted successfully.")
            except pymysql.Error as e:
                print("Error inserting data:", e)


    def insert_into_table_penta(self, data, column_indices, table_name, column_names):
        if len(column_indices) != len(column_names):
            print("Error: Number of column indices does not match number of column names.")
            return

        for index, row in data.iterrows():
            value1 = row.iloc[column_indices[0]]
            value2 = row.iloc[column_indices[1]]
            value3 = row.iloc[column_indices[2]]
            value4 = row.iloc[column_indices[3]]
            value5 = row.iloc[column_indices[4]]
    
            select_query = "SELECT {}, {}, {}, {}, {} FROM {} WHERE {} = '{}' AND {} = '{}' AND {} = '{}' AND {} = '{}' AND {} = '{}'".format(column_names[0], column_names[1], column_names[2], column_names[3], column_names[4], table_name, column_names[0], value1, column_names[1], value2, column_names[2], value3, column_names[3], value4, column_names[4], value5)
            self.cursor.execute(select_query)
            result = self.cursor.fetchone()

            if result is None:
                insert_query = "INSERT INTO {} ({}, {}, {}, {}, {}) VALUES ('{}', '{}', '{}', '{}', '{}') ON DUPLICATE KEY UPDATE {} = '{}', {} = '{}', {} = '{}', {} = '{}', {} = '{}'".format(table_name, column_names[0], column_names[1], column_names[2],column_names[3], column_names[4], value1, value2, value3, value4, value5, column_names[0], value1, column_names[1], value2, column_names[2], value3, column_names[3], value4, column_names[4], value5)
                try:
                    self.cursor.execute(insert_query)
                    self.connection.commit()
                    print("Data inserted successfully.")
                except pymysql.Error as e:
                    print("Error inserting data:", e)
            elif result[0] != value1 or result[1] != value2 or result[2] != value3 or result[3] != value4 or result[4] != value5:
                update_query = "UPDATE {} SET {} = '{}', {} = '{}', {} = '{}', {} = '{}', {} = '{}' WHERE {} = '{}' AND {} = '{}' AND {} = '{}' AND {} = '{}' AND {} = '{}'".format(table_name, column_names[0], value1, column_names[1], value2, column_names[2], value3, column_names[3], value4, column_names[4], value5, column_names[0], value1, column_names[1], value2, column_names[2], value3, column_names[3], value4, column_names[4], value5)
                try:
                    self.cursor.execute(update_query)
                    self.connection.commit()
                    print("Data updated successfully.")
                except pymysql.Error as e:
                    print("Error updating data:", e)


             
    def insert_into_table_hexa(self, data, column_indices, table_name, column_names):
        if len(column_indices) != len(column_names):
            print("Error: Number of column indices does not match number of column names.")
            return

        for index, row in data.iterrows():
            values = [row.iloc[column_indices[i]] for i in range(len(column_indices))]
        
            select_query = "SELECT {} FROM {} WHERE {}".format(', '.join(column_names), table_name, ' AND '.join([f"{column_names[i]} = %s" for i in range(len(column_names))]))
            self.cursor.execute(select_query, values)
            result = self.cursor.fetchone()

            if result is not None and result == tuple(values):
                continue

            insert_query = "INSERT INTO {} ({}) VALUES ({}) ON DUPLICATE KEY UPDATE {}".format(table_name, ', '.join(column_names), ', '.join(['%s'] * len(column_names)), ', '.join([f"{col} = %s" for col in column_names]))
            try:
                self.cursor.execute(insert_query, values * 2)
                self.connection.commit()
            except pymysql.Error as e:
                print("Error inserting or updating data:", e)

    
    def insert_into_table_hept(self, data, column_indices, table_name, column_names):
        if len(column_indices) != len(column_names):
            print("Error: Number of column indices does not match number of column names.")
            return

        for index, row in data.iterrows():
            values = [row.iloc[column_index] for column_index in column_indices]

            select_query = "SELECT * FROM {} WHERE {}".format(table_name, ' AND '.join([f"{column_names[i]} = %s" for i in range(len(column_names))]))
            self.cursor.execute(select_query, values)
            result = self.cursor.fetchone()

            if result is not None and result == tuple(values):
                continue

            insert_query = "INSERT INTO {} ({}) VALUES ({}) ON DUPLICATE KEY UPDATE {}".format(table_name, ', '.join(column_names), ', '.join(['%s'] * len(column_names)), ', '.join([f"{col} = %s" for col in column_names]))
            try:
                self.cursor.execute(insert_query, values * 2)
                self.connection.commit()
            except pymysql.Error as e:
                print("Error inserting or updating data:", e)

    
    def insert_into_table_student(self, data, column_indices, table_name, column_names):
        if len(column_indices) != len(column_names):
            print("Error: Number of column indices does not match number of column names.")
            return

        for index, row in data.iterrows():
            values = [row.iloc[column_index] for column_index in column_indices]

            # Check if corresponding row exists in bed table
            select_bed_query = "SELECT * FROM bed WHERE Room_ID = %s AND Bed_Number = %s"
            self.cursor.execute(select_bed_query, (values[2], values[1]))
            bed_result = self.cursor.fetchone()

            if bed_result is None:
                print("Error: No matching row in bed table. Cannot insert data into student table.", values)
                continue

            select_query = "SELECT * FROM {} WHERE {} = %s AND {} = %s AND {} = %s AND {} = %s AND {} = %s AND {} = %s AND {} = %s AND {} = %s AND {} = %s AND {} = %s".format(table_name, *column_names)
            self.cursor.execute(select_query, values)
            result = self.cursor.fetchone()

            if result is None:
                # Check if the new data is the same as the existing data
                check_query = "SELECT * FROM {} WHERE {} = %s AND {} = %s AND {} = %s AND {} = %s AND {} = %s AND {} = %s AND {} = %s AND {} = %s AND {} = %s AND {} = %s".format(table_name, *column_names)
                self.cursor.execute(check_query, values)
                existing_data = self.cursor.fetchone()

                if existing_data is not None and existing_data[:len(values)] == tuple(values):
                    print("Data already exists in the table with the same values. Skipping insertion and update.")
                    continue

                insert_query = "INSERT INTO {} ({}) VALUES ({}) ON DUPLICATE KEY UPDATE {}".format(table_name, ', '.join(column_names), ', '.join(['%s'] * len(column_names)), ', '.join([f"{col} = %s" for col in column_names]))
                try:
                    self.cursor.execute(insert_query, values + values)
                    self.connection.commit()
                    print("Data inserted successfully.")

                    # Update Is_empty column in room table
                    update_room_query = "UPDATE room SET Is_empty = 0 WHERE Room_ID = %s"
                    self.cursor.execute(update_room_query, (values[2],))
                    self.connection.commit()
                    print("Is_empty column in room table updated successfully.")

                    # Update Is_empty column in bed table
                    update_bed_query = "UPDATE bed SET Is_empty = 0 WHERE Bed_Number = %s"
                    self.cursor.execute(update_bed_query, (values[1],))
                    self.connection.commit()
                    print("Is_empty column in bed table updated successfully.")
                except pymysql.Error as e:
                    print("Error inserting data:", e)
            else:
                continue


    ##试过用循环+列数 只用一个函数来实现，但是在插入数据的过程中会出现问题，所以分开写了

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
        delete_query = "DELETE FROM {}".format(table_name)
        try:
            self.cursor.execute(delete_query)
            self.connection.commit()
            print("Table '{}' data cleared successfully.".format(table_name))
        except pymysql.err.ProgrammingError as err:
            print("Error deleting data from table '{}': {}".format(table_name, err))

    def drop_all(self):
        self.drop_table("Student")
        self.drop_table("Bed")
        self.drop_table("Room")
        self.drop_table("Floor")
        self.drop_table("Floor_Tutor")
        self.drop_table("Dormitory")
        self.drop_table("Dormitory_Supervisor")
