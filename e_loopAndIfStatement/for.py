print("대기번호 : 0")
print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

for waitingNum_1 in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waitingNum_1))  # 0, 1, 2, 3, 4

for waitingNum_2 in range(5):
    print("대기번호 : {0}".format(waitingNum_2))  # 0, 1, 2, 3, 4

for waitingNum_3 in range(1, 6):
    print("대기번호 : {0}".format(waitingNum_3))  # 1, 2, 3, 4, 5

avengers = ["아이언맨", "토르", "캡틴아메리카"]
for entry in avengers:
    print("{0}, 출동".format(entry))

# 한줄 For
# 출석번호 1 2 3 4 100씩 더하기로 함 => 101 102 103 104
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "Captain America", "Spider Man"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "Captain America", "Spider Man"]
students = [i.upper() for i in students]
print(students)

# Quiz
# 택시기사 50명과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램

# 조건 1: 승객별 운행 소요 시간은 5 ~ 50분 사이의 난수
# 조건 2: 당신은 소요 시간 5 ~ 15분사이의 승객만 매칭

# 출력문 예제
# [o] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [o] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)
# 총 탑승 승객 : 2 분

from random import *
passanger = list(range(1, 51))
driveTime = [int(random()*50)+1 for i in passanger]
match = 0
for i in passanger:
    if 5 <= driveTime[i-1] <= 15:
        message = "[o] {0}번째 손님 (소요시간:{1})".format(i, driveTime[i-1])
        match += 1
    else:
        message = "[ ] {0}번째 손님 (소요시간:{1})".format(i, driveTime[i-1])

    print(message)
print("총 탑승 승객 : " + str(match) + "분")