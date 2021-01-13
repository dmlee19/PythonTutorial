# # Quiz
# 파이썬 코딩 대회
# 참석률 높이기 위한 댓글 이벤트
# 댓글 작성자 추첨 1명은 치킨, 3명은 커피 쿠폰
# 추첨 프로그램 작성

# 조건 1: 편의상 댓글은 20명이 작성, 아이디 1~20으로 가정
# 조건 2: 댓글 내용과 상관없이 무작위로 추첨, 중복 불가능
# 조건 3: random 모듈의 shuffle과 sample을 활용

# 출력예제
# -- 당첨자 발표--
# 치킨 당첨자: 1
# 커피 당첨자: [2, 3, 4]
# -- 축하합니다. --

# 활용 예제
from random import *
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
users = list(range(1, 21))  # 1<= users <21
print(type(users))
print(users)
# print(lst)
shuffle(users)
winners = sample(users, 4)
print(type(winners))
chicken = winners[0]
coffee = winners[1:]
print(f"--당첨자 발표--\n치킨당첨자:{chicken}\n커피 당첨자{coffee}\n--축하합니다--")
