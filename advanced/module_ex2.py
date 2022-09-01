from random import random
from random import randint,choice,shuffle,choices

val = random()
print(val)

for i  in range(10):
    val = randint(1,10)
    print(val,end='')

nums = []
for i in range(10):
    nums.append(randint(1,1000))
print("/n",nums)

nums =['🐴','🐸','🐼','🐨','🦝','🐮','🐵','🐶']

sel_ani = choice('animals')
print(f'selected animal:{sel_ani}')

sel_3_anim = choices(animals, k=3)
print(f'selected 3 animals:{" ".join(sel_ani)}')
shuffle (animals)
print(f'shuffled animals ')