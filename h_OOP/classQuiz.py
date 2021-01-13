# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하세요.
# (출력 예제)
# 총 3개의 매물
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
class House:
    # 매물 초기화
    def __init__(self, location, houseType, dealType, price, completionYear):
        self.location = location
        self.houseType = houseType
        self.dealType = dealType
        self.price = price
        self.completionYear = completionYear

    # 매물 정보 표시
    def showDetail(self):
        pass


class Apartment(House):
    def __init__(self, location, dealType, price, completionYear):
        House.__init__(self, location, "아파트", dealType, price, completionYear)

    def showDetail(self):
        print("{0} 아파트 {1} {2} {3}".format(
            self.location, self.dealType, self.price, self.completionYear))


class Officetel(House):
    def __init__(self, location, dealType, price, completionYear):
        House.__init__(self, location, "오피스텔", dealType, price, completionYear)

    def showDetail(self):
        print("{0} 오피스텔 {1} {2} {3}".format(
            self.location, self.dealType, self.price, self.completionYear))


class Villa(House):
    def __init__(self, location, dealType, price, completionYear):
        House.__init__(self, location, "빌라", dealType, price, completionYear)

    def showDetail(self):
        print("{0} 빌라 {1} {2} {3}".format(
            self.location, self.dealType, self.price, self.completionYear))


a1 = Apartment("강남", "매매", "10억", "2010년")
o1 = Officetel("마포", "전세", "5억", "2007년")
v1 = Villa("송파", "월세", "500/50", "2000년")

houses = []
houses.append(a1)
houses.append(o1)
houses.append(v1)

print("총 {0}개의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.showDetail()
