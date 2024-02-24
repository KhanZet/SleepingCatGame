import json


def frame_msg(msg, first_symbol, second_symbol):
    line_msg = (first_symbol + second_symbol) * int(len(msg) / 1.5)
    if list(line_msg)[-1] == second_symbol:
        line_msg += first_symbol
    spaceLen = (len(line_msg) - len(msg) - 2) // 2
    outputMessage = first_symbol + ' ' * spaceLen + msg + spaceLen * ' '
    if len(outputMessage) % 2 == 1:
        outputMessage += ' ' + first_symbol
    else:
        outputMessage += first_symbol
    return f"{line_msg} + \n + {outputMessage} + \n + {line_msg}"



def get_hero_stat():
    try:
        with open('session/character_statistics.json', 'r', encoding='utf-8') as f:
            loaded_data = json.load(f)
            return loaded_data
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def get_hero_data():
    try:
        with open('session/data.json', 'r', encoding='utf-8') as f:
            loaded_data = json.load(f)
            return loaded_data
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def get_max_length(data):
    max_length = 0
    for key, value in data.items():
        current_length = 0
        if type(value) == dict:
            current_length = len(f"{key}: {value["current"]}/{value['max']}")
        elif type(value) == list:
            pass
        else:
            current_length = len(f"{key}: {value}")
        if current_length > max_length:
            max_length = current_length
    return max_length

def stat_msg(data_hero, data_stat):
    window_name = f'Статистика {data_hero['name']}'
    window_width = 0
    if get_max_length(data_stat) > len(window_name):
        window_width = get_max_length(data_stat)
    else:
        window_width = len(window_name)
    print(window_name, window_width)
    simple_line = f"╠{'═'*(window_width+2)}╣"
    first_line = f"╔{'═'*(window_width+2)}╗"
    second_line = f"║ {window_name} ║"
    print(first_line)
    print(second_line)
    print(simple_line)
stat_msg(get_hero_data(), get_hero_stat())

print(get_hero_stat())
def format_string(data_stat, window_witdh):
    total_string = ""
    for key, value in data_stat.items():
        if type(value) == dict:
            string_lentgh = len(f"{key}: {value["current"]}/{value['max']}")
            total_string += f"║ {key}: {value["current"]}/{value['max']}{" " * (window_witdh-string_lentgh+5)}║\n"
        elif type(value) == list:
            pass
        else:
            string_lentgh = len(f"{key}: {value}")
            total_string += f"║ {key}: {value}{" " * (window_witdh-string_lentgh+5)}║\n"
    print(total_string[:-1])
    return total_string[:-1]

format_string(get_hero_stat(), 15)


def move_words(dict_name, words_list, window_width):
    # Начинаем строку с имени словаря и двоеточия для заголовка.
    total_string = f"{dict_name}: "
    # Изначально текущая длина строки равна длине начальной строки.
    current_line_length = len(total_string)

    # Проходим по каждому слову в списке слов.
    for word in words_list:
        # Вычисляем длину текущего слова, добавляя 1 для пробела после слова.
        word_length = len(word) + 1  # +1 для учета пробела между словами

        # Проверяем, превысит ли добавление текущего слова максимально допустимую ширину строки.
        if current_line_length + word_length > window_width:
            # Если слово не помещается, начинаем новую строку.
            total_string += "\n"  # Добавляем символ новой строки для переноса.
            current_line_length = 0  # Сбрасываем длину текущей строки, так как мы начали новую.

        # Добавляем текущее слово к строке, включая пробел после него.
        total_string += word + " "
        # Обновляем длину текущей строки, добавляя длину только что добавленного слова.
        current_line_length += word_length

    # Возвращаем сформированную строку после добавления всех слов.
    return total_string


# Пример использования функции с конкретными значениями.
dict_name = "Словарь"
words_list = ["это", "пример", "списка", "слов", "которые", "должны", "поместиться", "в", "окно"]
window_width = 20

# Вызываем функцию и печатаем результат ее работы.
formatted_string = move_words(dict_name, words_list, window_width)
print(formatted_string)



