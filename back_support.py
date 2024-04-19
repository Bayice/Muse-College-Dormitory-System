from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL配置
app.config['MYSQL_HOST'] = '10.23.68.16'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'csc3170'

# 初始化MySQL
mysql = MySQL(app)

# 用户认证的路由
@app.route('/authenticate', methods=['POST'])
def authenticate():
    #***************************************#
    print("--进行登录认证--")

    try:
        data = request.json
        if not data or 'id' not in data or 'password' not in data:
            return jsonify({'success': False, 'message': 'Invalid request format'}), 400

        user_id = data['id']
        password = data['password']

        # 获取数据库连接
        cur = mysql.connection.cursor()

        # 查询数据库中是否有匹配的用户
        sql = "SELECT * FROM Dormitory_Supervisor WHERE Supervisor_ID=%s AND Password=%s"
        cur.execute(sql, (user_id, password))
        supervisor = cur.fetchone()

        #***************************************#
        print("开始搜索舍监")

        if supervisor:
            # 如果找到舍监用户，返回用户信息和身份
            return jsonify({'success': True, 'user': supervisor, 'role': 'supervisor'}), 200

        sql = "SELECT * FROM Floor_Tutor WHERE Tutor_ID=%s AND Password=%s"
        cur.execute(sql, (user_id, password))
        tutor = cur.fetchone()

        #***************************************#
        print("开始搜索导师")

        if tutor:
            # 如果找到导师用户，返回用户信息和身份
            return jsonify({'success': True, 'user': tutor, 'role': 'tutor'}), 200

        sql = "SELECT * FROM Student WHERE Student_ID=%s AND Password=%s"
        cur.execute(sql, (user_id, password))
        student = cur.fetchone()

        #***************************************#
        print("开始搜索学生")

        if student:
            # 如果找到学生用户，返回用户信息和身份
            return jsonify({'success': True, 'user': student, 'role': 'student'}), 200

        # 如果未找到用户，返回验证失败的标志
        return jsonify({'success': False, 'message': 'Invalid user ID or password'}), 401
    except Exception as e:
        # 记录错误日志
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({'success': False, 'message': 'An unexpected error occurred'}), 500
    finally:
        # 确保关闭数据库连接
        if 'cur' in locals():
            cur.close()


# 房间搜索的路由
@app.route('/search_rooms', methods=['POST'])
def search_rooms():
    #***************************************#
    print("开始搜索要求的房间")

    try:
        data = request.json
        if not data or 'floors' not in data or 'room_type' not in data:
            return jsonify({'success': False, 'message': 'Invalid request format'}), 400


        # 解析请求数据
        floors = data['floors']
        room_type = data['room_type']
        student_type = data.get('student_type')
        gender = data.get('gender')
        buildings = data.get('buildings')

        # 获取数据库连接
        cur = mysql.connection.cursor()

        # 构建查询条件
        where_conditions = []
        if floors:
            for floor in floors:
                where_conditions.append(f"Floor.Floor_Number={floor}")
        floor_clause = "(" + " OR ".join(where_conditions) + ")"
            

        where_conditions = []      
        if buildings:
            for building in buildings:
                where_conditions.append(f"Room.Dormitory_ID = {building}")

        # 使用 OR 连接所有的 WHERE 条件
        building_clause = "(" + " OR ".join(where_conditions)  + ")"

        # 添加额外的条件：学生类型和性别
        additional_conditions = []
        if student_type:
            additional_conditions.append(f"StudentType='{student_type}'")
        if gender:
            additional_conditions.append(f"Gender='{gender}'")


        # 构建最终的 WHERE 子句
        if additional_conditions:
            building_clause += " AND " + " AND ".join(additional_conditions) + " AND " + floor_clause

        #***************************************#
        print("最终查询语句")
        print(f"WHERE {building_clause} AND Room_Type='{room_type}' AND Is_empty=1")

        # 查询数据库中符合要求的房间信息
        sql = f"""
            SELECT Room.*
            FROM Room
            JOIN Floor ON Room.Floor_Number = Floor.Floor_Number
            WHERE {building_clause} AND Room_Type='{room_type}'
        """
        cur.execute(sql)
        rooms = cur.fetchall()

        # 返回符合要求的房间信息
        return jsonify({'success': True, 'rooms': rooms}), 200
    except Exception as e:
        # 记录错误日志
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({'success': False, 'message': 'An unexpected error occurred'}), 500
    finally:
        # 确保关闭数据库连接
        if 'cur' in locals():
            cur.close()


if __name__ == '__main__':
    app.run(debug=True)
