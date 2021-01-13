class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")


# 모듈 직접 실행 (모듈 테스트)
# 모듈을 직접 실행하는지 외부에서 실행하는지 확인 가능
if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    tripTo = ThailandPackage()
    tripTo.detail()
else:
    print("Thailand 외부에서 호출")
