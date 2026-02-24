import json

# 1
json_string = '{"name": "John", "age": 30, "city": "New York"}'
python_dict = json.loads(json_string)

print("Python Dictionary name:", python_dict["name"])

# 2
user_data = {
    "id": 101,
    "username": "coder_pro",
    "is_active": True,
    "skills": ["Python", "C++", "Linux"]
}

# 'indent=4' makes the JSON readable
json_output = json.dumps(user_data, indent=4)
print("Converted JSON:\n", json_output)

# 3
with open("user.json", "w") as file:
    json.dump(user_data, file, indent=4)
    print("\nData successfully saved to user.json")