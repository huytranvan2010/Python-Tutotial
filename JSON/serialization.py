import json

data = {
    "user": {
        "name": "Huy",
        "age": 30
    }
}

# lưu file JSON bên ngoài
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4)   #  theem indent nhìn dexw hơn

# chuyển thành string JSON
json_str = json.dumps(data)
print(json_str)

import json
print("From dict: ", json.dumps({'name': "Huy", 'age': 30}))
print("From list: ", json.dumps(["1", "a"]))
print("From tuple: ", json.dumps(('anh', 'em')))
print("From string: ",json.dumps("Hello"))
print("From int: ",json.dumps(100))
print("From float: ", json.dumps(23.8))
print("From True: ", json.dumps(True))
print("From False: ", json.dumps(False))
print("From None: ", json.dumps(None))