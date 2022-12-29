# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]


n = int(input('Введите значение N: '))
elements = [c for c in range(-n, n+1)]


def shift(elements, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            elements.append(elements.pop(0))
    else:
        for i in range(steps):
            elements.insert(0, elements.pop())


shift(elements, 2)
print(elements)
