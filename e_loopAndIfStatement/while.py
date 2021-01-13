customer = "토르"
index = 5

while index >= 1:
    print("{0}님 커피가 준비 되었습니다. {1}번 남았어요".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# # 무한 루프
# while True:
#     print("{0}님 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index += 1
# # ctrl + c 로 무한 루프 탈출

customer = "토르"
person = "Unknown"

while person != customer:
    print("{0}님 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")

# 토르가 입력되면 false => 반복문 종료

# break vs continue (해당 반복문 실행하지 않고 다음 반복문으로)
absent = [2, 5]  # 결석
noBook = [7]  # 책 안가져옴
for student in range(1, 11):
    if student in absent:
        continue
    elif student in noBook:
        print("오늘 수업 여기까지 {0}번, 교무실로 따라와".format(student))
        break
    print("{0}번, 책 읽어봐".format(student))


