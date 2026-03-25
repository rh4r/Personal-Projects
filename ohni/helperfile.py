import json

FILE_PATH = "data.json"


def load_data():
    with open(FILE_PATH, "r") as f:
        return json.load(f)


def save_data(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)


data = load_data()

filter_list = data["filter_list"]
command_list = data["command_list"]


def add_word(word: str):
    word = word.lower()
    if word not in filter_list:
        filter_list.append(word)
        save_data(data)
        return True
    return False


def remove_word(word: str):
    word = word.lower()
    if word in filter_list:
        filter_list.remove(word)
        save_data(data)
        return True
    return False
