a ="I eat %d apples." %3 
print(a)
day = "three"
number =10

a="I ate %d apples %s days" %(number,day)
print(a)
a="I ate %s apples %s days" %(number,day) #%s로 숫자도 가능
print(a)

a ="asdfsadf asdfsa df{}fsadfsadf".format("안녕")
print(a)
a ="asdfsadf asdfsa df{name}fsadfsadf".format(name="안녕")
print(a)

print("asdfsadfsadf{}safa{}s {age}df".format("안녕","ㅎ하이",age=4))

#방법 1
print("나는 %d살입니다." % 20)
print("나는 %s를 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요" % "A")

print("나는 %s 색과 %s 색을 좋아해요" %("파란","빨간"))

#방법 2
print("나는 {}살입니다.".format(20))
print("나는 {} 색과 {} 색을 좋아해요" .format("파란","빨간"))
print("나는 {0} 색과 {1} 색을 좋아해요" .format("파란","빨간")) #순서 상관없이 숫자 순서에 따라 출력
print("나는 {1} 색과 {0} 색을 좋아해요" .format("파란","빨간"))

#방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

#방법4
age=20
color ="빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")