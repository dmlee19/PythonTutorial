def openAccount():
    print("새로운 계좌가 생성되었습니다.")

openAccount()

# 입금
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다".format(balance+money))
    return balance + money

# 출금
def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

def withdrawNight(balance, money):
    commission = 100
    return commission, balance - money - commission

balance = 0  # 잔액
balance = deposit(balance, 1000)
print(balance)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)

commission, balance = withdrawNight(balance, 500)
print("수수료는 {0}원이고, 잔액은 {1}원입니다.".format(commission, balance))



# 기본값
def profile(name, age, mainLang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, mainLang))

profile("유재석", "20", "Python")
profile("김태호", "25", "Java")

# 같은 학교, 같은 학년, 같은 반, 같은 수업
def profile(name, age=17, mainLang="Python"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, mainLang))


profile("유재석")
profile("김태호")


# 키워드
def profile(name, age, mainLang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, mainLang))


profile(name="유재석", mainLang="Python", age=27)
profile(mainLang="Python", age=31, name="김태호")


# 가변인자
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)


# 이름 : 유재석   나이 : 20        Python Java C C++ C#
profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# 이름 : 김태호   나이 : 27        Kotlin Swift
profile("김태호", 27, "Kotlin", "Swift", "", "", "")


def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()  # 줄바꿈


profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "Javascript")
# 이름 : 유재석   나이 : 20        Python Java C C++ C# Javascript
profile("김태호", 27, "Kotlin", "Swift")  # 이름 : 김태호   나이 : 27        Kotlin Swift
