# 튜플 개념
# : 읽기 전용 리스트
a = (3,4,5)
b = 3,4,5
c = 4,

# 리스트 => 튜플로 변환
e = tuple([3,4,5])
f = list(range(10))
g = tuple(f)

# 튜플 => 리스트로 변환
h = 3,4,5
i = list(h)


# 튜플 관련 함수
x = 5,6,7
print(max(x))
print(min(x))
print(sum(x))
print(x.count(x))
print(x.index(x))