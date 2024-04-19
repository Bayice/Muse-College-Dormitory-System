from sql_class import MySQL
import pymysql 
import pandas as pd


if __name__ == '__main__':
    host = "10.23.68.16"
    user = "root"
    password = "123456"
    database = "csc3170"
    db = MySQL(host, user, password, database)
    
    #从excel中读取数据
    data = pd.read_excel('simulator.xlsx')

    #db.insert_into_table(data,column_indice(s),table_name,column_name(s))
    ##PK insert
    db.insert_into_table(data,0,'dormitory_supervisor','Supervisor_ID')
    db.insert_into_table(data,1,'dormitory','Dormitory_ID')
    db.insert_into_table(data,0,'floor_tutor','Tutor_ID')
    db.insert_into_table_bi(data,[1,2],'floor',['Dormitory_ID','Floor_Number'])
    db.insert_into_table_tri(data,[3,2,1],'room',['Room_ID','Floor_Number','Dormitory_ID'])
    db.insert_into_table_tetra(data,[3,1,2,4],'bed',['Room_ID','Dormitory_ID','Floor_Number','Bed_Number'])
    db.insert_into_table_penta(data,[6,4,3,2,1],'student',['Student_ID','Bed_Number','Room_ID','Floor_Number','Dormitory_ID'])
    
    """无法顺利插入的非PK,FK数据
    db.insert_into_table_bi(data,[9,10],'dormitory_supervisor',['Name','Password'])
    db.insert_into_table(data,1,'dormitory','Dormitory_Supervisor_ID')
    db.insert_into_table_bi(data,[5,0],'floor',['Gender','Tutor_ID'])
    db.insert_into_table(data,11,'floor_tutor','Name')
    db.insert_into_table_tri(data,[12,13,8],'room',['Room_Type','Room_Tag','StudentType'])
    db.insert_into_table_penta(data,[7,6,14,8,14],'student',['Name','Gender','Age_Class','Type','Contact'])
    """
 