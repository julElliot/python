# Программа высчитывает Индекс Массы Тела по введённым параметрам: вес и рост. Даёт рекомендации исходя из результата bmi.

STEPS = 40
users = []

def getAdvise(bmi, user):
    if bmi <= 16:
        print(user['имя'],', у Вас выраженный дефицит массы тела! Следует обратиться к врачу!')
    elif bmi < 18.5:
        print(user['имя'],', у Вас дефицит массы тела! Следует набрать пару киллограммов.')
    elif bmi < 25:
        print(user['имя'],', Ваша масса тела в норме')
    elif bmi < 30:
        print(user['имя'],', у Вас предожирение! Хватит кушать булочки на ночь!')
    elif bmi < 35:
        print(user['имя'],', у Вас ожирение! Записываемся в спортзал и садимся на диету!')
    elif bmi >= 35:
        print(user['имя'],', у Вас резкое ожирение! Немедленно обратитесь к врачу!')
    print()

def outputUsers(users):
    for temp_user in users:
        print(temp_user['имя'], temp_user['вес'], 'кг ', temp_user['рост'], 'см', ' bmi: ', temp_user['bmi'])
    print()

def printScale(bmi):
    scale = '10' + "=" * (round(bmi) - 10) + '|' + "="*(STEPS - (round(bmi) - 10)) + '50'
    print(scale)
    print()

def calcBMI(weight, hight):
    bmi = weight/(hight/100)**2
    print('Ваш индекс массы тела:', bmi)
    return bmi

def inputData():
    print('Введите ФИО: ')
    user_name = input()
    print('Введите Ваш вес в килограммах: ')
    weight = int(input())
    print('Введите Ваш рост в сантиметрах: ')
    hight = int(input())
    return user_name, weight, hight

def addUser(user_name, weight, hight, bmi):
    global users
    user = {'имя': user_name,
            'вес': weight,
            'рост': hight,
            'bmi': bmi}
    users.append(user)

def main():
    while True:
        user_name, weight, hight = inputData()
        bmi = calcBMI(weight, hight)
        printScale(bmi)
        addUser(user_name, weight, hight, bmi)
        getAdvise(bmi, users[len(users)-1])

        action = 0
        while action != 2:
            print('1 - вывести список пользователей\n2 - продолжить программу ')
            action = int(input())
            if action == 1:
                outputUsers(users)


if __name__ == "__main__":
    main()