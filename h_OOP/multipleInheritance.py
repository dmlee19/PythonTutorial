class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")


class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__() # 다중 상속의 모든 부모 클래스에 대해 초기화하는 것에 적절하지 않음
        Unit.__init__(self)
        Flyable.__init__(self)


# 드랍쉽
dropship = FlyableUnit()
# Unit 생성자 (Unit 상속을 먼저한 경우)
# Flyable 생성자 (Flyable 상속을 먼저한 경우)
# 각 클래스의 생성자를 호출한 경우
# Unit 생성자
# Flyable 생성자
