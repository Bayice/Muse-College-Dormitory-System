import requests

url = 'http://127.0.0.1:5000/authenticate'
data = {'id': '120001187', 'password': '123'}
response = requests.post(url, json=data)

print(response.json())


# 请求的URL
url = 'http://127.0.0.1:5000/search_rooms'

# 请求的数据
data = {
    'floors': [1, 2, 3, 4],  # 选择的楼层列表
    'buildings': ['"MuseCollege-A"', '"MuseCollege-B"'],  # 选择的楼栋列表
    'room_type': 'A',  # 房间类型
    'student_type': '本科生',  # 学生类型（可选）
    'gender': '男',  # 性别（可选）
}

# 发送POST请求
response = requests.post(url, json=data)

# 解析响应
if response.status_code == 200:

    rooms = response.json()['rooms']
    for room in rooms:
        print(room)  # 在控制台输出房间信息
else:
    print('Error:', response.status_code)
    print(response.json())  # 输出错误信息






























# # 用户ID
# user_id = '1'

# # 请求数据
# data = {'id': user_id}

# # 发送请求
# response = requests.post('http://127.0.0.1:5000/user_info', json=data)

# # 打印响应
# print(response.json())