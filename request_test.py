import requests



# # 舍监查看整楼的URL
# url = 'http://127.0.0.1:5000/view_building'

# # 请求的数据
# data = {
#     'Dormitory_Supervisor_ID': '1',   # 舍监ID
#     'floors': [2,3],  # 选择的楼层列表
#     'infors': ['Tutor'],  # 用户类型（'Dormitory_Supervisor', 'Tutor', 'Student'）
# }
# # 发送POST请求
# response = requests.post(url, json=data)

# print(response.json())


# # Admin查看请求的URL
# url = 'http://127.0.0.1:5000/admin_query'

# # 请求的数据
# data = {
#     'buildings': ['MuseCollege-A'],  # 选择的楼栋列表
#     'floors': [2,3],  # 选择的楼层列表
#     'infors': ['Student'],  # 用户类型（'Dormitory_Supervisor', 'Tutor', 'Student'）
# }

# # 发送POST请求
# response = requests.post(url, json=data)

# # 解析响应
# if response.status_code == 200:
#     users = response.json()['users']
#     for user in users:
#         print(user)  # 在控制台输出用户信息
# else:
#     print('Error:', response.status_code)
#     print(response.json())  # 输出错误信息

# 请求的URL
url = 'http://127.0.0.1:5000/LLM'

# 请求的数据
data = {
    'input_string': '请帮我选一个合适的宿舍吧！'  # 要处理的字符串
}

# 发送 POST 请求
response = requests.post(url, json=data)

# 输出响应
if response.status_code == 200:
    processed_string = response.text
    print("处理后的字符串:", processed_string)
else:
    print('请求失败:', response.status_code)




# # 用户认证请求的URL
# url = 'http://127.0.0.1:5000/authenticate'
# data = {'id': '121', 'password': '12345'}
# response = requests.post(url, json=data)

# print(response.json())



# 房间搜索请求的URL
# url = 'http://127.0.0.1:5000/search_rooms'

# 请求的数据
# data = {
#     'floors': [1, 2, 3, 4],  # 选择的楼层列表
#     'buildings': ['MuseCollege-A', 'MuseCollege-B'],  # 选择的楼栋列表
#     'room_type': ['上床下桌','上下铺'],  # 房间类型
#     'student_type': '本科生',  # 学生类型（可选）
#     'gender': '女',  # 性别（可选）
# }

# # 发送POST请求
# response = requests.post(url, json=data)

# # 解析响应
# if response.status_code == 200:

#     rooms = response.json()['rooms']
#     for room in rooms:
#         print(room)  # 在控制台输出房间信息
# else:
#     print('Error:', response.status_code)
#     print(response.json())  # 输出错误信息



# # 更改房间tag请求的URL
# url = 'http://127.0.0.1:5000/change_tag'

# # 请求的数据
# data = {
#     'Room_ID': 'A202',  # 房间ID
#     'New_Room_Tag': '不睡不起',  # 新的房间tag
# }
# # 发送POST请求
# response = requests.post(url, json=data)

# print(response.json())







# # tutor查看某楼层的URL
# url = 'http://127.0.0.1:5000/view_floor'

# # 请求的数据
# data = {
#     'Tutor_ID': '12004',  # 舍监ID
# }
# # 发送POST请求
# response = requests.post(url, json=data)

# print(response.json())


# 查看某个room的URL
# url = 'http://127.0.0.1:5000/view_room'

# # 请求的数据
# data = {
#     'Room_ID':'C709',  # 房间ID
# }
# # 发送POST请求
# response = requests.post(url, json=data)

# print(response.json())



# # 添加学生到宿舍
# url = 'http://127.0.0.1:5000/AddAStudent'
# student_data = {
#     'id': '122869882',  # 学生ID
#     'dormitory': 'C709C',  # 学生选的宿舍
# }
# response = requests.post(url, json=student_data)
# print(response.json())  




# # 请求的URL
# url = 'http://127.0.0.1:5000/update_student_introduction'

# # 请求的数据
# data = {
#     'id': '120001187',  # 学生ID
#     'introduction': '我是一个来自中国的本科生。'  # 学生自我介绍
# }

# # 发送POST请求
# response = requests.post(url, json=data)

# # 解析响应
# if response.status_code == 200:
#     print(response.json())  # 输出成功信息
# else:
#     print('Error:', response.status_code)
#     print(response.json())  # 输出错误信息





















# # 用户ID
# user_id = '1'

# # 请求数据
# data = {'id': user_id}

# # 发送请求
# response = requests.post('http://127.0.0.1:5000/user_info', json=data)

# # 打印响应
# print(response.json())