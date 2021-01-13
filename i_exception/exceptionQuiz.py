# Quiz) 항상 대기 손님이 있는 맛집 치킨집
#       자동 주문 시스템 제작
#       시스템 코드 확인 후 적절한 예외처리 구문 넣기

#       조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어오는 경우 ValueError로 처리
#               출력 : "잘못된 값을 입력하였습니다."
#       조건 2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#               치킨 소진 시 사용자 정의 에러[SoldOutError] 발생 시키고 프로그램 종료
#               출력 : "재고가 소진되어 더이상 주문을 받지 않습니다."

# [코드]
class SoldOutError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


chicken = 10
waiting = 1  # 홀 안에는 현재 만석, 대기번호 1부터 시작

while(True):
    try:
        if chicken == 0:
            raise SoldOutError("재고가 소진되어 더이상 주문을 받지 않습니다.")
        print("[남은치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리를 주문 하시겠습니까?: "))
        if order < 1:
            raise ValueError
        elif order > chicken:  # 남은 치킨 보다 많이 주문하는 경우
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError as ex:
        print(ex)
        break
