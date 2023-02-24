# 상속 
# : 클래스들에 중복된 코드를 제거하고 유지보수를 편하게 하기위해서 사용

# 부모클래스
class Monster:
    def __init__(self,name,health,attack):
        self.name = name
        self.health = health
        self.attack = attack
    def move(self):
        print(f"{self.name} 지상에서 이동하기")

# 자식 클래스
class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self): # 메소드 오버라이딩
        print(f"{self.name} 헤엄치기")

class Dragon(Monster):
    def move(self):
        print(f"{self.name} 날기")

wolf = Wolf("울프",1500,200)
wolf.move()

shark = Shark("샤크",3000,400)
shark.move()

dragon = Dragon("드래곤",4000,600)
dragon.move()