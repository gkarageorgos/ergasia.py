import json

dictionary = {}
with open("./data.txt", "r") as file:
    lines = file.readlines()
    keys = json.loads(lines[0]).keys()
    for key in keys:
        dictionary[key] = []
    for line in lines:
        d = json.loads(line)
        for key in keys:
            dictionary[key].append(d[key])
file.close()

print(keys)
k = input("Choose the key:")
print("min: " + str(min(dictionary[k])))
print("max: " + str(max(dictionary[k])))
