# Class
# # 마린 : 공격, 군인, 총을 쏜다.
# name = "마린"   # 이름
# hp = 40         # 체력
# damage = 5      # 공격력

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력{1}\n".format(hp, damage))

# # 탱크 (일반/시즈)
# tankName = "탱크"
# tankHp = 150
# tankDamage = 35

# print("{0} 유닛이 생성되었습니다.".format(tankName))
# print("체력 {0}, 공격력{1}\n".format(tankHp, tankDamage))

# # 탱크 추가
# tank2Name = "탱크"
# tank2Hp = 150
# tank2Damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank2Name))
# print("체력 {0}, 공격력{1}\n".format(tank2Hp, tank2Damage))


# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 공격을 합니다. [공격력: {2}]".format(name, location, damage))


# attack(name, "1시", damage)
# attack(tankName, "1시", tankDamage)
# attack(tank2Name, "1시", tank2Damage) # 계속해서 추가하기 번거로움 중복 코드 증가

# class Unit:
#     # __init__ : 생성자
#     def __init__(self, name, hp, damage):
#         self.name = name        # 멤버 변수
#         self.hp = hp            # 멤버 변수
#         self.damage = damage    # 멤버 변수
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# # 레이스 공중 유닛, 비행기, 클로킹
# wraith1 = Unit("레이스", 80, 5)
# print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# # 마인트 컨트롤 : 상대방 유닛을 내 것으로 만듦
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True
# # 클래스 밖에서 멤버 변수 생성하여 사용 가능 (wraith2 에만 적용 (wraith1 clocking 없음))

# print("유닛이름 : {0}, 공격력 : {1}".format(wraith2.name, wraith2.damage))
# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# # Function
# class AttackUnit:
#     # __init__ : 생성자
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 공격합니다. [공격력 {2}]".format(
#             self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))


# # 파이어뱃 : 공격 유닛
# firebet1 = AttackUnit("파이어뱃", 50, 16)
# firebet1.attack("5시")
# # 두번 공격 받음
# firebet1.damaged(25)
# firebet1.damaged(25)

# 상속

# # 일반 유닛
# class Unit:
#     # __init__ : 생성자
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp


# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 공격합니다. [공격력 {2}]".format(
#             self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))


# # 파이어뱃 : 공격 유닛
# firebet1 = AttackUnit("파이어뱃", 50, 16)
# firebet1.attack("5시")
# # 두번 공격 받음
# firebet1.damaged(25)
# firebet1.damaged(25)

# 다중 상속 (부모 클래스 2 이상)

class Unit:
    # __init__ : 생성자
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
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
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flyingSpeed)


# 발키리: 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
