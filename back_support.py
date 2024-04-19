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


# 获取用户信息的路由
@app.route('/user_info', methods=['POST'])
def user_info():
    #***************************************#
    print("开始搜索用户信息")
    
    try:
        data = request.json
        if not data or 'id' not in data:
            return jsonify({'success': False, 'message': 'Invalid request format'}), 400

        user_id = data['id']

        # 获取数据库连接
        cur = mysql.connection.cursor()

        # 查询用户信息
        sql = "SELECT * FROM Users WHERE ID=%s"
        cur.execute(sql, (user_id,))
        user = cur.fetchone()

        if not user:
            return jsonify({'success': False, 'message': 'User not found'}), 404

        # 检查用户是否被分配了房间
        if 'room_id' in user and user['room_id'] is not None:
            return jsonify({'success': True, 'user': user, 'message': 'User has been assigned a room'}), 200
        else:
            return jsonify({'success': True, 'user': user, 'message': 'User has not been assigned a room'}), 200
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({'success': False, 'message': 'An unexpected error occurred'}), 500
    finally:
        if 'cur' in locals():
            cur.close()



if __name__ == '__main__':
    app.run(debug=True)
