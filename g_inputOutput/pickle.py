import pickle
# pickle 가지고 있는 데이터를 pickle 파일에 저장해놓고 데이터 필요할 때 불러와서 사용 가능

profileFile = open("profile.pickle", "wb")  # w:쓰기, b: binary 타입 encoding 필요 X
profile = {"이름": "박명수", "나이": 30, "취미": ["EDM", "운전", "호통"]}
print(profile)
# pickle을 이용해서 파일에 쓰기
pickle.dump(profile, profileFile)   # profile에 정보를 file에 저장
profileFile.close()

# pickle file 정보 불러오기
profileFile = open("profile.pickle", "rb")
profile = pickle.load(profileFile)  # file에 있는 정보를 profile에 불러오기
print(profile)  # {'이름': '박명수', '나이': 30, '취미': ['EDM', '운전', '호통']}
profileFile.close()

# With
# 파일 열기, 처리, 닫기를 편하게
# import pickle

# 불러오기
with open("profile.pickle", "rb") as profileFile:
    print(pickle.load(profileFile))
# with를 사용하면 close 필요 X

# 쓰기 (파일생성)
with open("study.txt", "w", encoding="utf8")as studyFile:
    studyFile.write("파이썬 공부하고 있습니다.")

# 읽기
with open("study.txt", "r", encoding="utf8") as studyFile:
    print(studyFile.read())

# Quiz
# 회사에서 매주 1회 보고서 작성
# 출력 예제
# - X 주차 주간 보고 -
# 부서 :
# 이름 :
# 업무 요약 :
# 1주차 부터 50주차까지 보고서를 만드는 프로그램 작성
# 조건 : 파일명은 1주차.txt, 2주차.txt, ... 와 같이 만든다
for week in range(1, 51):
    with open(str(week)+"주차.txt", "w", encoding="utf8") as reportFile:
        reportFile.write("- "+str(week)+"주차 주간 보고-\n부서 : \n이름 : \n업무 요약 : ")
