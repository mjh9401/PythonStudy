# 시퀀스 자료형
# :순서가 있는 자료형   
# 1.리스트
# 2.문자열 
# 3.range 객체 
# 4.튜플, 딕셔너리

# for 사용법
# for 변수 in 시퀀스 자료:
#   명령문

# range(10) : 0 ~ 9까지 숫자를 포함하는 range객체를 만들어 준다.

# for문
# - 리스트 사용
champions = ['티모','이즈리얼','리신']

for champion in champions:
    print("선택한 챔피언은",champion,"입니다.")

# - 문자열 사용
fighting_message = "자신감을 가지자! 나에게 한계란 없다!"

for word in fighting_message:
    print(word)

# range 객체사용
# range(10) -> 0 ~ 9까지 숫자를 포함하는 range객체가 나온다.
# range(시작, 끝+1, 단계)
for i in range(1,10,2):
    print(i)


# while
# : 보통 반복횟수가 정해지지 않았을 때 사용한다.

i = 5 #초기식
while i < 9:
    print(i,"번째 다짐, 나는 할수 있다.")
    i +=1

# 무한루프
# : 조건식에 True를 넣어서 항산 반복하게 만든 것

while True:
    x = input("종료하려면 exit를 입력하세요 >>>")
    if x == "exit":
        break