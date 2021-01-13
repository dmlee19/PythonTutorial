from random import *

# 일반유닛


class Unit:
    # 생산 (생성자)
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    # 이동
    def move(self, location):
        print("[지상유닛이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(
            self.name, location, self.speed))

    # 공격 받음
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    # 공격
    def attack(self, location):
        print("{0} : {1} 방향으로 공격합니다. [공격력 {2}]".format(
            self.name, location, self.damage))


# 일반 공중 유닛
class Flyable:
    def __init__(self, flyingSpeed):
        self.flyingSpeed = flyingSpeed

    # 이동
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"
              .format(name, location, self.flyingSpeed))


# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flyingSpeed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 속도 = 0
        Flyable.__init__(self, flyingSpeed)

    # 이동
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩: 체력을 10 감소하고 일정 시간동안 이동 및 공격 속도 증가
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 사용할 수 없습니다.".format(self.name))


# 탱크
class Tank(AttackUnit):
    # 시즈모드: 탱크를 지상에 고정, 공격력 증가 (이동불가), 한번 개발하면 모든 탱크에 적용
    seizeDeveloped = False  # 시즈모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seizeMode = False

    def setSeizeMode(self):
        if Tank.seizeDeveloped == False:
            return
        # 시즈모드가 아닌경우 -> 시즈모드
        if self.seizeMode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seizeMode = True
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seizeMode = False


# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        # 클로킹 모드는 개발이 필요없다고 가정
        self.clocked = False  # 클로킹 모드 (해제상태)

    # 클로킹
    def clocking(self):
        if self.clocked == True:  # 클로킹 모드 -> 모드 해제
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else:   # 클로킹 모드 설정
            print("{0} : 클로킹 모드로 전환합니다.".format(self.name))
            self.clocked = True


# --- 게임 시작/종료 ---
def gameStart():
    print("[알림] 새로운 게임을 시작합니다.")


def gameOver():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")


# --- 게임 진행 ---
gameStart()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 부대 설정 (생성된 모든 유닛 append)
unitGroup1 = []
unitGroup1.append(m1)
unitGroup1.append(m2)
unitGroup1.append(m3)
unitGroup1.append(t1)
unitGroup1.append(t2)
unitGroup1.append(w1)

# 모든 유닛 이동
for unit in unitGroup1:
    unit.move("1시")

# 탱크 시즈 모드 개발
Tank.seizeDeveloped = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹)
for unit in unitGroup1:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.setSeizeMode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 그룹 1 공격
for unit in unitGroup1:
    unit.attack("1시")

# 그룹 1 피해
for unit in unitGroup1:
    unit.damaged(randint(5, 21))  # 공격은 난수로 지정 (from random import *) 5 ~ 20

# 게임 종료
gameOver()
