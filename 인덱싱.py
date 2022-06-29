a = "Life is too short, You need Python"

print(a)
print(a[0])
print(a[1])
print(a[-1])#뒤로 간다
print(a[-2])
print(a[:8])#이상:미만:간격
print(a[2:8])
print(a[8:])
print(a[::2])#첨부터 끝까지 2간격으로 짝수번만
print(a[::3])
print(a[::-1])#뒤로 읽는다
print(a[::-2])

jumin = "990303-1401826"

print("성별 : "+jumin[7])
print("생년월일 : "+jumin[:6])
print("뒤 7자리 : "+ jumin[7:])
print("뒤 7자리 (뒤에부터)" + jumin[-7:])
