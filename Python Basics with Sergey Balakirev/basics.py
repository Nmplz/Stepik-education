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


# 81 УСЛОВНЫЕ ОПЕРАТОРЫ.
