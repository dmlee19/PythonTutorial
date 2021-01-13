# 중복 X 순서 X
mySet = {1, 2, 3, 3, 3}
print(mySet)

java = {"유재석", "김태호", "조세호"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python 모두 가능한 개발자)
print(java & python)  # 유재석
print(java.intersection(python))  # 유재석

# 합집합 (java를 할 수 있거나 python을 개발할 수 있는 개발자 )
print(java | python)
print(java.union(python))

# 차집합 (java O, python X)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 개발자 증가
python.add("김태호")
print(python)

# java를 까먹음
java.remove("김태호")
print(java)

# 자료 구조의 변경
# 카페
menu = {"커피", "우유", "주스"}
print(menu, type(menu))
menu = list(menu)
print(menu, type(menu))
menu = tuple(menu)
print(menu, type(menu))
menu = set(menu)
print(menu, type(menu))