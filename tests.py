import os
import json


def get_hero_data():
    try:
        with open('session/data.json', 'r', encoding='utf-8') as f:
            loaded_data = json.load(f)
            return loaded_data
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def get_hero_stat():
    try:
        with open('session/character_statistics.json', 'r', encoding='utf-8') as f:
            # return json.dumps(json.load(f), indent=4, ensure_ascii=False)
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, Exception) as e:
        print(f"Произошла ошибка: {e}")
    return None


def push_hero_data(data):
    with open('session/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def push_hero_stats(data):
    with open('session/character_statistics.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


print(get_hero_stat()['Сила'])
