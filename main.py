from random import randint


def attack(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} нанёс урон противнику равный {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон противнику равный {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс урон противнику равный {5 + randint(-3, -1)}')
def defence(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')

def special(char_name, char_class):
    if char_class == 'warrior': 
        return (f'{char_name} применил специальное умение' f'"Выносливость"{80 + 25}')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение «Атака»')
    if char_class == 'healer':
        return (f'{char_name} не применил специальное умение')


def start_training(char_name, char_class):
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('attack — атака, defence — блокировка, special — сила.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Название персонажа: warrior, mage, healer:=14')
        if char_class == 'warrior':
            print('Воитель — воин ближнего боя. Сильный, выносливый.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. Высокий интеллект.')
        if char_class == 'healer':
            print('Лекарь — Заклинатель. Черпает силы из природы, духов.')
        approve_choice = input('(Y) - подтвердить выбор. Любую другую кнопку - выбрать другого персонажа').lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))
    

main()