# Error 생성 Exception 처리
class BigNumberError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


try:
    print("한 자리 숫자 나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값: {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력했습니다.")
except BigNumberError as ex:
    print("오류: 한 자리 숫자만 입력하세요")
    print(ex)
# try 실행 시 Error 발생 여부와 상관없이 실행
finally:
    print("계산기를 이용해 주셔서 감사합니다.")
