import json


def read(str_path):
    file = open(str_path, "r")
    data = json.load(file)
    file.close()

    return data


def update(str_path, data):
    file = open(str_path, "w+")
    result = file.write(json.dumps(data))
    file.close()

    return result
