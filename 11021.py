# a=int(input())
# b=[list(map(int,input().split())) for _ in range(a)]

# for x in range(a):
#     print("Case #{}: {}".format(x+1,b[x][0]+b[x][1]))

import sys
num=int(input())

for i in range(num):
    a,b=map(int,sys.stdin.readline().split())
    print("Case #%d:"%(i+1),a+b)
