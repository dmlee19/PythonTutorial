import moduleTheater
moduleTheater.price(3)  # 3명이서 영화보러 갔을 때 가격
moduleTheater.priceMorning(4)  # 4명이서 조조영화보러 갔을 때 가격
moduleTheater.priceSoldier(5)  # 군인 5명이 영화보러 갔을 때 가격

import moduleTheater as mv
mv.price(3)  # 3명이서 영화보러 갔을 때 가격
mv.priceMorning(4)  # 4명이서 조조영화보러 갔을 때 가격
mv.priceSoldier(5)  # 군인 5명이 영화보러 갔을 때 가격

from moduleTheater import *
# from random import *
price(3)
priceMorning(4)
priceSoldier(5)

from moduleTheater import price, priceMorning
price(3)
priceMorning(4)
# priceSoldier(5) # NameError: name 'priceSoldier' is not defined

from moduleTheater import priceSoldier as price
price(5)  # 5명 군인 할인 가격은 20000원 입니다.
