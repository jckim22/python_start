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