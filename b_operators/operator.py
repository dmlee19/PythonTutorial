# 연산자 간단한 수식
print(1+1)
print(3-1)
print(5*2)
print(6/2)

print(2**3)  # 2^3 (=8)
print(5 % 3)  # % 나머지 (=2)
print(10//3)  # // 몫 (=3)

print(10 > 3)  # True
print(4 >= 7)  # False
print(10 < 3)  # False
print(5 >= 5)  # True

print(3 == 3)  # True
print(4 == 2)  # False
print(3+3 == 6)  # True

print(1 != 3)  # True
print(not (1 != 3))  # False

# and 둘 다 만족
print((3 > 0) and (3 < 5))  # True
print((3 > 0) & (3 < 5))  # True

# or 둘 중에 하나만 만족
print((3 > 0) or (3 > 5))
print((3 > 0) | (3 > 5))  # True

print(5 > 4 > 3)  # True
print(5 > 4 > 7)  # False

number = 2 + 3 * 4
print(number)  # 14
number = number + 2
print(number)  # 16
number += 2
print(number)  # 18
number *= 2
print(number)  # 36
number /= 2
print(number)  # 18
number -= 2
print(number)  # 16
number %= 5
print(number)  # 1


