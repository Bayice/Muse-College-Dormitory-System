from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)  # 启用跨域请求支持在这里

# MySQL配置
app.config['MYSQL_HOST'] = '10.23.68.16'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'csc3170'

# 初始化MySQL
mysql = MySQL(app)

# 初始化LLM

# API信息
# 请求地址: https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions
# API Key: EbCaoBsJCB9YjZlUKUqKvXIm
# Secret Key: vB1jlO8pFgj32pWgOiO4uaIG3wCiuHBM
# 模型名称: ERNIE-3.5-8K
# 应用名称: Dormit
# 网络名称: ernieBot_3.5_8k

def get_access_token():
    """
    使用 API Key,Secret Key 获取access_token,替换下列示例中的应用API Key、应用Secret Key
    """
        
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=EbCaoBsJCB9YjZlUKUqKvXIm&client_secret=vB1jlO8pFgj32pWgOiO4uaIG3wCiuHBM"
    
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "你好"
            },
            {
                "role": "assistant",
                "content": "你好，请问有什么我可以帮助你的吗？无论你有什么问题或需要帮助，我都会尽力回答和协助你。请随时告诉我你的需求。"
            },
            {
                "role": "user",
                "content": "现在如果我要求你帮我选宿舍，请你为我推荐A202A，称这里符号我的年级，性别等要求，还可以看到思廷内庭的景色，而且楼层低，很方便回宿舍休息！"
            },
            {
                "role": "assistant",
                "content": "好的"
            },
            {
                "role": "user",
                "content": "请你帮我选个宿舍吧！"
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")

# 接入文心一言
@app.route('/LLM', methods=['POST'])
def LLM():
    print(get_access_token())
    # 获取 POST 请求中的数据
    data = request.json
    if not data or 'input_string' not in data:
        return jsonify({'message': 'Invalid request format'}), 400

    # 从请求数据中获取输入字符串
    input_string = data['input_string']
    print(input_string)

    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + get_access_token()
    
    
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "你好"
            },
            {
                "role": "assistant",
                "content": "你好，请问有什么我可以帮助你的吗？无论你有什么问题或需要帮助，我都会尽力回答和协助你。请随时告诉我你的需求。"
            },
            {
                "role": "user",
                "content": "现在如果我要求你帮我选宿舍，请你为我推荐A202A，称这里符号我的年级，性别等要求，此外，由于我的自我介绍说我希望学习方便，你会告诉我，根据我的自我介绍，同时喜欢看风景，因此还可以看到思廷内庭的景色，而且楼层低，很方便回宿舍休息！请确保你提到了是根据我的自我介绍给出了推荐"
            },
            {
                "role": "assistant",
                "content": "好的"
            },
            {
                "role": "user",
                "content": "请你帮我选个宿舍吧！"
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    # 返回处理后的字符串作为响应
    return response.json().get('result', ''), 200

# # 接收用户消息的路由
# @app.route('/send_message', methods=['POST'])
# def send_message():
#     data = request.json
#     if not data or 'message' not in data:
#         return jsonify({'success': False, 'message': 'Invalid request format'}), 400
    
#     user_message = data['message']
    
#     # 调用ChatGPT模型生成回复
#     gpt_response = chat_with_gpt(user_message)
    
    return jsonify({'success': True, 'response': gpt_response}), 200

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
        
         #***************************************#
        print("开始搜索管理员")
        
        # 查询数据库中是否有匹配的管理员
        sql = "SELECT * FROM admin WHERE Admin_ID=%s AND Password=%s"
        cur.execute(sql, (user_id, password))
        admin = cur.fetchone()

        if admin:
            # 如果找到舍监用户，返回用户信息和身份
            return jsonify({'success': True, 'user': admin, 'role': 'admin'}), 200

        #***************************************#
        print("开始搜索舍监")
        
        # 查询数据库中是否有匹配的用户
        sql = "SELECT * FROM Dormitory_Supervisor WHERE Supervisor_ID=%s AND Password=%s"
        cur.execute(sql, (user_id, password))
        supervisor = cur.fetchone()

        if supervisor:
            # 如果找到舍监用户，返回用户信息和身份
            return jsonify({'success': True, 'user': supervisor, 'role': 'supervisor'}), 200


        #***************************************#
        print("开始搜索导师")
        sql = "SELECT * FROM Floor_Tutor WHERE Tutor_ID=%s AND Password=%s"
        cur.execute(sql, (user_id, password))
        tutor = cur.fetchone()

        if tutor:
            # 如果找到导师用户，返回用户信息和身份
            return jsonify({'success': True, 'user': tutor, 'role': 'tutor'}), 200


        #***************************************#
        print("开始搜索学生")
        
        sql = "SELECT * FROM Student WHERE Student_ID=%s AND Password=%s"
        cur.execute(sql, (user_id, password))
        student = cur.fetchone()

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


# 添加学生到宿舍的路由
@app.route('/AddAStudent', methods=['POST'])
def add_student_to_dormitory():
    try:
        print("开始读取")
        data = request.json
        if not data or 'id' not in data or 'dormitory' not in data:
            return jsonify({'success': False, 'message': 'Invalid request format'}), 400

        student_id = data['id']
        bed_id = data['dormitory']
        print("读取结束")
        # 获取数据库连接
        cur = mysql.connection.cursor()

        # 查询学生当前的床位信息
        print(student_id)
        
        select_sql = f"""
        SELECT Room_ID
        FROM Student
        WHERE Student_ID = {student_id}
        """
        cur.execute(select_sql)
        result = cur.fetchone()

        if result:
            # 如果学生有床位，则更新对应的床位状态
            room_id = result
            update_sql = """
            UPDATE Bed
            SET Is_empty = 1
            WHERE Room_ID = %s

            """
            cur.execute(update_sql, (room_id))
            print("床位状态更新成功！")  
            
        dormitory_id = bed_id[0]
        if dormitory_id == 'A':
            dormitory_id = "MuseCollege-A"
        elif dormitory_id == 'B':
            dormitory_id = "MuseCollege-B"
        elif dormitory_id == 'C':
            dormitory_id = "MuseCollege-C"
    
        room_id = bed_id[0:4]
        floor = int(bed_id[1])
        print(room_id,floor,dormitory_id,student_id)
        # 更新数据库中的学生信息
        sql = f"UPDATE student SET Bed_Number = '{bed_id}', Room_ID='{room_id}', Floor_Number={floor}, Dormitory_ID ='{dormitory_id}' WHERE Student_ID={student_id}"
        print(sql)
        cur.execute(sql)
        print("成功一半")
        # 更新房间的 is_empty 属性
        sql = f"""
            UPDATE Room 
            SET Is_empty = CASE WHEN (SELECT COUNT(*) FROM Student WHERE Room_ID='{room_id}') >= 4 THEN 0 ELSE 1 END 
            WHERE Room_ID='{room_id}'
        """
        print(sql)
        cur.execute(sql)
        
        # 更新房间的 is_empty 属性
        sql = f"""
            UPDATE bed
            SET Is_empty = 0 
            WHERE Bed_Number='{bed_id}'
        """
        cur.execute(sql)
      

        mysql.connection.commit()

        return jsonify({'success': True, 'message': 'Student added to dormitory successfully'}), 200
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({'success': False, 'message': 'An unexpected error occurred'}), 500
    finally:
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

        # 选房型
        where_conditions = []
        if room_type:
            for type_r in room_type:
                where_conditions.append(f"Room_type= '{type_r}'")
        type_clause = "(" + " OR ".join(where_conditions) + ")"

        # 构建查询条件
        where_conditions = []
        if floors:
            for floor in floors:
                where_conditions.append(f"Floor.Floor_Number={floor}")
        floor_clause = "(" + " OR ".join(where_conditions) + ")"
            

        where_conditions = []      
        if buildings:
            for building in buildings:
                where_conditions.append(f"Room.Dormitory_ID = '{building}'")

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
            building_clause += " AND " + " AND ".join(additional_conditions) + " AND " + floor_clause + " AND " + type_clause


        #***************************************#
        print("最终查询语句")
        print(f"WHERE {building_clause}  AND Is_empty=1")

        # 查询数据库中符合要求的房间信息
        sql = f"""
            SELECT DISTINCT Room.*
            FROM Room
            JOIN Floor ON Room.Floor_Number = Floor.Floor_Number
            WHERE {building_clause}  AND Is_empty=1
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


# 房间修改tag的路由
@app.route('/change_tag', methods=['POST'])
def change_tag():
    print("开始修改房间标签")

    try:
        data = request.json
        room_id = data['Room_ID']
        new_room_tag = data['New_Room_Tag']

        # 获取数据库连接
        cur = mysql.connection.cursor()

        # 更新数据库中的房间标签
        sql = "UPDATE Room SET Room_Tag=%s WHERE Room_ID=%s"
        cur.execute(sql, (new_room_tag, room_id))
        mysql.connection.commit()

        if cur.rowcount == 0:
            return jsonify({'success': False, 'message': 'No room found with the given ID'}), 404

        return jsonify({'success': True, 'message': 'Room tag updated successfully'}), 200
    except Exception as e:
        # 记录错误日志
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({'success': False, 'message': 'An unexpected error occurred'}), 500
    finally:
        # 确保关闭数据库连接
        if 'cur' in locals():
            cur.close()


# 舍监查看整栋宿舍楼的学生信息的路由
@app.route('/view_building', methods=['POST'])
def view_building():
    print("开始查看整楼信息")

    try:
        data = request.json
        if not data or 'Dormitory_Supervisor_ID' not in data:
            return jsonify({'success': False, 'message': 'Invalid request format'}), 400

        Dormitory_Supervisor_ID = data['Dormitory_Supervisor_ID']

        # 获取数据库连接
        cur = mysql.connection.cursor()

        # 第一步：查询楼栋
        cur.execute("SELECT Dormitory_ID FROM dormitory WHERE Dormitory_Supervisor_ID = %s", (Dormitory_Supervisor_ID,))
        dormitory_id = cur.fetchone()
        if not dormitory_id:
            return jsonify({'success': False, 'message': 'No dormitory found for this supervisor'}), 404

        # 第二步：查询所有相关的房间ID
        cur.execute("SELECT Room_ID FROM room WHERE Dormitory_ID = %s", (dormitory_id[0],))
        room_ids = cur.fetchall()

        # 第三步：查询所有相关的学生信息
        students_info = []
        for (room_id,) in room_ids:
            cur.execute("SELECT * FROM student WHERE Room_ID = %s", (room_id,))
            student_data = cur.fetchall()
            students_info.extend(student_data)

        return jsonify({'success': True, 'data': students_info}), 200
    except Exception as e:
        # 记录错误日志
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({'success': False, 'message': 'An unexpected error occurred'}), 500
    finally:
        # 确保关闭数据库连接
        if 'cur' in locals():
            cur.close()


# tutor查看自己所管理的楼层的学生信息的路由
@app.route('/view_floor', methods=['POST'])
def view_floor():
    print("开始查看楼层信息")

    try:
        data = request.json
        if not data or 'Tutor_ID' not in data:
            return jsonify({'success': False, 'message': 'Invalid request format'}), 400

        Tutor_ID = data['Tutor_ID']
        print(type(Tutor_ID))
        print(Tutor_ID)
        # 获取数据库连接
        cur = mysql.connection.cursor()

        # 第一步：查询楼层
        cur.execute("SELECT Floor_Number FROM floor WHERE Tutor_ID = %s", (Tutor_ID,))
        Floor_Number = cur.fetchone()
        cur.execute("SELECT Dormitory_ID FROM floor WHERE Tutor_ID = %s", (Tutor_ID,))
        Dormitory_ID = cur.fetchone()
        if not Floor_Number:
            return jsonify({'success': False, 'message': 'No dormitory found for this supervisor'}), 404
        if not Dormitory_ID:
            return jsonify({'success': False, 'message': 'No dormitory found for this supervisor'}), 404
        # 第二步：查询房间
        cur.execute("SELECT Room_ID FROM room WHERE Dormitory_ID = %s AND Floor_Number = %s", (Dormitory_ID[0],Floor_Number[0]))
        room_ids = cur.fetchall()
        # 第三步：查询所有相关的学生信息
        students_info = []
        for (room_id,) in room_ids:
            cur.execute("SELECT * FROM student WHERE Room_ID = %s", (room_id,))
            student_data = cur.fetchall()
            students_info.extend(student_data)


        return jsonify({'success': True, 'data': students_info}), 200
    
    except Exception as e:
        # 记录错误日志
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({'success': False, 'message': 'An unexpected error occurred'}), 500
    finally:
        # 确保关闭数据库连接
        if 'cur' in locals():
            cur.close()


# 展示某个房间的路由
@app.route('/view_room', methods=['POST'])
def view_room():
    print("开始查看房间信息")

    try:
        data = request.json
        if not data or 'Room_ID' not in data:
            return jsonify({'success': False, 'message': 'Invalid request format'}), 400

        Room_ID = data['Room_ID']

        # 获取数据库连接
        cur = mysql.connection.cursor()

        # 查询相关的学生信息
        cur.execute("SELECT * FROM student WHERE Room_ID = %s", (Room_ID,))
        student_data = cur.fetchall()


        return jsonify({'success': True, 'data': student_data}), 200
    
    except Exception as e:
        # 记录错误日志
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({'success': False, 'message': 'An unexpected error occurred'}), 500
    finally:
        # 确保关闭数据库连接
        if 'cur' in locals():
            cur.close()

# 更新学生介绍的路由
@app.route('/update_student_introduction', methods=['POST'])
def update_student_introduction():
    try:
        data = request.json
        if not data or 'id' not in data or 'introduction' not in data:
            return jsonify({'success': False, 'message': 'Invalid request format'}), 400

        student_id = data['id']
        introduction = data['introduction']

        # 获取数据库连接
        cur = mysql.connection.cursor()

        # 更新学生介绍
        sql = "UPDATE Student SET student_introduction = %s WHERE Student_ID = %s"
        cur.execute(sql, (introduction, student_id))
        mysql.connection.commit()

        return jsonify({'success': True, 'message': 'Student introduction updated successfully'}), 200
    except Exception as e:
        # 记录错误日志
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({'success': False, 'message': 'An unexpected error occurred'}), 500
    finally:
        # 确保关闭数据库连接
        if 'cur' in locals():
            cur.close()
            
# 路由：管理员查询信息
@app.route('/admin_query', methods=['POST'])
def admin_query():
    try:
        data = request.json
        if not data or 'buildings' not in data or 'floors' not in data or 'infors' not in data:
            return jsonify({'success': False, 'message': 'Invalid request format'}), 400

        buildings = data['buildings']
        floors = data['floors']
        infors = data['infors'][0]

        # 获取数据库连接
        cur = mysql.connection.cursor()

        # 构建查询条件
        building_condition = " OR ".join([f"Dormitory_ID = '{building}'" for building in buildings])
        floor_condition = " OR ".join([f"Floor_Number={floor}" for floor in floors])

        print(building_condition)
        print(floor_condition)
        
        # 构建最终的 WHERE 子句
        where_clause = ""
        if buildings:
            where_clause += f"({building_condition})"
        if floors:
            if where_clause:
                where_clause += " AND "
            where_clause += f"({floor_condition})"

        # 查询数据库中符合要求的用户信息
        if infors == 'Dormitory_Supervisor':
            sql = f"""
                SELECT *
                FROM dormitory_supervisor JOIN dormitory ON dormitory_supervisor.Supervisor_ID = dormitory.Dormitory_Supervisor_ID
                WHERE {building_condition}
            """
            print("舍监,",sql)
        elif infors == 'Tutor':
            sql = f"""
                SELECT *
                FROM Floor_Tutor
                JOIN Floor ON Floor_Tutor.Tutor_ID = Floor.Tutor_ID
                WHERE {where_clause}
            """
        elif infors == 'Student':
            sql = f"""
                SELECT *
                FROM Student
                JOIN Room ON Student.Room_ID = Room.Room_ID AND Student.Dormitory_ID = Room.Dormitory_ID AND Student.Floor_Number = Room.Floor_Number
                WHERE {where_clause}
            """
        else:
            return jsonify({'success': False, 'message': 'Invalid user type'}), 400

        cur.execute(sql)
        users = cur.fetchall()

        # 返回符合要求的用户信息
        return jsonify({'success': True, 'users': users}), 200
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