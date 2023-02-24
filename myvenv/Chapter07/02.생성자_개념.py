# 생성자 
# : 인스턴스를 만들 때 호출되는 메소드

class Monster:
    # 생성자
    # self는 인스턴스 자신, 메소드마다 무조건 self는 들어가야함
    def __init__(self,health,attack,speed) :
        self.health = health
        self.atttack = attack
        self.speed = speed

    def decrease_health(self,num):
        self.health -= num
    def get_health(self):
        return self.health

# 고블린 인스턴스 생성
goblin = Monster(800,120,300)
goblin.decrease_health(100)
print(goblin.get_health())

# 늑대 인스턴스 생성
wolf = Monster(1500,200,350)
wolf.decrease_health(1000)
print(wolf.get_health())
