import requests

url = 'http://127.0.0.1:5000/authenticate'
data = {'id': '120001187', 'password': '123'}
response = requests.post(url, json=data)

print(response.json())

































# # 用户ID
# user_id = '1'

# # 请求数据
# data = {'id': user_id}

# # 发送请求
# response = requests.post('http://127.0.0.1:5000/user_info', json=data)

# # 打印响应
# print(response.json())