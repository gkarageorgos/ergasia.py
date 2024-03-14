number = ord("c")
binary = bin(number)[2:]
binary = (7 - len(binary))*"0" + binary
print(binary)
print(binary[:2] + binary[-2:])
print([ord(i) for i in ['b', 'a', 's']])