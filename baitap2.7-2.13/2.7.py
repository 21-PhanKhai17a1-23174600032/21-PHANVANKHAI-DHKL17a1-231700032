#khaideptraichuanbicode
import json

# Dữ liệu JSON (chuỗi)
json_data = '''
{
    "name": "Khải",
    "age": 20,
    "city": "Hà Giang",
    "hobbies": ["reading", "traveling", "swimming"]
}
'''

# Chuyển đổi JSON thành đối tượng Python (dict)
python_object = json.loads(json_data)

# In đối tượng Python
print(python_object)

# Truy cập vào các giá trị trong đối tượng Python
print("Name:", python_object["name"])
print("Age:", python_object["age"])
print("City:", python_object["city"])
print("Hobbies:", python_object["hobbies"])