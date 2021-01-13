# List

# 지하철 칸별로 10명 20명 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30, ]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))  # 1 (index)

subway.append("하하")  # 항상 맨뒤에 추가
print(subway)

subway.insert(1, "정형돈")  # 유재석과 조세호 사이에 정형돈 삽입
print(subway)

subway.pop()  # 가장 마지막의 객체 삭제
print(subway)
subway.pop()  # 가장 마지막의 객체 삭제
print(subway)
subway.pop()  # 가장 마지막의 객체 삭제
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)  # 유재석, 조세호, 유재석
print(subway.count("유재석"))  # 2

# 정렬 가능
numList = [5, 2, 4, 3, 1]
numList.sort()
print(numList)
print(numList.reverse())
print(numList)
# 제거
numList.clear()
print(numList)

# 다양한 자료형 함께 사용 가능
mixList = ["유재석", 20, True]
print(mixList)

# 리스트 합성
numList = [5, 2, 4, 3, 1]
mixList = ["유재석", 20, True]
numList.extend(mixList)
print(numList)
