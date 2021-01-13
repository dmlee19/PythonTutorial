
class Unit:
    # __init__ : 생성자
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상유닛이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(
            self.name, location, self.speed))


# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)  # 다중 상속을 하는 경우에 사용
        super().__init__(name, hp, 0)       # 단일 상속의 경우에 사용
        # super뒤 () 추가, 매개변수에 self 제외
        self.location = location
