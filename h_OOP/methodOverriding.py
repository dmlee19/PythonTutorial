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


# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 공격합니다. [공격력 {2}]".format(
            self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 일반 공중 유닛
class Flyable:
    def __init__(self, flyingSpeed):
        self.flyingSpeed = flyingSpeed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"
              .format(name, location, self.flyingSpeed))


# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flyingSpeed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 속도 = 0
        Flyable.__init__(self, flyingSpeed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 발키리: 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중유닛 체력, 공격력 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# [지상유닛이동]
# 벌쳐 : 11시 방향으로 이동합니다. [속도 10]

# 오버로딩을 통해서 move만 써서 지상유닛은 move 공중유닛은 fly 하도록 한다.

# battlecruiser.fly(battlecruiser.name, "9시") # 배틀크루저 : 9시 방향으로 날아갑니다. [속도 3]

battlecruiser.move("9시")
# [공중 유닛 이동]
# 배틀크루저 : 9시 방향으로 날아갑니다. [속도 3]
