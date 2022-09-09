import functools import reduce
import operator

x = [2,3,4,5,6,4,1,4]

# multiply all values of  x 

ans = reduce(operator.mul, x)
print(ans)

# same as
ans = 1
for i in x:
    ans *= i
print(ans)