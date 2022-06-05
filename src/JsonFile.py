import json


def read(strPath):
    file = open(strPath, "r")
    data = json.load(file)
    file.close()

    return data


def update(strPath, data):
    file = open(strPath, "w+")
    result = file.write(json.dumps(data))
    file.close()

    return result
