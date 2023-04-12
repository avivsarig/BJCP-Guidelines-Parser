import json


def pretty_print(data, indent=0):
    if isinstance(data, dict):
        for key, value in data.items():
            print(" " * indent + f"{key}:")
            pretty_print(value, indent + 2)
    elif isinstance(data, list):
        for item in data:
            pretty_print(item, indent)
    else:
        print(" " * indent + str(data))


def save_to_json(data, file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)
