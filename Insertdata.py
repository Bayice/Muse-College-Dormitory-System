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
    data_bed = pd.read_excel('bed.xlsx')
    data_room = pd.read_excel('room.xlsx')

    #db.insert_into_table(data,column_indice(s),table_name,column_name(s))
    """
    db.insert_into_table_tri(data,[0,9,10],'dormitory_supervisor',['Supervisor_ID','Name','Password'])
    db.insert_into_table_bi(data,[1,0],'dormitory',['Dormitory_ID','Dormitory_Supervisor_ID'])
    db.insert_into_table_bi(data,[0,11],'floor_tutor',['Tutor_ID','Name'])
    db.insert_into_table_tetra(data,[1,2,5,0],'floor',['Dormitory_ID','Floor_Number','Gender','Tutor_ID'])
    db.insert_into_table_hept(data_room,[2,1,0,3,6,4,5],'room',['Room_ID','Floor_Number','Dormitory_ID','Room_Type','Room_Tag','StudentType','Is_empty'])
    """
    db.insert_into_table_penta(data_bed,[2,0,1,3,4],'bed',['Room_ID','Dormitory_ID','Floor_Number','Bed_Number','Is_empty'])
    db.insert_into_table_student(data,[6,4,3,2,1,7,5,14,8,15],'student',['Student_ID','Bed_Number','Room_ID','Floor_Number','Dormitory_ID','Name','Gender','Age_Class','Type','Contact'])