from itertools import product


product= input("what item did you buy")
price = float(input("how much did you pay"))
qty = int(input("how many did you buy?"))

print ('you purchased',qty,product,'for',price)
print(f'you purchased{qty} {product} for {price}')