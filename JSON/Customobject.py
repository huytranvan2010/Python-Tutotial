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
            return {'name': o.name, 'age': o.age, o.__class__.__name__:True}    # cái cuối là User class name (trick để tí decode)
        return JSONEncoder.default(self, o)

userJSON = json.dumps(user, cls=UserEncoder)

# hoặc dùng thẳng luôn
userJSON = UserEncoder().encode(user)
print(userJSON)

""" Muốn decode thì sao (deserialization) """
# Khi decode trở lại sẽ nhận được dictionary chứ không phải object như ta mong muốn
# ko dùng được như user.name, do đó cần viết custom decoding method
user = json.loads(userJSON)
print(user)
print(type(user))

def decode_user(dct):
    if User.__name__ in dct:   # tìm tên class User có thuộc keys của dict không
        return User(name=dct['name'], age=dct['age'])
    return dct 

user = json.loads(userJSON, object_hook=decode_user)
print(user.name)
print(user)
