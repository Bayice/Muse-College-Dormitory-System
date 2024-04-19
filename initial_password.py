import hashlib
import pymysql

# 连接数据库
connection = pymysql.connect(host='10.23.68.16',
                             user='root',
                             password='123456',
                             database='csc3170',
                             cursorclass=pymysql.cursors.DictCursor)

def generate_hash(student_id):
    hashed_id = hashlib.sha256(str(student_id).encode()).hexdigest()
    password = int(hashed_id[:8], 16)
    password %= 100000000
    print(password)
    return password

try:
    with connection.cursor() as cursor:
        # 查询数据库中所有用户
        sql = "SELECT * FROM Dormitory_Supervisor"
        cursor.execute(sql)
        supervisors = cursor.fetchall()

        # #*********************#
        # print("更新舍监")

        # # 更新舍监用户的密码
        # for supervisor in supervisors:
        #     password = generate_hash(str(supervisor['Supervisor_ID']))  # 使用舍监ID生成密码
        #     sql_update = "UPDATE Dormitory_Supervisor SET Password=%s WHERE Supervisor_ID=%s"
        #     cursor.execute(sql_update, (password, supervisor['Supervisor_ID']))

        # # 查询数据库中所有用户
        # sql = "SELECT * FROM Floor_Tutor"
        # cursor.execute(sql)
        # tutors = cursor.fetchall()

        # #*********************#
        # print("更新导师")
        # # 更新导师用户的密码
        # for tutor in tutors:
        #     password = generate_hash(str(tutor['Tutor_ID']))  # 使用导师ID生成密码
        #     sql_update = "UPDATE Floor_Tutor SET Password=%s WHERE Tutor_ID=%s"
        #     cursor.execute(sql_update, (password, tutor['Tutor_ID']))

        # 查询数据库中所有用户
        sql = "SELECT * FROM Student"
        cursor.execute(sql)
        students = cursor.fetchall()

        #*********************#
        print("更新学生")

        # 更新学生用户的密码
        for student in students:
            password = generate_hash(str(student['Student_ID']))  # 使用学生ID生成密码
            sql_update = "UPDATE Student SET Password=%s WHERE Student_ID=%s"
            cursor.execute(sql_update, (password, student['Student_ID']))

    # 提交更新
    connection.commit()
    print("密码初始化完成！")
except Exception as e:
    # 发生错误时回滚更改
    print(f"An error occurred: {str(e)}")
    connection.rollback()
finally:
    # 关闭数据库连接
    connection.close()
