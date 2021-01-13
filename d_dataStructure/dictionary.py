cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(100))

# print(cabinet[5]) # error 후 프로그램 종료
# print("hi")

print(cabinet.get(5))  # None
print(cabinet.get(5, "사용 가능"))  # 사용가능 (값이 없는 경우 사용하는 default 값)
print("hi")

print(3 in cabinet)  # True
print(5 in cabinet)  # False

cabinet1 = {"A-3": "유재석", "B-12": "김태호"}
print(cabinet1["A-3"])
print(cabinet1["B-12"])

# 새 손님
print(cabinet1)
cabinet1["A-3"] = "김종국"
cabinet1["C-20"] = "조세호"
print(cabinet1)

# 떠난 손님
del cabinet1["A-3"]
print(cabinet1)

# key만 출력
print(cabinet1.keys())

# value만 출력
print(cabinet1.values())

# key와 value
print(cabinet1.items())

# 전체 삭제
cabinet1.clear()
print(cabinet1)
