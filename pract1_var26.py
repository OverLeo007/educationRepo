from math import cos, degrees, radians, sin, asin
from itertools import combinations


def eq(a, b):
    if abs(a - b) < 0.000000000001:
        return True
    else:
        return False


# a, b, ang1 = map(int, input().split())
a, b, ab = 3, 5, 90
ab = radians(ab)
c = (a ** 2 + b ** 2 - 2 * a * b * cos(ab)) ** 0.5
bc = asin((a * sin(ab) / c))
ac = asin((b * sin(bc)) / a)
ab, bc, ac = degrees(ab), degrees(bc), degrees(ac)
print(a, b, c)
print(ab, bc, ac)
sides = (a, b, c)
angles = (ab, bc, ac)
sr_sid = list(combinations(sides, 2))

sn = 0
for i in sr_sid:
    if eq(*i):
        sn += 1

if sn == 1:
    print('Треугольник равнобедренный')
elif sn == 3:
    print('Треугольник равносторонний')
for i in angles:
    if eq(90, i):
        print('Треугольник прямоугольный')
        break
