python = "Python is Amazing"
print(python.lower()) #소문자로 출력
print(python.upper()) #대문자로 출력
print(python[0].isupper()) #대문자이면 true
print(len(python)) #길이
print(python.replace("python","Java")) #python이라는 단어를 Java로 변경

index = python.index("n") #'n'의 인덱스 반환
print(index)
index = python.index("n",index+1) #index+1부터 찾는다 (두번째 n을 찾는 것)
print(index)

print(python.find("n"))
print(python.find("Java")) #find에서는 없으면 -1 반환
#print(python.index("Java")) #index에서는 없으면 오류 출력

print(python.count('n'))#'n'이 몇번 나오는지