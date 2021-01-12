# 변수
print("우리집 강아지의 이름은 연탄이예요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집" + animal + "의 이름은" + name + "예요")
print(name + "는 " + str(age) + "살이며," + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

animal = "다람쥐"
name = "키키"
age = 2
hobby = "쳇바퀴"
is_adult = age >= 3
# 변수를 지정하면 필요한 변수만 바꿔서 출력이 가능
print("우리집" + animal + "의 이름은" + name + "예요")
print(name + "는 " + str(age) + "살이며," + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))
# ,로 연결할 수도 있다. 한칸 띄워서 출력
print("우리집", animal, "의 이름은", name, "예요")
print(name, "는", age, "살이며,", hobby, "을 아주 좋아해요")
print(name, "는 어른일까요? ", str(is_adult))

#  Quiz
# 변수형 station
# 변수 값 : 사당, 신도림, 인천공항 순서대로 입력
# 출력 문장: XX 행 열자가 들어오고 있습니다.

# station = "사당"
# station = "신도림"
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")