# 조건문
# : 조건에 따라 실행할 명령이 달라 지는 것

origin_pass = "1234"
input_pass = input("패스워드를 입력해주세요>>>>")

if origin_pass == input_pass: 
    print("로그인 성공!")
elif input_pass == "": 
    print("아무것도 입력하지 않았습니다.")
else :
    print("로그인에 실패.")
    print("비밀번호를 확인해주세요")