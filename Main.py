import random

print("Добро пожаловать в игру камень, ножницы, бумага!")

Player_point = 0
Computer_point = 0
option = ['камень', 'ножницы', 'бумага']

while True:
    print("Введи камень/ножницы/бумага или 1 для выхода")
    Player_input = input('').lower()
    if Player_input == "1":
        break
    if Player_input not in option:
        continue
    random_number = random.randint(0, 2)
    computer_pick = option[random_number]
    print("Компьютер выбрал:", computer_pick)

    if Player_input == 'бумага' and computer_pick == 'камень':
        print("Победа!")
        Player_point += 1
        Computer_point += 0

    elif Player_input == 'ножницы' and computer_pick == 'бумага':
        print("Победа!")
        Player_point += 1
        Computer_point += 0

    elif Player_input == 'камень' and computer_pick == 'ножницы':
        print("Победа!")
        Player_point += 1
        Computer_point += 0

    elif Player_input == computer_pick:
        print("Ничья!")
        Player_point += 0
        Computer_point += 0
    else:
        print("Проигрыш!")
        Player_point += 0
        Computer_point += 1

result = Player_point - Computer_point

print("Игра окончена")
print("Вы набрали очков =", Player_point)
print("Компьютер набрал очков =", Computer_point)
print("Ваша разница в очках с компьютером = ", result)
