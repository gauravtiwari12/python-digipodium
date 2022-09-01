# syntax
#def fun_name[parameter]:
# statement
#[return expression]

from email.errors import MessageError


def hello():
    print('👋hello')
    print('world🌍')

#calling or  using
hello()
hello()

def greetings(messege):
    print('👋', messege)
greetings('world')
greetings('hola amingos')
greetings('banjour amis')
greetings('namaste dosto')

def calc_area(w,h):
    area = w*h
    print('area:',area)

calc_area(10,20)
calc_area(3,5)
calc_area(100,200)

#display
print(calc_area_v2(10,20))
print(calc_area_v2(3,5))

#storing return value is variable
ans = calc_area_v2(10,20)

#using return value in a expresssion
ans = calc_area_v2(3,5) + calc_area_v2(10,2)
print (ans)