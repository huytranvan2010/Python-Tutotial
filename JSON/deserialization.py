import json

# taoj tuple
anh = (8, "Q")

# chuyển Python object về JSON format
encoded_anh = json.dumps(anh)
print(encoded_anh)
# chuyển JSON format về Python object
decoded_anh = json.loads(encoded_anh)

print("Nhận được list từ tuple ban đầu: ", decoded_anh)