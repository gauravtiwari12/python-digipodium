name = ['gaurav tiwari','vipin tiwari','shikha tiwari']
initials = [n.split()[0]+n.split([-1])]

for name in name :
    parts = name.split()
    initials.append(parts[0][0]+parts[-1][0])
    print(initials)