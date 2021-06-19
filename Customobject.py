import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age 


user = User('Max', 27)

"""
Serializarion thông thường sẽ báo lỗi như này
TypeError: Object of type User is not JSON serializable
"""
# userJSON = json.dumps(user)

# cần viết custom encoding function
def encode_user(o):
    if isinstance(o, User):     # kiểm tra o có phải instance của class User không
        return {'name': o.name, 'age': o.age, o.__class__.__name__:True}   # nếu có trả về dict
    else:
        raise TypeError("Object of type User is not JSON serializable")

userJSON = json.dumps(user, default=encode_user)
print(userJSON)

""" Cách 2: custom JSONEncoder """
from json import JSONEncoder

class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__:True}
        return JSONEncoder.default(self, o)

userJSON = json.dumps(user, cls=UserEncoder)

# hoặc dùng thẳng luôn
userJSON = UserEncoder().encode(user)
print(userJSON)

