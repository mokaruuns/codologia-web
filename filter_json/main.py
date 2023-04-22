import json

with open('data.json', encoding="utf-8") as json_file:
    data = json.load(json_file)


def filter_by_age(age=18):
    result = []
    for number in data:
        if data[number]["age_min"] <= age <= data[number]["age_max"]:
            result.append(data[number])
    return result


def filter_by_category(category):
    result = []
    for number in data:
        if data[number]['category'] == category:
            result.append(data[number])
    return result


def print_data(lst):
    for i in lst:
        print("Действие:", i['action'])
        print('Возрастной промежуток:', i['age_min'], '-', i['age_max'])
        print('Время:', i['time'])
        print()


print_data(filter_by_age())

print(filter_by_category("спорт"))
