# 1
# ввод целого числа
d = int(input())
# здесь продолжите программу
print(abs(d))

# 2
# ввод целого числа
d1, d2, d3, d4, d5 = map(int, input().split())
# здесь продолжите программу
print(min(d1, d2, d3, d4, d5))


# 3
# ввод целого числа
d1, d2, d3, d4, d5 = map(int, input().split())
# здесь продолжите программу
print(max(d1, d2, d3, d4, d5))


# 4
import math

# ввод данных
a, b = map(int, input().split())
# здесь продолжите программу
print(round(math.sqrt((a**2) + (b**2)), 2))

# 5
from math import factorial as f

# ввод данных
n, k = map(int, input().split())
# здесь продолжите программу
result = f(n) / (f(k) * f(n - k))
print(int(result))

# 6
# ввод данных
n, m = map(int, input().split())
# здесь продолжите программу
result = n // 20 + 1
print(result)


# 7
# ввод данных
x = int(input())
# здесь продолжите программу
print(int(500 // (x * 0.9)))


# 8
# put your python code here
a = 7
b = -4
c = 3
print(a, b, c)

# 9
# put your python code here

a = 7
b = -4
c = 3
print(a, b, c, sep="\n")

# 10
# put your python code here
s1, s2 = "Hello", "Balakirev"

print(s1, end=" ")
print(s2)

# 11
# ввод данных
s1, s2 = map(str.strip, input().split())
# здесь продолжите программу
print(f"Word 1: {s1} | Word 2: {s2}")

# 12
# put your python code here
s1, s2 = map(int, input().split())
print(s1**s2)


# 13
# put your python code here
s1, s2 = map(float, input().split())
print(s1 + s2)


# 14
# put your python code here
x, y = map(int, input().split())
print(x + x * 2 + y + y * 4)


# 15
# put your python code here
a = float(input())
b = float(input())

print(float((a + b) * 2))


# 16
# put your python code here
import math

print(round(math.pi, 3))


# 17
# put your python code here
s = float(input())
print("Вы ввели число", s)


# 18
# put your python code here
s = float(input())
print(True if int(s) % 3 == 0 else False)


# 19
x = float(input())
check_fraction = lambda x: x % 1 > 0.50
print(check_fraction(x))


# 20
# put your python code here
a, b = map(int, input().split())
print(a % b == 0)


# 21
# put your python code here
a, b, c = map(int, input().split())
print(a < b + c and b < c + a and c < b + a)


# 22
# put your python code here
s = float(input())
print(0 <= s <= 2 or 10 <= s <= 20)


# 23
# put your python code here
s1 = input()
s2 = input()
print(s1 + " " + s2)

# 24
# put your python code here
s, t = input().split()
print(s, s, t, t, t)


# 25
# put your python code here
s, t = input().split()
print(f"Переменная a = {s}, переменная b = {t}")


# 26
# put your python code here
s = input()
print(f"Строка: {s}. Длина: {len(s)}")


# 27
# put your python code here
s, t = input().split()
print(s in t, s == t, s > t, s < t)


# 28
# put your python code here
s, t = input().split()
print(f"Коды: {s} = {ord(s)}, {t} = {ord(t)}")


# 29
# put your python code here
s = input()

print(s[0], s[-1], sep="")


# 30
# put your python code here
s = input()
print(s[:4])


# 31
# put your python code here
s = input()
print(s[-3:])


# 32
# put your python code here
s = input()
print(s[1::2])


# 33
# put your python code here

s = input()
t = input()
print(s[::2], t[1::2])


# 34
# put your python code here
s = input()
print(s[:5:][::-1])


# 35
# put your python code here
s, t = input().split()
print(t[: len(s) :])


# 36
# put your python code here
s, t = input().split()
print(s[1 : len(t) : 2] == t[1::2])


# 37
# put your python code here
s = input()
print(s.capitalize())

# 38
# put your python code here
s = input()
print(s.count("-"))


# 39
# put your python code here
s = input()
print(s.find("ra"))


# 40
# put your python code here
s = input()
while "--" in s:
    s = s.replace("--", "-")
print(s)


# 41
s, t, y = map(int, input().split())
print(f"{s:03}\n{t:03}\n{y:03}")


# 42
# put your python code here
s = input()
print(s.count(" ") + 1)


# 43
# put your python code here
s = input()
print(s.replace(" ", ";"))


# 44
# put your python code here
print('Тема занятия "спецсимволы"')


# 45
# put your python code here
s, t = input().split()
print(s + "\\" + t)


# 46
# put your python code here
s = input()
print(s.replace(" ", "'", 1).replace(" ", '"'))


# 47
# put your python code here
print("C:\\WINDOWS\\System32\\drivers\\etc\\hosts")


# 48
# put your python code here
print(f'"{input()}"')

# 49
# put your python code here
n = input()
f = input()
a = input()
print(f"Уважаемый {n} {f}! Поздравляем Вас с {a}-летием!")


# 50
# put your python code here
n, f, a = input().split()
print(f"Габариты: {n} x {f} x {a}")


# 51
# put your python code here
s, t = map(int, input().split())
print(f"{min(s,t)} {max(s,t)}")


# 52
# put your python code here
c = input()
s = input()
n = input()
sh = input()
print(f"г. {c}, ул. {s}, д. {n}, кв. {sh}")


# 53
# put your python code here
s = float(input())
t = int(input())
print(f"Вы можете получить {int(t//s)}$ за {t} рублей по курсу {s}")


# 54
lst = list(map(int, input().split()))
print(lst)


# 55
# put your python code here
cities = input().split()
print("Москва" in cities)


# 56
# put your python code here
cities = input().split()
print(cities[-1])

# 57
# put your python code here
marks = list(map(int, input().split()))
print(round(sum(marks) / len(marks), 1))


# 58
# put your python code here
list = []

list.append(str(input()))
list.append(str(input()))
list.append(int(input()))
list.append(float(input()))

list.remove(list[2])
list[1] = "Пушкин"
list[-1] = list[-1] * 2

print(list)

# 59
# put your python code here
lst = list(map(int, input().split()))
print(max(lst), min(lst), sum(lst))


# 60
lst = list(map(int, input().split()))
print(*sorted(lst, reverse=True))


# 61
lst = list(map(str, input().split()))
cities = ["Москва", "Тверь", "Вологда"]
cities += lst
lst = cities

print(*lst)


# 62
# put your python code here
lst = list(map(str, input().split()))
cities = ["Москва", "Тверь", "Вологда"]
lst += cities

print(*lst)


# 63
# put your python code here
v = [1205, 1101, 1434, 1320, 923, 874]
print(v[:3])


# 64
# put your python code here
v = [1205, 1101, 1434, 1320, 923, 874]
print(v[-4::])

# 65
# put your python code here
c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
print(c[::2])


# 66
# put your python code here
c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
print(c[1::2])


# 67
# put your python code here
m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
print(m[2:7][::-1])


# 68
# put your python code here
m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
print(m[::-2])


# 69
s = input().split()
s.append("True") if s[0] != s[-1] else s.append("False")
print(*s)


# 70
cities = ["Москва", "Казань", "Ярославль"]
cities.insert(1, "Ульяновск")
print(*cities)


# 71
# put your python code here
s = input()

lst = [
    x for x in s if (x.isdigit() or x in "()")
]  # ['7', '(', '9', '1', '2', ')', '1', '2', '3', '4', '5', '6', '7']
lst = lst[1:]
lst.insert(0, "8")
print("".join(lst))


# 72
# put your python code here
s = input().split()
print(s[2], s[0][0] + "." + s[1][0] + ".")


# 73
# put your python code here
s = list(map(int, input().split()))  # [8, 11, -5, 10, -1, 0, 7]
s.sort()
print(*s[:3])


# 74
# put your python code here
lst = list(map(int, input().split()))
lst.append(bool(lst.pop() % 2))
print(*lst)


# 75
# put your python code here
lst = list(map(int, input().split()))
print(lst.count(2))

# 76
# put your python code here
lst = list(map(str, input().split()))
lst.sort()
del lst[0]
print(*lst)


# 77
lst = [5.4, 6.7, 10.4]

# здесь продолжайте программу
digs = map(int, input().split())
lst.append([*digs])
print(lst)


# 78
# put your python code here
lst = [input().split() for _ in range(3)]
print(lst)


# 79
# put your python code here
lst = [input().split() for _ in range(3)]
print(*list(zip(*lst))[-1])


# 80
t = [
    ["Скажи-ка", "дядя", "ведь", "не", "даром"],
    ["Я", "Python", "выучил", "с", "каналом"],
    ["Балакирев", "что", "раздавал?"],
]
v = input()

print(any(v in s for s in t))


# 81
# put your python code here
print(max(map(float, input().split())))


# 82

s = input().lower()
print("ДА" if s == s[::-1] else "НЕТ")


# 83
m, n = map(int, input().split())
if m % n == 0:
    print(m // n)
else:
    print(f"{m} на {n} нацело не делится")

# 84

a, b, c = input().split()
print("ДА" if (int(a) ** 2 + int(b) ** 2 == int(c) ** 2) else "НЕТ")


# 85
s = input()
print("ДА" if s[-1] == "7" else "НЕТ")


# 86
i = input()
print("ДА" if i.count("t") and i.count("h") and i.count("o") else "НЕТ")


# 87
# put your python code here
cities = list(map(str, input().split()))

if "Москва" in cities:
    cities.remove("Москва")
print(*cities)


# 88
a, b, c, d = map(int, input().split())

print("ДА" if max(a, b) >= max(c, d) + 2 and min(a, b) >= min(c, d) + 2 else "НЕТ")


# 89
# put your python code here
i = input()
print(
    "ДА"
    if int(i[0]) + int(i[1]) + int(i[2]) == int(i[3]) + int(i[4]) + int(i[5])
    else "НЕТ"
)

# 90
i = float(input())
print("green" if i % 5 < 4 else "red")

# 91
# put your python code here

m = """1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход"""

i = input()
if i in ("2345"):
    start = m.find(i)
    end = m.find(str(int(i) + 1))
    print(m[start:end])
elif i == "6":
    print("6. Выход")
else:
    print("1. Введение в Python")


# 92
# put your python code here
a, b, c = map(int, input().split())
if a > b:
    if b > c:
        print(c)
    else:
        print(b)
else:
    if a > c:
        print(c)
    else:
        print(a)


# 93
# put your python code here
# 1) легкий вес – до 60 кг (включительно);
# 2) первый полусредний вес – до 64 кг (включительно);
# 3) полусредний вес – до 69 кг (включительно);
# 4) остальные - более 69 кг.


i = float(input())
if i > 64:
    if i > 69:
        print(4)
    else:
        print(3)
else:
    if i <= 60:
        print(1)
    else:
        print(2)


# 94
# put your python code here
lst = [
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье",
]
print(lst[int(input()) - 1])


# 95
# put your python code here

lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(lst[int(input()) - 1])


# 96
lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m, d = map(int, input().split())  # month  day
day_before = d - 1
day_after = d + 1
month_before = m
month_after = m
if d == 1:
    day_before = lst[d - 1]
    month_before = m - 1
elif d == lst[m - 1]:
    day_after = 1
    month_after = m + 1
print(f"{month_before:02}.{day_before:02} {month_after:02}.{day_after:02}")


# 97
# put your python code here
days = [
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье",
]
k = int(input())
print(days[(k % 7) - 1])


# 98
s = float(input())
t = float(input())
d = s if s > t else t
print(d)


# 99
# put your python code here
i = int(input())
msg = "кратно 3" if not i % 3 else "не кратно 3"
print(msg)


# 100
# put your python code here
t = input().lower()
msg = "палиндром" if t == t[::-1] else "не палиндром"

print(msg)


# 101
# put your python code here
print("False" if not int(input()) else "True")


# 102
# put your python code here
s = int(input())
print(0 if s == 59 else s + 1)


# 103
# put your python code here
m = ["#до", "ре", "ми", "#фа", "соль", "ля", "си"]
a, b, c = map(int, input().split())

print(m[a - 1], m[b - 1], m[c - 1])


# 104 ЦИКЛЫ

n, m = input().split()
N = int(n)
M = int(m)

iterator = 0
list = []
while N <= M:
    print(N**2, end=" ")
    N += 1


# 105
# put your python code here

book_price = float(input())
multiple = 2

while multiple <= 10:
    print(f"{book_price*multiple:.1f}", end=" ")
    multiple += 1


# 106
# put your python code here
N = int(input())
iteration = 1
summ = 0

while iteration <= N:
    summ += 1 / iteration
    iteration += 1

print(round(summ, 3))


# 107
# put your python code here
counter = 0
while True:
    inp = int(input())
    if inp == 0:
        break
    else:
        counter += inp

print(counter)


# 108
# put your python code here


inp = input()

while "--" in inp:
    inp = inp.replace("--", "-")
print(inp)


# 109
# put your python code here

inp = int(input())
result = 1
while inp > 0:
    result *= inp % 10
    inp = inp // 10
print(result)


# 110
# put your python code here

inp = int(input())

prev = 1
curr = 1
fib = "1 1 "
counter = 0

while counter < inp - 2:
    fib += str(curr + prev) + " "
    temp = curr
    curr += prev
    prev = temp
    counter += 1
print(fib)


# 111
# put your python code here
inp = int(input())

kletok = 1

while inp > 3:
    kletok *= 2
    inp -= 3

print(kletok)


# 112
inp = int(input())
vklad = int(1000)

while inp > 0:
    vklad *= 1.05
    inp -= 1

print(round(vklad, 2))


# 113
# put your python code here
# Чтение входных данных
n, m = map(int, input().strip().split())

# Если n четное, начинаем с n + 1, иначе начинаем с n
start = n + 1 if n % 2 == 0 else n

# Инициализация переменной для хранения результатов
result = []

# Используем цикл while для генерации нечетных чисел в интервале
while start <= m:
    result.append(start)
    start += 2  # Переход к следующему нечетному числу

# Формируем строку и выводим результат
print(" ".join(map(str, result)))


# 114
inp = 100
res = []
while inp < 1000:
    if inp % 47 == 43 and inp % 3 == 0:
        res.append(inp)
        inp += 1
    else:
        inp += 1
print(*res)


# 115
p = [0] * 10
counter = 0

for v in p:
    if counter == 5:
        break
    index = int(input())
    if p[index] == 1:
        continue
    else:
        p[index] = 1
        counter += 1
print(*p)

# 116
summ = 1
inp = 1

while inp != 0:
    inp = int(input())
    if inp > 0:
        summ *= inp
    else:
        continue
print(summ)


# 117
# put your python code here
inp = input().strip().split()
index = 0

while index < len(inp):

    current_el = inp[index]

    if len(current_el) > 4:
        index += 1
        continue
    else:
        print("НЕТ")
        break
else:
    print("ДА")


# 118
inp = input().strip().split()
index = 0

while index < len(inp):

    current_el = inp[index].lower()
    if current_el[0] == current_el[-1]:
        print("ДА")
        break
    else:
        index += 1
        continue
else:
    print("НЕТ")


# 119
N = int(input())
temp = 1
list_ = []

while temp < N + 1:
    if N < 100:
        if temp % 3 == 0 and temp % 5 == 0:
            list_.append(temp)
            temp += 1
        else:
            temp += 1

    else:
        print("слишком большое значение n")
        break
else:
    print(*list_)


# 120
# put your python code here
n = int(input())
temp = 1

while True:
    if temp**2 <= n:
        temp += 1
    else:
        print(temp)
        break


# 121
n = int(input())

current = 10
day = 1
while current <= n:
    current *= 1.1
    day += 1

print(day)


# 122
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_out = []
i = 0

while i < len(lst_in):
    if " " in lst_in[i]:
        i += 1
    else:
        lst_out.append(lst_in[i])
        i += 1

print(*lst_out)

# 123
# put your python code here
for i in range(0, 11):
    print(i, end=" ")


# 124
# put your python code here
for i in range(-10, 1):
    print(i, end=" ")


# 125
# put your python code here
for i in range(-10, -1, 2):
    print(i, end=" ")


# 126
# put your python code here
for i in range(1, 20, 3):
    print(i, end=" ")


# 127
inp = list(map(int, input().strip().split()))
summ = 0

for i in inp:
    if i % 2 != 0:
        summ += i
print(summ)

# 128
# put your python code here

inp = list(map(str, input().strip().split()))
for i in range(len(inp)):
    inp[i] = len(inp[i])
print(*inp)


# 129
# put your python code here

inp = int(input())

for i in range(1, inp + 1):
    if inp % i == 0:
        print(i)


# 130
# put your python code here
inp = int(input())
flag = True

for i in range(2, inp):
    if inp % i == 0:
        flag = False
print("ДА" if flag else "НЕТ")


# 131
inp = list(map(str.lower, input().strip().split()))
# inp = int(input())
last = ""

for i in inp:
    i = i.strip("ъыь")
    if i[0] == last or i == inp[0]:
        last = i[-1]
    else:
        print("НЕТ")
        break
else:
    print("ДА")


# 132
# put your python code here
inp = int(input())
summ = 0

for i in range(1, inp):
    if i % 3 == 0 or i % 5 == 0:
        summ += i
print(summ)


# 133
# put your python code here
inp = str(input().lower())
count = 0

for i in range(len(inp) - 1):
    if inp[i] + inp[i + 1] == "ра":
        print(i, end=" ")
        count += 1
if count == 0:
    print(-1)


# 134
N = input()
flag = True
if not N.startswith("+"):
    flag = False

for char in "+-()":
    N = N.replace(char, "")
if not N.startswith("7"):
    flag = False
for i in N:
    if not i.isdigit():
        flag = False
        break
    else:
        continue

if flag:
    print("ДА")
else:
    print("НЕТ")


# 135
# put your python code here
text = input().replace(" ", "").replace("-", "+-").split("+")
print(sum(map(int, text)))


# 136
# put your python code here
lst_in = list(map(int, input().strip().split()))

for i in range(len(lst_in)):
    lst_in[i] = abs(lst_in[i]) ** 2
print(*lst_in)


# 137
# put your python code here
lst_in = list(map(int, input().strip().split()))
new_lst = []

for i in range(len(lst_in)):
    new_lst.append(lst_in[i])
    new_lst.append(lst_in[i])

print(*new_lst)


# 138
# put your python code here
lst = list(map(float, input().split()))
a = lst[0]
for i in lst:
    if i < a:
        a = i
print(a)

# 139
lst_in = list(map(float, input().strip().split()))

for x in range(len(lst_in)):
    if lst_in[x] < 0:
        lst_in[x] = -1.0

print(*lst_in)


# 140
inp = input()

cities = list(map(str, inp.strip().split()))

c = iter(cities)

print(next(c))
print(next(c))


# 141
# put your python code here

inp = input()
it = iter(inp)

for i in inp:
    if i != " ":
        print(i, end="")
        next(it)
    else:
        break


# 142
# put your python code here
it = iter(map(str, input()))
result = []
for i in range(4):
    result.append(next(it))

print(" ".join(result))


# 143
# put your python code here
n = int(input())
lst = []
for i in range(n):
    r = []
    for j in range(n):
        if j == n - 1:
            r.append(5)
        else:
            r.append(1)
    lst.append(r)

for i in lst:
    print(*i)


# 144
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

for i in range(len(lst_in)):

    while "  " in lst_in[i]:
        lst_in[i] = lst_in[i].replace("  ", " ")

    lst_in[i] = lst_in[i].replace(" ", "-")
    print(lst_in[i])


# 145
# put your python code here
d = int(input())
for i in range(2, d):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i, end=" ")


# 146
import sys

# Чтение данных
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# Размер матрицы
rows = len(lst_in)
cols = len(lst_in[0])


# Функция проверки соседей
def is_valid(i, j):
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            new_i, new_j = i + x, j + y
            if 0 <= new_i < rows and 0 <= new_j < cols:
                if lst_in[new_i][new_j] == 1:
                    return False
    return True


# Основная проверка
for i in range(rows):
    for j in range(cols):
        if lst_in[i][j] == 1:
            if not is_valid(i, j):
                print("НЕТ")
                exit()

print("ДА")


# 147
import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
# здесь продолжайте программу (используйте список lst_in)
flag = "ДА"
for i in range(len(lst_in)):
    for j in range(len(lst_in)):
        if lst_in[i][j] != lst_in[j][i]:
            flag = "НЕТ"

print(flag)


# 148
# put your python code here
inp = list(map(int, input().strip().split()))

for i in range(len(inp)):
    for j in range(i, len(inp)):
        if inp[i] < inp[j]:
            continue
        else:
            inp[i], inp[j] = inp[j], inp[i]

print(*inp)


# 149
# put your python code here
inp = list(map(int, input().strip().split()))

for i in range(len(inp) - 1):
    for j in range(0, len(inp) - i - 1):
        if inp[j] > inp[j + 1]:
            inp[j], inp[j + 1] = inp[j + 1], inp[j]

print(*inp)


# 150
# put your python code here
d = int(input())
money = [64, 32, 16, 8, 4, 2, 1]
result = []
rest = d

for i in money:
    for j in range(int(rest // i)):
        result.append(i)
    rest = d % i

print(*result)


# 151
# put your python code here
input_data = list(map(float, input().split()))
lst_abs = [abs(x) for x in input_data]
print(lst_abs)


# 152
# put your python code here
print([int(x) for x in str(input())])

# 153
inp = int(input())

A = [[1 if k == x else 0 for k in range(inp)] for x in range(inp)]
for row in A:
    print(*row)


# 154
# put your python code here
inp = input()
result = [x for x in inp.strip().split() if len(x) > 5]
print(*result)


# 155
# put your python code here
n = int(input())
result = [x for x in range(n + 1) if x != 0 and n % x == 0]
print(*result)


# 156
# put your python code here
n = int(input())

result = [[0 + x for k in range(n)] for x in range(n)]

for i in result:
    print(*i)


# 157
inp = input()

lst = list(map(float, inp.strip().split()))

result = [x for i, x in enumerate(lst) if i % 2 == 0]
print(*result)


# 158
# put your python code here
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

combined_list = [lst1[i] + lst2[i] for i, x in enumerate(lst1)]
print(*combined_list)


# 159
# put your python code here
lst = list(map(str, input().strip().split()))

cities = [x for x in lst[::2]]
population = [int(x) for x in lst[1::2]]
combined = [[cities[i], population[i]] for i, x in enumerate(cities)]

print(combined)


# 160
import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
print(" ".join(map(str, [x for row in lst_in for x in row][::-1])))

# 161
# put your python code here

import sys
import math

inp = list(map(int, sys.stdin.read().strip().split()))
n = int(math.sqrt(len(inp)))
lst = [inp[i * n : (i + 1) * n] for i in range(n)]
print(lst)


# 162
t = [
    "– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!",
    "Недаром помнит вся Россия",
    "Как мы рубили их тогда!",
]

lst = [[k for k in x.split() if len(k) > 3] for x in t]

print(lst)

# 163
import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
A = [[row[x] for row in lst_in] for x in range(len(lst_in[0]))]

for row in A:
    print(*row)


# 164
# put your python code here
t = input()
t_splited = t.split()
d = dict()
for i in range(len(t_splited)):
    key, value = t_splited[i].split("=")
    d[key] = int(value)

print(*sorted(d.items()))


# 165
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {}
# здесь продолжайте программу (используйте список lst_in)
for i in lst_in:
    key, value = i.split("=")
    d[int(key)] = value


print(*sorted(d.items()))


# 166
# put your python code here
inp = input().split()
ddd = {}
for i in inp:
    key, value = i.split("=")
    ddd[key] = value
if "house" in ddd and "True" in ddd and "5" in ddd:
    print("ДА")
else:
    print("НЕТ")


# 167
d = dict([x.split("=") for x in input().split()])

if "False" in d:
    del d["False"]
if "3" in d:
    del d["3"]

print(*sorted(d.items()))


# 168
# put your python code here
dat = input().split()
d = {}
for number in dat:
    key, value = number[:2], number
    if key not in d:
        d[key] = [value]
    else:
        d[key].append(value)

print(*sorted(d.items()))


# 169
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
# ['+71234567890 Сергей', '+71234567810 Сергей', '+51234567890 Михаил', '+72134567890 Николай']
d = {}
for i in lst_in:
    phone, name = i.split()
    if name not in d:
        d[name] = [phone]
    else:
        d[name].append(phone)

print(*sorted(d.items()))


# 170
d = {}
while (m := int(input())) != 0:
    if m in d:
        print("значение из кэша:", d.get(m, []))

    else:
        sqr = round(m**0.5, 2)
        d[m] = sqr
        print(sqr)


# 171
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)

d = {}

for i in lst_in:
    if i not in d:
        d[i] = f"HTML-страница для адреса {i}"
        print(d[i])
    else:
        print(f"Взято из кэша: {d[i]}")


# 172
# put your python code here
d = {
    " ": "-...-",
    "Ё": ".",
    "А": ".-",
    "Б": "-...",
    "В": ".--",
    "Г": "--.",
    "Д": "-..",
    "Е": ".",
    "Ж": "...-",
    "З": "--..",
    "И": "..",
    "Й": ".---",
    "К": "-.-",
    "Л": ".-..",
    "М": "--",
    "Н": "-.",
    "О": "---",
    "П": ".--.",
    "Р": ".-.",
    "С": "...",
    "Т": "-",
    "У": "..-",
    "Ф": "..-.",
    "Х": "....",
    "Ц": "-.-.",
    "Ч": "---.",
    "Ш": "----",
    "Щ": "--.-",
    "Ъ": "--.--",
    "Ы": "-.--",
    "Ь": "-..-",
    "Э": "..-..",
    "Ю": "..--",
    "Я": ".-.-",
}

inp = input()
morze = ""
for x in inp.upper():
    morze += d.get(x) + " "
print(morze)


# 173
# put your python code here
d = {
    " ": "-...-",
    "Ё": ".",
    "А": ".-",
    "Б": "-...",
    "В": ".--",
    "Г": "--.",
    "Д": "-..",
    "Е": ".",
    "Ж": "...-",
    "З": "--..",
    "И": "..",
    "Й": ".---",
    "К": "-.-",
    "Л": ".-..",
    "М": "--",
    "Н": "-.",
    "О": "---",
    "П": ".--.",
    "Р": ".-.",
    "С": "...",
    "Т": "-",
    "У": "..-",
    "Ф": "..-.",
    "Х": "....",
    "Ц": "-.-.",
    "Ч": "---.",
    "Ш": "----",
    "Щ": "--.-",
    "Ъ": "--.--",
    "Ы": "-.--",
    "Ь": "-..-",
    "Э": "..-..",
    "Ю": "..--",
    "Я": ".-.-",
}

inp = input().split()
translate = ""
reversed_morze = {v: k for k, v in d.items()}

for i in inp:
    translate += reversed_morze[i]

print(translate.lower())


# 174
# put your python code here
inp = list(map(str, input().strip().split()))
d = {}
d = dict.fromkeys(inp)
new_list = [x for x in d.keys()]

print(*new_list)


# 175
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
di = {}

for x in lst_in:
    key, value = x.split()
    di.setdefault(key, []).append(value)

for key, value in di.items():
    print(key + ":", ", ".join(value))


# 176
# put your python code here
things = {
    "карандаш": 20,
    "зеркальце": 100,
    "зонт": 500,
    "рубашка": 300,
    "брюки": 1000,
    "бумага": 200,
    "молоток": 600,
    "пила": 400,
    "удочка": 1200,
    "расческа": 40,
    "котелок": 820,
    "палатка": 5240,
    "брезент": 2130,
    "спички": 10,
}

inp = int(input())
weight_limit = inp * 1000
to_take = []
reversed_things = {v: k for k, v in things.items()}
sorted_things = dict(sorted(reversed_things.items(), reverse=True))

for key, value in sorted_things.items():
    if weight_limit - key >= 0:
        weight_limit -= key
        to_take.append(value)


else:
    print(*to_take)


# 177
# put your python code here
t = (3.4, -56.7)
t += tuple(map(int, input().split()))

print(t)


# 178
# put your python code here

t = tuple(input().split())
if t.count("Москва") == 0:
    t += ("Москва",)
print(*t)


# 179
t = tuple(input().split())
if t.count("Ульяновск") > 0:
    tlist = list(t)
    tlist.remove("Ульяновск")
    t = tuple(tlist)
print(*t)


# 180
# put your python code here
t = tuple(input().split())
for i in t:
    if "ва" in i.lower():
        print(i.lower(), end=" ")


# 181
# put your python code here
t = tuple(map(int, input().split()))
new_t = tuple()
for i in t:
    if new_t.count(i) == 0:
        new_t += (i,)

print(*new_t)


# 182
t = tuple(map(int, input().split()))
for index, i in enumerate(t):
    if t.count(i) > 1:
        print(index, end=" ")


# 183
t = (
    (1, 0, 0, 0, 0),
    (0, 1, 0, 0, 0),
    (0, 0, 1, 0, 0),
    (0, 0, 0, 1, 0),
    (0, 0, 0, 0, 1),
)

n = int(input())
new_t = tuple()

for i in range(n):
    r = tuple()
    for j in range(n):
        r += (t[i][j],)

    new_t += (r,)
for i in new_t:
    print(*i)


# 185
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

new_t = tuple()

for i in lst_in:
    j, k = i.split()
    new_t += ((j, k),)

print(new_t)


# 186
# put your python code here
s = set(map(float, input().split()))

print(*sorted(s))


# 187
# put your python code here
s = set(map(str.lower, input().split()))

print(len(s))


# 188
# put your python code here
inp = input()
s = set()

for i in inp:
    if i.isdigit():
        s.add(i)

if len(s) > 0:
    print(*sorted(s))
else:
    print("НЕТ")


# 189
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
gest_list = set()
# здесь продолжайте программу (используйте список lst_in)
for i in lst_in:
    gest_list.add(i)
print(len(gest_list))


# 190
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))


# здесь продолжайте программу (используйте список lst_in)
set_names = set()
for i in lst_in:
    name, comment = i.split(":")
    set_names.add(name)
print(len(set_names))


# 191
cities = set()

while (inp := input()) != "q":
    cities.add(inp)
print(len(cities))


# 192
# put your python code here
inp = list(map(int, input().split()))
inp2 = list(map(int, input().split()))
s = set(inp) & set(inp2)

print(*sorted(s))


# 193
# put your python code here

inp = list(map(int, input().split()))
inp2 = list(map(int, input().split()))
s = set(inp) - set(inp2)

print(*sorted(s))


# 194
# put your python code here
inp = list(map(int, input().split()))
inp2 = list(map(int, input().split()))
s = set(inp) ^ set(inp2)

print(*sorted(s))


# 195
print("ДА" if set(input().split()) == set(input().split()) else "НЕТ")


# 196
# put your python code here
inp = set(map(int, input().split()))
print("НЕ ДОПУЩЕН") if 2 in inp else print("ДОПУЩЕН")


# 197
# put your python code here
inp1 = set(map(str, input().split()))
inp2 = set(map(str, input().split()))
print("ДА") if inp1 <= inp2 else print("НЕТ")


# 198
# put your python code here
dig = int(input())
set_const = {2, 3, 5}
set_custom = set()

for x in range(1, int(dig**0.5) + 1):
    if dig % x == 0:
        set_custom.add(x)

print("ДА") if set_const < set_custom else print("НЕТ")


# 199
# put your python code here
inp = list(input().split())

d = {index: value for index, value in enumerate(inp[1:], start=int(inp[0]))}

print(d[4])


# 200
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)

d = {x for x in lst_in}
print(len(d))

# 201
# put your python code here
d = {x for x in input().lower().split() if len(x) >= 3}
print(len(d))


# 202
inp = input().lower().split()
di = {x: inp.count(x) for x in inp}

print(di.get("и", 0))


# 203
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
d = {}
for x in lst_in:
    author, poem = x.strip().split(": ")
    if author not in d:
        d[author] = set()

    d[author].add(poem)


# 204
# put your python code here


def not_first():
    print("It's my first function")


not_first()


# 205
# put your python code here


def not_first(name, surname):
    print(f"""Уважаемый, {name} {surname}! Вы верно выполнили это задание!""")


name, surname = input().split()
not_first(name, surname)


# 206
# put your python code here


def not_first(weight):
    print(f"Предмет имеет вес: {weight} кг.")


not_first(input())


# 207
# put your python code here


def not_first(list_):
    list__ = list(map(int, list_.split()))
    print(f"Min = {min(list__)}, max = {max(list__)}, sum = {sum(list__)}")


not_first(input())


# 208
# put your python code here


def not_first(width, height):
    print(f"Периметр прямоугольника, равен {(int(width) + int(height)) * 2}")


width_, height_ = input().split()
not_first(width_, height_)

# 209
# put your python code here
import string


def not_first(w):
    valid_chars = set(string.ascii_letters + string.digits + "_@.")

    if all(char in valid_chars for char in w) and w[-3] == "." and "@" in w:
        print("ДА")
    else:
        print("НЕТ")


not_first(input())


# 210


def get_sq(dig):
    return dig**2


print(get_sq(float(input())))


# 211
def is_triangle(a, b, c):
    return a < b + c and b < a + c and c < b + a


# 212


def is_large(string_):
    return len(string_) >= 3


# 213
def is_large(string_):
    return string_ % 2 == 0


while (x := int(input())) != 1:
    if is_large(x):
        print(x)
    else:
        continue


# 214
# put your python code here
def nechet(n):
    return n % 2 != 0


lst_d = list(map(int, input().split()))
lst = [x for x in lst_d if nechet(x)]
print(*lst)


# 215
tp = input().strip()

if tp == "RECT":

    def get_sq(lenght, width):
        return int(lenght) * int(width)

else:

    def get_sq(lenght):
        return lenght**2


# 216
# put your python code here
def fu(string_):
    return len(string_) >= 6


cities = list(map(str, input().split()))
lst = [x for x in cities if fu(x)]
print(*lst)


# 217
# put your python code here
def fu(string_):
    return string_, len(string_)


d = {x: y for x, y in (fu(x) for x in input().split())}
a = sorted(d, key=d.get)
print(*a)


# 218
# put your python code here
def fu(max, min):
    return int(max) * int(min)


digs = list(map(int, input().split()))
print(fu(max(digs), min(digs)))


# 219
def get_nod(a, b):
    if a < b:
        b, a = a, b
    while b != 0:
        a, b = b, a % b
    return a


# 220
def get_rect_value(a, b, type=0):
    return a * b if type else 2 * (a + b)


# 221
def check_password(password, chars="$%!?@#"):
    return any(x in chars for x in password) and len(password) > 7


# 222
def fo(row, sep="-"):
    t = {
        "ё": "yo",
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "h",
        "ц": "c",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    }

    t.setdefault(" ", sep)
    return "".join([t[x] if x in t else x for x in row.lower()])


s = input()
print(fo(s))
print(fo(s, "+"))


# 223
# put your python code here
def fo(row, tag="h1"):
    return f"<{tag}>{row}</{tag}>"


s = input()
print(fo(s))
print(fo(s, "div"))


# 224
def fo(row, tag="h1", up=True):
    return f"<{tag.upper()}>{row}</{tag.upper()}>" if up else f"<{tag}>{row}</{tag}>"


s = input()
print(fo(s, "div"))
print(fo(s, "div", up=False))


# 225


def get_even(*args):
    return [x for x in args if not x % 2]


# 226
def get_biggest_city(*args):
    return max(args, key=len)


# 227
def get_data_fig(*args, **kwargs):
    perim = sum(args)
    result = (perim,)
    param_order = ["tp", "color", "closed", "width"]
    for param in param_order:
        if param in kwargs:
            result += (kwargs[param],)

    return result


# 228
def is_isolate(x, y, matrix):
    n = len(matrix)
    if x + 1 < n and y + 1 < n:
        return (
            matrix[x][y] != matrix[x][y + 1]
            and matrix[x][y] != matrix[x + 1][y]
            and matrix[x][y] != matrix[x + 1][y + 1]
        )
    elif x + 1 == n and y + 1 == n:
        return True

    elif x + 1 == n:
        return matrix[x][y] != matrix[x][y + 1]
    elif y + 1 == n:
        return matrix[x][y] != matrix[x + 1][y]
    return True


def verify(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if matrix[x][y] == 1:
                if not is_isolate(x, y, matrix):
                    return False
    return True


# 229
def str_min(str1, str2):
    return str1 if str1 < str2 else str2


# Функция для поиска минимальной строки среди трёх
def str_min3(str1, str2, str3):
    return str_min(str_min(str1, str2), str3)


# Функция для поиска минимальной строки среди четырёх
def str_min4(str1, str2, str3, str4):
    return str_min(str_min3(str1, str2, str3), str4)


# 230
*lst, x, y, z = map(int, input().split())
print(*lst)


# 231

lst = list(map(str, input().split()))
lst_c = (*lst,)
print(lst_c)


# 232
# put your python code here
a, b = map(int, input().split())
lst = [*range(a, b + 1)]

print(*lst)


# 233
d = map(float, input().split())
c = map(str, input().split())
lst = [*d, *c]
print(*lst)


# 234
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
menu2 = dict([x.split("=") for x in lst_in])


menu = {"Главная": "home", "Архив": "archive", "Новости": "news"}
# здесь продолжайте программу (используйте список lst_in и menu)

menu = {**menu, **menu2}


# 235
# считывание числа N
N = int(input())


# здесь продолжайте программу
def get_rec_N(n):
    if n == 0:
        return
    else:
        get_rec_N(n - 1)
    print(n)


get_rec_N(N)  # вызов рекурсивной функции


# 236
# put your python code here
d = map(int, input().split())


def get_rec_sum(d):
    head, *tail = d
    return head + get_rec_sum(tail) if tail else head


print(get_rec_sum(d))


# 237
N = int(input())


def fib_rec(N, f=[1, 1]):
    if len(f) == N:
        return f
    f.append(f[-1] + f[-2])
    return fib_rec(N, f)


# 238
# ввод числа n
n = int(input())


# здесь задается функция fact_rec  (переменную n не менять!)
def fact_rec(n):
    if n == 0:
        return 1
    return n * fact_rec(n - 1)


# 239
d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ["True", [-2, -1]]], 7.89]


# здесь продолжайте программу
def get_line_list(d, a=[]):
    for x in d:
        if isinstance(x, list):
            get_line_list(x, a)
        else:
            a.append(x)
    return a


# 240
# put your python code here
N = int(input())


def fib_rec(N, f=[1, 2]):
    if len(f) == N:
        return f
    f.append(f[-1] + f[-2])
    return fib_rec(N, f)


print(*fib_rec(N)[-1:])


# 241
# put your python code here
def merge_sort(arr):
    # Если длина массива меньше или равна 1, он уже отсортирован
    if len(arr) <= 1:
        return arr

    # Разделяем список на две половины
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Слияние двух половин
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    # Пока есть элементы в обоих списках, сравниваем и объединяем их
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы из левого и правого списков
    result.extend(left[i:])
    result.extend(right[j:])

    return result


lst = list(map(int, input().split()))
print(*merge_sort(lst))


# 242
get_sq = lambda x: x**2

# 243
get_div = lambda x, y: None if y == 0 else x / y


# 244
# put your python code here
x = float(input())
nn = lambda x: x if x > 0 else x * (-1)
print(nn(x))


# 245
# put your python code here
s = input()

xx = lambda x: True if "ra" in x else False
print(xx(s))


# 246
def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res


# 247

WIDTH = int(input())


def func1():
    WIDTH += 1
    return WIDTH


print(func1())


# 248
def func1():
    msg = input()

    def func2():
        nonlocal msg
        msg = input()
        print(msg)

    func2()
    print(msg)


func1()


# 249


def create_global(x):
    global TOTAL
    TOTAL = x


# 250
# put your python code here
def counter_add(add):
    def fo():
        return add + 5

    return fo


k = int(input())

cnt = counter_add(k)
print(cnt())


# 251
# put your python code here
def counter_add(n):
    def fo(d):
        return d + n

    return fo


k = int(input())

cnt = counter_add(2)
print(cnt(k))


# 252
# put your python code here
def counter_add():
    def fo(string_):
        return "<h1>" + string_ + "</h1>"

    return fo


k = str(input())

cnt = counter_add()
print(cnt(k))


# 253
# put your python code here
def counter_add(tag):
    def fo(string_):
        return "<" + tag + ">" + string_ + "</" + tag + ">"

    return fo


tag = str(input())
st = str(input())
cnt = counter_add(tag)
print(cnt(st))


# 254
def counter_add(tp):
    def fo(digits):
        if tp == "list":
            return list(map(int, digits.split()))
        else:
            return tuple(map(int, digits.split()))

    return fo


tp = str(input())
digits = str(input())
cnt = counter_add(tp)
print(cnt(digits))


# 255
def get_sq(width, height):
    return width * height


def func_show(func):
    def wrapper(*args, **kwargs):
        print("Площадь прямоугольника:", func(*args, **kwargs))

    return wrapper


# 256
menu = input()  # чтение пунктов меню (переменную menu не менять)


def show_menu(func):
    def wrapper(*args, **kwargs):
        lst = func(*args, **kwargs)
        for x in range(len(lst)):
            print(f"{x+1}. {lst[x]}")

    return wrapper


@show_menu
def get_menu(s):
    return s.split()


# 257
def sotr_list(s):
    def wrapper(*args, **kwargs):
        return sorted(s(*args, **kwargs))

    return wrapper


@sotr_list
def get_list(s):
    return list(map(int, s.split()))


s = input()
lst = get_list(s)
print(*lst)


# 258
# put your python code here
def sotr_list(s):
    def wrapper(*args, **kwargs):
        func = s(*args, **kwargs)
        dct = {func[0][x]: func[1][x] for x in range(len(func[0]))}
        return dct

    return wrapper


@sotr_list
def get_list(s, d):
    return list(map(str, s.split())), list(map(str, d.split()))


s = input()
d = input()
lst = get_list(s, d)

print(*sorted(lst.items()))


# 259
def decorate(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        while result.count("--"):
            result = result.replace("--", "-")
        return result

    return wrapper


@decorate
def translate(str_):
    t = {
        "ё": "yo",
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "h",
        "ц": "c",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    }

    lst = [t.get(x.lower(), x.lower()) for x in str_]
    replaced_chars = " : ;.,_"
    return "".join(
        char.replace(char, "-") if char in replaced_chars else char for char in lst
    )


s = input()

ct = translate(s)
print(ct)


# 260


# put your python code here
def dec_start(start=5):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + start

        return wrapper

    return decorator


@dec_start()
def sum_func(str_):
    lst = list(map(int, str_.split()))
    return sum(lst)


inp = input()
ct = sum_func(inp)
print(ct)


# 261


def dec_start(tag="h1"):
    def decorator(fn):
        def wrapper(*args):
            return f"<{tag}>{''.join(fn(*args))}</{tag}>"

        return wrapper

    return decorator


@dec_start(tag="div")
def my_func(str_):
    return [x.lower() for x in str_]


inp = input()
ct = my_func(inp)
print(ct)


# 262
def dec_start(chars="!? "):
    def decorator(fn):
        def wrapper(*args):
            lst = "".join(["-" if x in chars else x for x in fn(*args)])
            while lst.count("--"):
                lst = lst.replace("--", "-")
            return lst

        return wrapper

    return decorator


@dec_start()
def my_func(str_):
    t = {
        "ё": "yo",
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "h",
        "ц": "c",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    }
    return [t.get(x.lower(), x.lower()) for x in str_]


inp = input()
ct = my_func(inp)
print(ct)


# 263
from functools import wraps


def decorator(fn):
    @wraps(fn)
    def wrapper(*args):
        return sum(fn(*args))

    # wrapper.__name__ = fn.__name__
    # wrapper.__doc__ = fn.__doc__
    return wrapper


@decorator
def get_list(str_):
    """Функция для формирования списка целых значений"""
    lst = list(map(int, str_.split()))
    return lst


# 264
import math

print(math.ceil(float(input())))


# 265
# put your python code here
from math import floor

print(floor(float(input())))


# 266
from math import factorial as fact


def factorial(n):
    p = 1
    for i in range(2, n + 1):
        p *= i

    print("my factorial")
    return p


# 267

# put your python code here
from random import seed, randint

seed(1)
print(randint(10, 50))


# 268
from random import seed
from random import random as rnd


seed(10)
print(round(rnd(), 2))


# 279
f = open("abc.txt")
r = f.read(1)
f.close()


# 280
gen = (x for x in range(2, 10001))


# 281
a, b = map(int, input().split())
tp = tuple(x**2 for x in range(a, b + 1))


# 282
# put your python code here
a, b = map(int, input().split())
tp = (abs(x) for x in range(a, b + 1))

for x in range(5):
    print(next(tp))


# 283
# put your python code here
a = int(input())
gen = (abs(x) for x in range(-a, a + 1))
gen2 = (next(gen) ** 3 for x in range(4))
print(*gen2)


# 284
# put your python code here
from string import ascii_lowercase

gen = (y + x for y in ascii_lowercase for x in ascii_lowercase)
[print(next(gen), end=" ") for _ in range(50)]


# 285
cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]


a = (x for x in cities * 1000000)

[print(next(a), end=" ") for _ in range(20)]


# 286

# put your python code here
a, b = map(int, input().split())
fx = ((0.5 * pow(x / 100, 2) - 2.0) for x in range(100 * a, 100 * b + 1))
[print(round(next(fx), 2), end=" ") for _ in range(20)]


# 287
# ввод значения N (эту переменную не менять)
N = int(input())


# здесь продолжайте программу
def get_sum(total):
    sum = 0
    for i in range(1, total + 1):
        sum += i
        yield sum


# 288
# put your python code here
N = int(input())


def balak_seq(max_len):
    a, b, c = 1, 1, 1
    for i in range(max_len):
        if i < 3:
            yield 1
        else:
            a, b, c = b, c, a + b + c
            yield c


print(*balak_seq(N))


# 289
import random
from string import ascii_lowercase, ascii_uppercase

# установка зерна датчика случайных чисел (не менять)
random.seed(1)
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"


# здесь продолжайте программу
def passgen(N):
    yield "".join([chars[random.randint(0, len(chars) - 1)] for i in range(N)])


N = int(input())

for i in range(5):
    print(*passgen(N))


# 290
# put your python code here
from string import ascii_lowercase, ascii_uppercase
import random

random.seed(1)
chars = ascii_lowercase + ascii_uppercase


# здесь продолжайте программу
def mail_gen(n):
    while True:
        mail = ""
        for _ in range(n):
            mail += chars[random.randint(0, len(chars) - 1)]
        yield mail + "@mail.ru"


N = int(input())

for _ in range(5):
    print(next(mail_gen(N)))


# 291
# put your python code here
def digit_simple(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def simple():
    for i in range(2, 10 * 10):
        if digit_simple(i):
            yield i
        i += 1


get_prime = simple()

for i in range(20):
    print(next(get_prime), end=" ")


# 292
# put your python code here
s = map(float, input().split())

print(*[next(s) for _ in range(3)])


# 293
s = map(lambda x: abs(int(x)), input().split())

print(*s)


# 294
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
# переменную lst_in не менять!

lst2D = [list(map(int, x.split())) for x in lst_in]


# 295
# ввод строки (переменную s не менять)
s = input()
s_lst = s.split()

# здесь продолжайте программу

tp = tuple(map(lambda x: tuple(x.split("=")), s_lst))


# 296
# ввод строки (переменную s не менять)Привет Питон
s_lst = input()
t = {
    "ё": "yo",
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "y",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "h",
    "ц": "c",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ъ": "",
    "ы": "y",
    "ь": "",
    "э": "e",
    "ю": "yu",
    "я": "ya",
}
# здесь продолжайте программу

tp = list(map(lambda x: t.get(x.lower(), "-"), s_lst))

print(*tp, sep="")


# 297
# put your python code here
# ввод строки (переменную s не менять)Привет Питон
s_lst = input().split()

# здесь продолжайте программу

tp = list(map(lambda x: x if len(x) > 5 else "-", s_lst))

print(*tp)


# 298
# ввод строки (переменную s не менять)Привет Питон
lst = input().split()

# здесь продолжайте программу
ft = filter(lambda x: len(x) > 5, lst)
for i in range(3):
    print(next(ft), end=" ")


# 299
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
tp = tuple(map(lambda x: tuple(x.split("=")), lst_in))
ft = filter(lambda x: int(x[1]) > 500, tp)
print(*(i[0] for i in ft))


# 300
# put your python code here
lst = input().split()

ft = filter(lambda x: 9 < abs(int(x)) < 100, lst)
print(*ft)


# 301
coll_1 = input().split()
coll_2 = input().split()

sets = set(coll_1) & set(coll_2)
print(*sorted(filter(lambda x: int(x) % 2 == 0, map(int, sets))))


# 302
# put your python code here
import string


def mail_check(mail):
    letters_and_digits = string.ascii_lowercase + string.digits + "._@"

    if all(x in letters_and_digits for x in mail):
        head, tail = mail.split("@")
        if "." in tail and (x in letters_and_digits for x in head):
            return all(x in letters_and_digits for x in tail)

        else:
            return False

    else:
        return False


a = input().split()
print(*(filter(mail_check, a)))


# 303
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = map(lambda pair: pair[0] * pair[1], zip(a, b))

print(*(next(res) for _ in range(3)))


# 304
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
# здесь продолжайте программу (используйте список строк lst_in)
a = [[int(y) for y in x.split()] for x in lst_in]
lst2 = list(zip(*zip(*a)))
for x in lst2:
    print(*x)


# 305
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
# здесь продолжайте программу (используйте список строк lst_in)
# ['1 2 3 4', '5 6 7 8', '9 8 7 6']
zi = list(zip(*[[int(y) for y in x.split()] for x in lst_in]))

for x in zi:
    print(*x)


# 306
s = list(map(str, input().split()))
str_len = int(int(len(s)) ** 0.5)
lst = list(zip(*[iter(s)] * str_len))
for i in lst:
    a, b, c = i
    print(a, b, c)


# 307
# считывание строки в переменную s (эту переменную в программе не менять)
s = input()

lst = list(zip(s, range(10)))


# 308
# ввод строки в переменную s (переменную в программе не менять)
s = input()

# здесь продолжайте писать программу
s1 = list(map(int, s.split()))
lst = sorted(s1)
tp_lst = tuple(sorted(s1))


# 309
def get_sort(d):
    s = [v for k, v in sorted(d.items(), reverse=True)]
    return s


# 310
# put your python code here
s = map(int, input().split())
print(*(sorted(set(s), reverse=True)[:4]))


# 311
# put your python code here
s = list(map(int, input().split()))
t = list(map(int, input().split()))

s.sort()
t.sort(reverse=True)
print(*[x + y for x, y in zip(s, t)])


# 312
import sys


def func(di):
    s = sorted(di.items(), key=lambda x: x[1])
    return [item[0] for item in s[:3]]


# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
dct = {k: int(v) for k, v in (x.split(":") for x in lst_in)}
print(*func(dct))


# 313
# put your python code here
print(*(sorted(input().split(), key=len, reverse=True)))


# 314
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
dct = {k: int(v) for k, v in (x.split("=") for x in lst_in)}
dct2 = dict(sorted(dct.items(), key=lambda x: x[1], reverse=True))
print(*dct2)


# 315
# put your python code here
note = input().split()
# ['до', 'фа', 'соль', 'до', 'ре', 'фа', 'ля', 'си']
notes = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
n = sorted(note, key=notes.index)
print(*n)


# 316
import sys

# считывание списка из входного потока (не меняйте переменную lst_in в программе)
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
a = [
    (
        [int(number), name, int(bal), zachet]
        if "Номер" not in number
        else [number, name, bal, zachet]
    )
    for number, name, bal, zachet in (x.split(";") for x in lst_in)
]
n = [1, 3, 2, 0]
t_sorted = tuple(tuple(sorted(x, key=lambda i: n.index(x.index(i)))) for x in a)


# 317
import sys

# считывание списка из входного потока (переменную lst_in не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))
# print(lst_in) #['Атос=лейтенант', 'Портос=прапорщик', "д'Артаньян=капитан", 'Арамис=лейтенант', 'Балакирев=рядовой']
# здесь продолжайте программу (используйте список строк lst_in)
military_ranks = [
    "рядовой",
    "сержант",
    "старшина",
    "прапорщик",
    "лейтенант",
    "капитан",
    "майор",
    "подполковник",
    "полковник",
]
lst_nonsort = [[name, rank] for name, rank in [x.split("=") for x in lst_in]]
# print(lst_nonsort)

lst = sorted(lst_nonsort, key=lambda x: military_ranks.index(x[1]))


# 318
def get_add(a, b):
    if type(a) in (int, float) and type(b) in (int, float):
        return a + b
    elif type(a) is str and type(b) is str:
        return a + b


# 319
def get_sum(it):
    return sum(filter(lambda x: type(x) is int, it))


# 320
def get_even_sum(it):
    return sum(filter(lambda x: type(x) is int and not x % 2, it))


# 321
def get_list_dig(lst):
    return [x for x in lst if type(x) in (int, float)]


# 322
s = input().split()

print(all(map(lambda x: not int(x) % 2, s)))


# 333
# put your python code here
s = list(map(float, input().split()))

print(any(map(lambda x: x < 0, s)))


# 334
def is_string(lst):
    return all(isinstance(x, str) for x in lst)


# 335
s = list(map(int, input().split()))

print("отчислен" if any(map(lambda x: x < 3, s)) else "учится")


# 336
import sys

# считывание списка из входного потока (переменную lst_in не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))  # ['# x o', 'x # x', 'o o #']

# здесь продолжайте программу (используйте список строк lst_in)
pole = [
    [y for y in x.split()] for x in lst_in
]  # [['#', 'x', 'o'], ['x', '#', 'x'], ['o', 'o', '#']]


def is_free(lst):
    return any(y == "#" for x in lst for y in x)


# 337
num = int(input())

# Включение четвертого бита (3-й индекс, начиная с 0)
result = num | 0b1000  # то же самое, что и num | 8

# Вывод результата
print(result)


# 338
flag = int(input())
print(flag & ~0b0010010)


# 339
# put your python code here
n = int(input())
print(n ^ 0b00001001)


# 340
# put your python code here
n = int(input())
print(n << 2)


# 341
# put your python code here
n = int(input())

print(n >> 1)


# 342
# put your python code here
key = 123

# Чтение зашифрованного слова из входного потока
encrypted_word = input()

# Расшифровка каждого символа
decrypted_word = "".join(chr(ord(char) ^ key) for char in encrypted_word)

# Вывод результата
print(decrypted_word)


# 343
def check_bits(num):
    # Проверяем 6-й бит (нумерация с 0) с помощью маски
    bit_6_set = (num & (1 << 6)) != 0
    # Проверяем 3-й бит (нумерация с 0) с помощью маски
    bit_3_set = (num & (1 << 3)) != 0

    # Если оба бита установлены, выводим "ДА", иначе - "НЕТ"
    if bit_6_set and bit_3_set:
        print("ДА")
    else:
        print("НЕТ")


# Чтение входного числа
num = int(input().strip())
check_bits(num)


# 344
def check_bits(num):
    # Создаем маски для проверки 5-го и 1-го битов
    bit_5_mask = 1 << 5  # Маска для 5-го бита (32 в десятичной системе)
    bit_1_mask = 1 << 1  # Маска для 1-го бита (2 в десятичной системе)

    # Проверяем, установлен ли 5-й бит
    bit_5_set = (num & bit_5_mask) != 0

    # Проверяем, установлен ли 1-й бит
    bit_1_set = (num & bit_1_mask) != 0

    # Если хотя бы один из битов установлен, выводим "ДА", иначе - "НЕТ"
    if bit_5_set or bit_1_set:
        print("ДА")
    else:
        print("НЕТ")


# Чтение входного числа
num = int(input().strip())
check_bits(num)


# 345
import random

# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# здесь продолжайте программу
a, b = input().split()
print(round(random.uniform(int(a), int(b)), 2))


# 346
import random

# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# здесь продолжайте программу
a, b = input().split()
print((random.randint(int(a), int(b))))


# 347
import random

# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# здесь продолжайте программу
lst = input().split()
print(random.choice(lst))


# 348
import sys
import random

# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# считывание списка из входного потока
lst_in = list(
    map(str.strip, sys.stdin.readlines())
)  # ['1 2 3 4', '5 6 7 8', '9 8 6 7']

# здесь продолжайте программу

s = [
    x.split() for x in lst_in
]  # [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '8', '6', '7']]
st = list(zip(*s))
random.shuffle(st)
st = list(zip(*st))
for i in st:
    print(*i)


# 349
import random

# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# здесь продолжайте программу

s = input().split()
print(*random.sample(s, 3))


# 350
import random

# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# здесь продолжайте программу
N = int(input())
# N = 10
P = [[0] * N for _ in range(N)]
k = 0
while k < 10:
    raw = random.randint(0, N - 1)
    pos = random.randint(0, N - 1)
    if raw % 2 == 0 and pos % 2 == 0 and P[raw][pos] != 1:
        P[raw][pos] = 1
        k += 1


# 351
cmd = input()


match cmd:
    case "top" | "Top" | "TOP":
        print(f"Команда {cmd.lower()}")
    case "bottom" | "Bottom" | "BOTTOM":
        print(f"Команда {cmd.lower()}")
    case "right" | "Right" | "RIGHT":
        print(f"Команда {cmd.lower()}")
    case "left" | "Left" | "LEFT":
        print(f"Команда {cmd.lower()}")


# 352
def get_data(value):
    match value:
        case bool() as v:
            return v
        case int() as v:
            return v
        case str() as v:
            return v
        case float() as v:
            return v
    return None


# 353
def get_data(value):
    match value:
        case bool() as v:
            return v
        case int() as v if v > 0:
            return v
        case str() as v:
            return v
        case float() as v if -100 <= v <= 100:
            return v
    return None


# 354
t = (int, str, str, float, int)
book = [t[i](x) for i, x in enumerate(input().split(","))]

match book:
    case _, author, name, *_:
        print("Yes")
    case _, author, name, float() as price, *_:
        print("Yes")
    case (_, author, name, int() as date, *_):
        print("Yes")
    case _, author, name, float() as price, int() as date, *_:
        print("Yes")
    case _:
        print("No")


# 355
t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]

match book:
    case (_, author, name) if len(author) >= 6 and len(name) >= 10:
        print("Yes")
    case (_, author, name, float() as price) if len(author) >= 6 and price > 0:
        print("Yes")
    case (_, author, name, int() as date, *_) if date >= 2020:
        print("Yes")
    case (_, author, name, float() as price, int() as date, *_) if (
        price > 0 and date >= 2020
    ):
        print("Yes")
    case _:
        print("No")


# 356
def parse_json(data):
    match data:
        # здесь прописывайте шаблон

        case {"access": bool(access), "id": ids, "data": list([date, *_])}:
            return (access, date)

    return None


json_data = {
    "id": 2,
    "access": False,
    "data": ["26.05.2023", {"login": "1234", "email": "xxx@mail.com"}, 2000, 56.4],
}


# 357
def parse_json(data):
    match data:
        case {
            "access": bool() as access,
            "data": [_, {"login": str() as login, "email": str(email)}, *_],
        } if access:
            return (login, email)
        case {"id": ids, "data": [_, {"login": login}, _, _]}:
            return ids, login

    return None


json_data = {
    "id": 2,
    "access": True,
    "data": ["26.05.2023", {"login": "1234", "email": "xxx@mail.com"}, 2000, 56.4],
}


# 358
