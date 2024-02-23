import json
import os

# Console Functions


def cln():
    os.system('cls' if os.name == 'nt' else 'clear')

# Wrapping in a Border with any two symbols


def frameMsg(msg, firstSymbol, secondSymbol):
    lineMsg = (firstSymbol + secondSymbol) * int(len(msg) / 1.5)
    if list(lineMsg)[-1] == secondSymbol:
        lineMsg += firstSymbol
    spaceLen = (len(lineMsg) - len(msg) - 2) // 2
    outputMessage = firstSymbol + ' ' * spaceLen + msg + spaceLen * ' '
    if len(outputMessage) % 2 == 1:
        outputMessage += ' ' + firstSymbol
    else:
        outputMessage += firstSymbol
    print(lineMsg)
    print(outputMessage)
    print(lineMsg)
# DATA FUNCTIONS


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
            loaded_data = json.load(f)
            return loaded_data
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def pushHeroData(data):
    with open('session/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def pushHeroStats(data):
    with open('session/character_statistics.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


print(getHeroData())


class SleepingCatGame:
    def __init__(self):
        self.success = False

    def start_game(self):
        cln()
        print("      |\\      _,,,---,,_")
        print("ZZZzz /,`.-'`'    -.  ;-;;,_")
        print("     |,4-  ) )-,_. ,\\ (\\")
        print("    '---''(_/--'  `-'\\_)")
        frameMsg("Добро пожаловать в комнату спящего Котика", '*', '-')
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
            except ValueError as e:
                print("введен неверный тип данных")

    def play_game(self):
        heroData = getHeroData()
        if(heroData is not None):
            print(f"С возращением, {heroData['name']}!")
            print(f"Твой персонаж {heroData['race']} с классом {heroData['class']}")
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
        pushHeroData({
            'name': chosen_name,
            'race': chosen_race,
            'class': chosen_class
        })
        cln()
        print(f"\nВы выбрали {chosen_race} класса {chosen_class} под именем {chosen_name}. Игра начинается.")

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

    def get_choice(self, options_count):
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
        self.heroData = getHeroData()


if __name__ == "__main__":
    game = SleepingCatGame()
    game.start_game()
