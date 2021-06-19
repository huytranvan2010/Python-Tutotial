import json

# JSON string
employee = '{"id": "09", "name": "Huy", "address": "Me Nhu"}'

# Chuyển từ JSON string sang Python dict
employee_dict = json.loads(employee)
print(employee_dict)
print(type(employee_dict))

# Chuyển từ Python dict to JSON
json_object = json.dumps(employee_dict, indent=4)
print(json_object)
print(type(json_object))