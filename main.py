import json
import os


# Console Functions


def cln():
    os.system('cls' if os.name == 'nt' else 'clear')


# Text formatting functions>>>>

# Giving max length of pairs in dictionary in string type
def get_max_length(data):
    max_length = 0
    for key, value in data.items():
        current_length = 0
        if isinstance(value, dict):
            current_length = len(f"{key}: {value['current']}/{value['max']}")
        elif isinstance(value, list):
            pass
        else:
            current_length = len(f"{key}: {value}")
        if current_length > max_length:
            max_length = current_length
    return max_length


# Formatting each line to needed format
def format_string(data_stat, window_width):
    total_string = ""
    current_length = 0
    formatted_value = ""
    for key, value in data_stat.items():
        if isinstance(value, dict):
            current_length = len(f"{key}: {value['current']}/{value['max']}")
            formatted_value = f"{key}: {value['current']}/{value['max']}"
        elif isinstance(value, list):
            pass
        else:
            current_length = len(f"{key}: {value}")
            formatted_value = f"{key}: {value}"
        space_padding = " " * (window_width - current_length + 1)
        total_string += f"║ {formatted_value}{space_padding}║\n"
    return "\n".join(total_string.strip().split('\n')[:-1]) + "\n"


# Contain list of words in window width with format

def move_words(dict_name, words_list, window_width):
    total_string = f"║ {dict_name}: "
    if not words_list:
        words_list.append("Отсутствуют")
    current_line_length = len(total_string) - 2
    for word in words_list:
        word_length = len(word) + 2
        if current_line_length + word_length > window_width:
            total_string += f"{" " * (window_width - current_line_length + 1)}║"
            total_string += "\n"
            current_line_length = 0
        if current_line_length == 0:
            total_string += "║ "
        total_string += word + ', '
        current_line_length += word_length
    return total_string[:-2] + f"{" " * (window_width - current_line_length + 3)}║\n"


# Main function that return total string to print

def stat_msg(data_hero, data_stat):
    window_name = f"Статистика {data_hero['name']}"
    window_width = 0
    print(get_max_length(data_stat))
    if get_max_length(data_stat) > len(window_name):
        window_width = get_max_length(data_stat)

    else:
        window_width = len(window_name)
    simple_line = f"╠{'═' * (window_width + 2)}╣\n"
    first_line = f"╔{'═' * (window_width + 2)}╗\n"
    second_line = f"║ {window_name + " " * (window_width - len(window_name))} ║\n"
    last_line = f"╚{'═' * (window_width + 2)}╝"
    msg_array = [first_line, second_line, simple_line, format_string(data_stat, window_width),
                 move_words("Заклинания", data_stat["Заклинания"], window_width), last_line]
    return "".join(msg_array)


def frame_msg(msg, first_symbol, second_symbol):
    line_msg = (first_symbol + second_symbol) * int(len(msg) / 1.5)
    if list(line_msg)[-1] == second_symbol:
        line_msg += first_symbol
    space_len = (len(line_msg) - len(msg) - 2) // 2
    output_message = first_symbol + ' ' * space_len + msg + space_len * ' '
    if len(output_message) % 2 == 1:
        output_message += ' ' + first_symbol
    else:
        output_message += first_symbol
    print(line_msg)
    print(output_message)
    print(line_msg)


# =======================================================================================================================

# DATA FUNCTIONS

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
            loaded_data = json.load(f)
            return loaded_data
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def push_hero_data(data):
    with open('session/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def push_hero_stats(data):
    with open('session/character_statistics.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# ================================================================================================================

# Game Classes

class SleepingCatGame:
    def __init__(self):
        self.success = False

    def start_game(self):
        cln()
        print("      |\\      _,,,---,,_")
        print("ZZZzz /,`.-'`'    -.  ;-;;,_")
        print("     |,4-  ) )-,_. ,\\ (\\")
        print("    '---''(_/--'  `-'\\_)")
        frame_msg("Добро пожаловать в комнату спящего Котика", '*', '-')
        print("[1] Играть\n[2] Выйти")
        while not self.success:
            try:
                start_answer = int(input("Пожалуйста, сделайте выбор\n"))
                if start_answer == 1:
                    cln()
                    self.play_game()
                elif start_answer == 2:
                    cln()
                    self.exit_game()
                else:
                    print(
                        'Неправильное число. Пожалуйста выберите 1 для игры, и 2 для выхода из игры')
            except ValueError:
                print("введен неверный тип данных")

    def play_game(self):
        hero_data = get_hero_data()
        if hero_data is not None:
            print(f"С возращением, {hero_data['name']}!")
            print(f"Твой персонаж {hero_data['race']} с классом {hero_data['class']}")
            print('Желаешь продолжить, или начать заново?')
            print('[1] Продолжить\n[2] Начать заново\n')
            choice = int(input())
            if choice == 1:
                cln()
                print('Вперед к приключениям')
                self.success = True
                return
            elif choice == 2:
                self.start_new_game()
            else:
                cln()
                print('Не знаю такого варианта')
                self.success = True
                return

        else:
            cln()
            print('Приветствуем нового героя.')
            self.start_new_game()
        self.success = True

    def start_new_game(self):
        cln()
        print('Выбор за тобой!')
        choosing_hero = ChoosingHero()
        chosen_race, chosen_class, chosen_name = choosing_hero.choose_hero()
        initial_attributes = {
            "Воин": {
                "Сила": 4,
                "Ловкость": 3,
                "Мудрость": 2,
                "Интеллект": 1,
                "Выносливость": 6
            },
            "Маг": {
                "Сила": 1,
                "Ловкость": 2,
                "Мудрость": 5,
                "Интеллект": 6,
                "Выносливость": 2
            },
            "Паладин": {
                "Сила": 3,
                "Ловкость": 2,
                "Мудрость": 4,
                "Интеллект": 4,
                "Выносливость": 3
            },
            "Лучник": {
                "Сила": 2,
                "Ловкость": 5,
                "Мудрость": 2,
                "Интеллект": 3,
                "Выносливость": 4
            },
            "Некромант": {
                "Сила": 2,
                "Ловкость": 2,
                "Мудрость": 6,
                "Интеллект": 5,
                "Выносливость": 3
            },
            "Друид": {
                "Сила": 3,
                "Ловкость": 3,
                "Мудрость": 5,
                "Интеллект": 4,
                "Выносливость": 3
            },
            "Шаман": {
                "Сила": 2,
                "Ловкость": 4,
                "Мудрость": 4,
                "Интеллект": 3,
                "Выносливость": 3
            }
        }
        hero_stat = initial_attributes[chosen_class]
        push_hero_stats({
            'Имя': chosen_name,
            'Уровень': 1,
            'Здоровье': {
                "current": hero_stat['Выносливость'] * 10,
                "max": hero_stat['Выносливость'] * 10
            },
            'Мана': {
                "current": hero_stat['Интеллект'] * 10,
                "max": hero_stat['Интеллект'] * 10
            },
            'Опыт': {
                'current': 0,
                'max': 1000
            },
            'Сила': hero_stat['Сила'],
            'Ловкость': hero_stat['Ловкость'],
            'Мудрость': hero_stat['Мудрость'],
            'Интеллект': hero_stat['Интеллект'],
            'Выносливость': hero_stat['Выносливость'],
            'Золото': 0,
            'Заклинания': [],
        })
        push_hero_data({
            'name': chosen_name,
            'race': chosen_race,
            'class': chosen_class
        })
        cln()
        print(f"\nВы выбрали {chosen_race} класса {chosen_class} под именем {chosen_name}. Игра начинается.")
        answer = input("Выберите действия [1] Статистика [2] Выйти из игры\n")
        if answer == '1':
            print(stat_msg(get_hero_data(), get_hero_stat()))
        elif answer == '2':
            self.success = True

    def exit_game(self):
        print('Exiting game.')
        self.success = True
        return


class ChoosingHero:
    def __init__(self):
        self.cats = ["Кот-Сфинкс", "Кот-Манул", "Кот-Барсик", "Кот-Великан"]
        self.classes = ["Воин", "Маг", "Паладин",
                        "Лучник", "Некромант", "Друид", "Шаман"]

    def choose_hero(self):
        print("Выберите вашего кота:")

        for idx, cat in enumerate(self.cats, start=1):
            print(f"[{idx}] {cat}")
        cat_choice = self.get_choice(len(self.cats))
        chosen_race = self.cats[cat_choice - 1]
        cln()
        print("\nТеперь выберите класс для вашего кота:")
        for idx, cls in enumerate(self.classes, start=1):
            print(f"[{idx}] {cls}")
        class_choice = self.get_choice(len(self.classes))
        chosen_class = self.classes[class_choice - 1]
        cln()
        chosen_name = input('\nКак зовут героя?\n')
        return chosen_race, chosen_class, chosen_name

    @staticmethod
    def get_choice(options_count):
        choice = 0

        while choice < 1 or choice > options_count:
            try:
                choice = int(input("Введите номер выбора: "))
                if choice < 1 or choice > options_count:
                    print(f"Пожалуйста, введите число от 1 до {options_count}")
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите число")
        return choice


class Scene:
    """docstring for Scene"""

    def __init__(self):
        self.hero_data = get_hero_data()


# =========================================================================

if __name__ == "__main__":
    game = SleepingCatGame()
    game.start_game()
