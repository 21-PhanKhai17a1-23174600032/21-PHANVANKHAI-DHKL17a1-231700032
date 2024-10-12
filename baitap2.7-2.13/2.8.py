#khaideptraichuanbicode
import json

# Tạo đối tượng Python (dict)
python_object = {
    "name": "Khai",
    "age": 19,
    "city": "Vietnam",
    "hobbies": ["painting", "hiking", "dancing"]
}

# Chuyển đổi đối tượng Python thành chuỗi JSON
json_string = json.dumps(python_object, indent=4)

# In chuỗi JSON
print("Chuỗi JSON:")
print(json_string)

# In từng giá trị trong đối tượng Python
print("\nTất cả các giá trị trong đối tượng Python:")
for key, value in python_object.items():
    print(f"{key}: {value}")