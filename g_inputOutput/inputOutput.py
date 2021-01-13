# 표준 입출력

import sys
print("Python", "Java")             # Python Java
print("Python", "Java", sep=" ")    # Python Java
print("Python", "Java", sep=",")    # Python,Java
print("Python", "Java", sep=" vs ")  # Python vs Java

print("Python", "Java", sep=" vs ", end="?")  # print에 end를 정의하여 줄바꿈 기능이 없어진다.
print("무엇이 더 재미있을까요?")      # Python vs Java?무엇이 더 재미있을까요?

print("Python", "Java", file=sys.stdout)    # Python Java (표준출력)
print("Python", "Java", file=sys.stderr)    # Python Java (표준에러) 따로 처리 가능하게

# 시험 성적
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=" : ")
    # ljust(8): 8칸을 확보해서 왼쪽 정렬, rjust(4) 4칸을 확보해서 오른쪽 정렬
    # 수학       :    0
    # 영어       :   50
    # 코딩       :  100

# 은행 대기 순번표
# 001, 002, 003, 004, ....

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
    # 3칸을 확보 빈공간을 0으로 채움 (= 001, 002, 003)

answer = input("아무 값이나 입력하세요: ")
print(type(answer))  # 입력받는 값은 숫자 문자와 상관없이 str
print("입력하신 값은 {0} 입니다.".format(answer))

# 다양한 출력 포맷
# 빈 자리는 빈공간, 오른쪽 정렬, 총 10자리
print("{0: >10}".format(500))  # 500
# {0: >10} :" ":빈공간, >: 오른쪽 정렬, 10: 10칸 확보

# 양수 +로 음수 -로
print("{0: >+10}".format(500))  # +500
print("{0: >+10}".format(-500))  # -500

# 왼쪽 정렬, 빈칸 _로 채움
print("{0:_<10}".format(500))  # 500_______

# 3자리마다 , 찍기
print("{0:,}".format(11234412331))   # 11,234,412,331

# 3자리마다 ,  +/- 부호 추가
print("{0:+,}".format(11234412331))  # +11,234,412,331
print("{0:+,}".format(-11234412331))  # -11,234,412,331

# 3자리마다 ,  +/- 부호 추가, 자리수 추가, 빈자리 ^
print("{0:^<+20,}".format(102930420394))  # +102,930,420,394^^^^

# 소수점 출력
print("{0:f}".format(5/3))   # 1.666667

# 소수점 아래 2자리 (소수점 아래 3번째 자리에서 반올림)
print("{0:.2f}".format(5/3))  # 1.67
