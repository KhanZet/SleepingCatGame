import os
import json

def getHeroData():
    try:
        with open('session/data.json', 'r', encoding='utf-8') as f:
            loaded_data = json.load(f)
            return loaded_data
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def getHeroStat():
    try:
        with open('session/character_statistics.json', 'r', encoding='utf-8') as f:
            # return json.dumps(json.load(f), indent=4, ensure_ascii=False)
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, Exception) as e:
        print(f"Произошла ошибка: {e}")
    return None



def pushHeroData(data):
    with open('session/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def pushHeroStats(data):
    with open('session/character_statistics.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
print(getHeroStat()['Сила'])
