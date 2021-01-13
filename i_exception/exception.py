# try를 실행하고 오류가 발생했을때, except에 대한 오류가 발생하면 해당 구현부를 실행
# try:
#     print("나누기 전용 계산기")
#     num1 = int(input("첫 번째 숫자를 입력하세요: "))
#     num2 = int(input("두 번째 숫자를 입력하세요: "))
#     print("{0} / {1} = {2}.{3}".format(num1,
#                                        num2, int(num1/num2), int(num1 % num2)))
# # 숫자 입력 시 한글을 입력하면 오류 발생(ValueError) --> 프로그램 종료
# except ValueError:
#     print("숫자는 1~0 의 숫자로만 입력해주세요")
# # 두번째 숫자(나누는 수)가 0인 경우 오류 발생(ZeroDivisionError) --> 프로그램 종료
# except ZeroDivisionError as ex:
#     print(ex)

try:
    print("나누기 전용 계산기")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요: ")))
    nums.append(int(input("두 번째 숫자를 입력하세요: ")))
    # nums.append(int(nums[0]/nums[1])) # 실수로 누락
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except:
#     print("알수 없는 오류가 발생했습니다.")
except Exception as ex:
    print("오류가 발생했습니다.")
    print(ex)  # 0: list index out of range
               # 숫자가 아닌 입력값 : invalid literal for int() with base 10: '입력문자'