import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# convert into JSON, nếu để mặc định hơi khó nhìn
person_json = json.dumps(person)

# use different formatting style, chỉnh sửa chút cho dễ nhìn nào
# nên dùng sort_keys=True, bt mặc định là False để sắp xếp các keys theo alphabet, indent số khoảng trắng thụt dòng
# ở đây không khuyến khích dùng separators (dạng tuple), "; " sẽ thay ", ", "= " sẽ thay ": "
person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)

# the result is a JSON string:
print(person_json) 
print(person_json2) 

with open('person.json', 'w') as f:
    json.dump(person, f, indent=4)      # nên để indent=4 cho dễ nhìn