# Программа высчитывает Индекс Массы Тела по введённым параметрам: вес и рост.

print('Введите Ваш вес в килограммах: ')
weight = int(input())

print('Введите Ваш рост в сантиметрах: ')
hight = int(input())

bmi = weight/(hight/100)**2
print('Ваш индекс массы тела:', bmi)

STEPS = 40
scale = '10' + "=" * (round(bmi) - 10) + '|' + "="*(STEPS - (round(bmi) - 10)) + '50'
print(scale) 