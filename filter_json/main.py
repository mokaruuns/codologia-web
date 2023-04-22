import json

with open('data.json', encoding="utf-8") as json_file:
    data = json.load(json_file)
    age = 10

    for number in data:
        if data[number]["age_min"] <= age <= data[number]["age_max"]:
            print(data[number]["action"], data[number]["time"], "часа")

