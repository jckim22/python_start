# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예 http://naver.com

# http:// 부분은 제외
# 처음 만나는 점(.) 이후 부분은 제외
# 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

#내 풀이
site="http://daum.net"

print(site)

index=site.find('/')
indexDot=site.find('.')
site=site[index+2:indexDot]
print(site)

pwd=site[:3] + str(len(site)) + str(site.count('e'))+"!"

print(pwd)

#다른 풀이
url = "http://naver.com"
my_str = url.replace("http://","")
my_str= my_str[:my_str.index(".")]

pwd=my_str[:3] + str(len(site)) + str(site.count('e'))+"!"

print(pwd)