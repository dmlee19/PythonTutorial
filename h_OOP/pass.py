# 건물
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


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass


# 서플라이 디폿 : 건물 1개 건물 = 8 유닛
# 오류 X pass 일단 넘어가겠다. (완성된 것 처럼 취급)
supplyDepot = BuildingUnit("서플라이 디폿", 500, "7시")


def gameStart():
    print("[알림] 새로운 게임을 시작합니다.")


def gameOver():
    pass


gameStart()
gameOver()
