# getting a slice
s = 'digipodium'
slice1 = s[4:7]
print(slice1)




 
s = 'knowledge'
slice1 = s[0:4]
slice2 = s[:4]
print(slice1)
print(slice2)



name = 'vijay denanath chauhan'
#firstname
firstname =name[:5]
print(firstname)
lastname = name[-7:]
print(lastname)
middlename = name[6:-8]
print(middlename)
even_index = name[::2]
print(even_index) 

print(name[:])#wont effect
print(name[::-1][:7][::-1])


