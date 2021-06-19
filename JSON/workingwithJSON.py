import json
import requests

# request JSON data through the API package
response = requests.get("https://jsonplaceholder.typicode.com/todos")

""" 
Để nhận được Python list từ JSON data, tạo variable mới todos
response.text trả về nội dung của web request là là string chứa JSON data
Ở đây dùng loads() vì chúng ta đang đọc từ string ko phải từ file
"""
todos = json.loads(response.text)

print(type(todos))
print(todos[:2])

# tạo dictionary
todos_by_user = dict()  # keys là userId, values là số tasks đã completed

# duyệt qua các todo
for todo in todos:
    if todos_by_user.get(todo['userId']) is None:   # mặc định không có trả về None
        todos_by_user[todo['userId']] = 0
        if todo['completed'] == True:
            todos_by_user[todo['userId']] += 1

    else:
        if todo['completed'] == True:
            todos_by_user[todo['userId']] += 1

print(todos_by_user)

# chuyển về list of tuple
new_list = [(key, value) for key, value in todos_by_user.items()]
print(new_list)

# Sắp xếp list theo chiều giảm của số task hoàn thành
sorted_list = sorted(new_list, key=lambda x: x[1], reverse=True)
print(sorted_list)

# số lượng task hoàn thành nhiều nhất
max_complete = sorted_list[0][1]
print(max_complete)

# số lượng user hoàn thành tasks = max_complete
count = 0
user_list = []
for user, num_complete in sorted_list:
    if num_complete < max_complete:
        break   # vì mình sắp xếp giảm dần nên không cần kiểm tra nữa
    else:
        user_list.append(user)
        count += 1
print("Number of user completed {} tasks: {}".format(max_complete, count) + ". They are: ", user_list)
