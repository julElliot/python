def number_generator():
    value = 1
    while True:
        if value % 3 == 0:
            yield 'Василий'
        else:
            yield value
        value += 1

# цикл для проверки работоспособности генератора
for number in number_generator():
    print(number)
    if number == 10:
        break
