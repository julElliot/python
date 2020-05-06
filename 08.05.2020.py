# Программа высчитывает Индекс Массы Тела по введённым параметрам: вес и рост. Даёт рекомендации исходя из результата bmi.
STEPS = 40
users = []

while True:
    print('Введите ФИО: ')
    user_name = input()

    print('Введите Ваш вес в килограммах: ')
    weight = int(input())

    print('Введите Ваш рост в сантиметрах: ')
    hight = int(input())

    bmi = weight/(hight/100)**2
    
    print('Ваш индекс массы тела:', bmi)

    scale = '10' + "=" * (round(bmi) - 10) + '|' + "="*(STEPS - (round(bmi) - 10)) + '50'
    print(scale)
    print()

    user = {'имя': user_name,
            'вес': weight,
            'рост': hight,
            'bmi': bmi}
    
    users.append(user) 

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

    for temp_user in users:
        print(temp_user['имя'], temp_user['вес'], 'кг ', temp_user['рост'], 'см', ' bmi: ', temp_user['bmi'])
    print()
    
