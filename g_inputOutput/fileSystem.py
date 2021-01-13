# 파일 입출력
scoreFile = open("score.txt", "w", encoding="utf8") # w: 쓰기 (덮어씀)
print("수학 : 0", file=scoreFile)
print("영어 : 50", file=scoreFile)
scoreFile.close()

scoreFile = open("score.txt", "a", encoding="utf8")  # a: 뒤에 이어 쓰기
scoreFile.write("과학 : 80")
scoreFile.write("\n코딩 : 100")
scoreFile.close()

scoreFile = open("score.txt", "r", encoding="utf8")
print(scoreFile.read())
scoreFile.close()

scoreFile = open("score.txt", "r", encoding="utf8")
print(scoreFile.readline(), end="")  # 첫번째 줄 읽고 커서는 다음줄로 이동
print(scoreFile.readline(), end="")  # 두번째 줄 읽고 커서는 다음줄로 이동
print(scoreFile.readline(), end="")  # 세번째 줄 읽고 커서는 다음줄로 이동
print(scoreFile.readline(), end="")  # 네번째 줄 읽고 커서는 다음줄로 이동
scoreFile.close()

# line 수를 모르는 경우, 라인을 이용해서 모든 내용 출력
scoreFile = open("score.txt", "r", encoding="utf8")
while True:
    line = scoreFile.readline()
    if not line:
        break
    print(line)
scoreFile.close()

scoreFile = open("score.txt", "r", encoding="utf8")
lines = scoreFile.readlines()  # list 형태로 저장
for line in lines:
    print(line, end="")
