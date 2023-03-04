# 파일입출력 사용하는 이유
# : 파일로부터 데이터를 읽어와서 프로그램에 사용하기 위해서
#   프로그램에서 만든 데이터를 파일형태로 저장하기 위해서

# 파일열기모드
# w : 쓰기모드(덮어쓰기)
# a : 추가모드(이어쓰기)
# r : 읽기모드

# 1. 파일쓰기
file = open('./myvenv/Chapter09/data.txt','w',encoding='utf8')
file.write('1. 스타트코딩과 함께 파이썬 공부')
file.close()

# # 2. 파일추가
file = open('./myvenv/Chapter09/data.txt','a',encoding='utf8')
file.write('\n2. 비전공자도 정말 쉽게 배울 수 있습니다.')
file.close()

# 3. 파일읽기
file = open('./myvenv/Chapter09/data.txt','r',encoding='utf8')

# 3.1 파일 전체 읽기
data = file.read()
print(data)
file.close()

# 3.2 파일 한 줄 읽기
while True:
    data = file.readline()
    print(data, end="")
    if data == '':
        break
file.close()