class dog:

    breed = ''
    age = 0
    color = ''
    weight = 0
    gender = ''
    height = ''

    def bark(self):
        print('🐶 bow'*3)

    def wag(self):
        print('wags tail')

    def eat(self , food ):
        print(f'dog {food} kha raha h')

tommy = dog() # calling the costructor
tommy.age = 3
tommy.breed = 'street dog'
tommy.color = 'white'
tommy.weight = 10
tommy.gender = 'male'
tommy.height = '5 foot'



print(tommy.age, tommy.weight , tommy.breed , tommy.color)




