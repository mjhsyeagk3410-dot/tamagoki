# 펫 한마리를 표현하는 클래스

class Pet:
    def __init__(self, name):
        self.name = name    # 이름 
        self.hunger = 30    # 배고픔 (0~100)
        self.happy = 70     # 행복도 (0~100)
        self.energy = 70    # 에너지 (0~100)

    # 공통 메서드
    def _clamp(self, value):
        # 값의 범위를 (0~100) 유지
        if (value < 0): return 0
        if (value > 100): return 100
        return value

    def _change(self, hunger=0, happy=0, energy=0):
        # 상태값은 반드시 이 메서드를 사용한다. 
        self.hunger = self._clamp(self.hunger + hunger)
        self.happy = self._clamp(self.happy + happy)
        self.energy = self._clamp(self.energy + energy)

    # 밥주기
    def feed(self):
        if self.hunger <= 10:
            print(f"{self.name}: 배불러요~")
            return False
        self._change(hunger=-30, happy=5)
        print(f"{self.name}에게 밥을 줬습니다. 냠냠!!")

    # 놀아주기

    # 잠자기

# ------ 테스트 코드 ------
choco = Pet("초코")
dubu = Pet("두부")

choco.feed()
choco.feed()
print(choco.name, "배고픔:", choco.hunger)