# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

st_1 = 'one'
st_2 = 'onetwonine'

# первый вариант


def one_result():
    a_1 = st_1[0]
    a_2 = st_1[1]
    a_3 = st_1[2]

    sum_a_1 = 0
    sum_a_2 = 0
    sum_a_3 = 0

    for i in st_2:
        if i == a_1:
            sum_a_1 += 1
        elif i == a_2:
            sum_a_2 += 1
        elif i == a_3:
            sum_a_3 += 1
    print(f'{a_1} - {sum_a_1}, {a_2} - {sum_a_2}, {a_3} - {sum_a_3}')

# второй сокрощенный вариант


def two_result():
    print(f'{st_1[0]} - {st_2.count(st_1[0])}, {st_1[1]} - {st_2.count(st_1[1])}, {st_1[2]} - {st_2.count(st_1[2])}')


one_result()
two_result()
