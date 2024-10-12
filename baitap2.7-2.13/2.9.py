#khaideptraichuanbicode
import json

# Example Python object (dictionary)
python_object = {
    "name": "Khai",
    "age": 19,
    "city": "vietnam",
    "job": "Data Engineer"
}

json_data = json.dumps(python_object, sort_keys=True, indent=4)

# Print  JSON data
print(json_data)