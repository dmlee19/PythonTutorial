from random import *
# Random Function
# from random import *
print(random())  # 0.0 < 임의의 값 < 1.0
print(random()*10)  # 0.0 <= 임의의 값 < 10
print(int(random()*10))  # 0 <= 임의의 값 < 10
print(int(random()*10) + 1)  # 1 <= 임의의 값 < 11

print(int(random()*46) + 1)  # 1 <= 임의의 값 < 46

print(randrange(1, 46))  # 1 <= 임의의 값 < 46

print(randint(1, 45))  # 1 <= 임의의 값 <= 45

# Quiz
# 코딩 스터디 월 4회 중 3회 온라인 1회 오프라인
# 조건에 맞는 오프라인 모임 날짜 정하는 프로그램 작성
# 조건 1: 랜덤으로 날짜 뽑기
# 조건 2: 월별 날짜는 다름을 감안 최소 일수 인 28일 이내로 정함
# 조건 3: 매월 1~3일은 스터디 준비를 해야하므로 제외

# 출력 예제: 오프라인 스터디 모임 날짜는 매월 X일로 선정되었습니다.

dateOffline = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(dateOffline) + "일로 선정되었습니다.")