from ast import Lambda
from re import S


f = lambda x : x + x**2 #lamda expression

print(f)
ans = f(5)
print(ans)


for i in range(1,10):
    print(f(i))

g = lambda a,b : (a + b)
print(g(2,3))
print(g(2,2))
print(g(23,12))
print(g(2,12))