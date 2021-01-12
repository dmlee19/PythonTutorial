# 문자열

sentence = '나는 소년입니다'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

# 슬라이싱
# 필요한 정보만 잘라서 사용
jumin = "210104-3123456"
print("성별 : " + jumin[7])  # 3
print("생년 : " + jumin[0:2])  # 처음부터 2 전까지 (= 21)
print("생월 : " + jumin[2:4])  # 01
print("생일 : " + jumin[4:6])  # 04

print("생년월일 : " + jumin[0:6])  # 210104
print("생년월일 : " + jumin[:6])  # [0:6]과 동일 (= 210104)

print("뒤 7자리 : " + jumin[7:14])  # 3123456
print("뒤 7자리 : " + jumin[7:])  # [7:14]과 동일 (= 3123456)

print("뒤 7자리(뒤에서 부터) : " + jumin[-7:])  # 3123456
# 맨 뒤에서 자리 기준 -1 시작

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())  # 소문자로 출력
print(python.upper())  # 대문자로 출력

print(python[0].isupper())  # True
print(len(python))  # 17

print(python.replace("Python", "Java"))  # Java is Amazing

# index
index = python.index("n")
print(index)  # n이 몇번째에 있는지 (= 5)
index = python.index("n", index + 1)  # start 위치 지정 가능
print(index)  # n이 몇번째에 있는지 (= 15)

# find
print(python.find("n"))
print(python.find("Java"))  # 없는 문자 검색 시 -1
# print(python.index("Java")) # 없는 문자 검색 시 error

# count
print(python.count("n"))  # 원하는 문자가 몇번 나왔는지

# 문자열 포맷
print("a" + "b")  # ab
print("a", "b")  # a b

# 방법 1
print("나는 %d살 입니다." % 20)  # 나는 20살 입니다.
print("나는 %s을 좋아해요." % "파이썬")  # 나는 파이썬을 좋아해요.
print("Apple은 %c를 좋아해요." % "A")  # Apple은 A를 좋아해요.
# %s
print("나는 %s살 입니다." % 20)  # 나는 20살 입니다.
print("나는 %s을 좋아해요." % "파이썬")  # 나는 파이썬을 좋아해요.
print("Apple은 %s를 좋아해요." % "A")  # Apple은 A를 좋아해요.

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))  # 나는 파란색과 빨간색을 좋아해요.

# 방법 2
print("나는 {}살 입니다." .format(20))  # 나는 20살 입니다.
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))  # 나는 파란색과 빨간색을 좋아해요.
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))  # 나는 파란색과 빨간색을 좋아해요.
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))  # 나는 빨간색과 파란색을 좋아해요.

# 나는 20살이며, 빨간색을 좋아해요.
print("나는 {age}살이며, {color}색을 좋아해요." .format(age=20, color="빨간"))

# 방법 3 (v3.6 이상)
age = 20
color = "빨간"
print(f"나는{age}살이며, {color}색을 좋아해요.")  # 나는20살이며, 빨간색을 좋아해요.

# /n 줄 바꿈
print("백문이 불여일견\n백견이 불여일타")

# \" 문장내에서 " "를 사용할 때
# 출력문: 저는 "홍길동" 입니다.
# print("저는"홍길동"입니다.") # error
print('저는 "홍길동" 입니다.')  # 저는 "홍길동" 입니다.
print("저는 \"홍길동\" 입니다.")  # 저는 "홍길동" 입니다.
print('저는 \'홍길동\' 입니다.')  # 저는 '홍길동' 입니다.

# \\ : 문장내에서 \ 하나로 출력
# C:\Users\ldmld\OneDrive\Documents\projects_dmlee89\PythonTutorial
print("C:\\Users\\ldmld\\OneDrive\\Documents\\projects_dmlee89\\PythonTutorial")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")  # //커서를 앞으로 이동하여 덮어씀 (= PineApple)

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")  # RedApple

# \t : 탭
print("Red\tApple")  # Red   Apple

# Quiz
# 사이트 별로 비밀번호를 만들어주는 프로그램 작성
# 예 http://naver.com
# 규칙 1: http:// 부분은 제외 => naver.com
# 규칙 2: 처음 만나는 점 (.) 이후 부분은 제외 => naver
# 규칙 3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자내 'e' 갯수 + "!" 로 구성
#                          (nav)     (5)              (1)         (!)
# 예) 생성된 비밀번호 : nav51!

site = "http://naver.com"
site = "http://google.com"
site = "http://daum.net"
site = "http://youtube.com"
myStr = site.replace("http://", "")  # 규칙 1
myStr = myStr[:myStr.index(".")]    # 규칙 2
password = myStr[0:3] + str(len(myStr)) + str(myStr.count("e")) + "!"
print(f"{site}의 비밀번호는 {password}입니다.")
