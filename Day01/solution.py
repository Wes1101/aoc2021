out = 0

input = tuple(open("D:\\Privat\\Programming\\adventOfCode2021\\Day01\\input.txt", "r").read().split("\n"))

print('\n'.join(input))

leange = len(input)
print("Länge: ", leange)

rang = range(1, leange)
print("Range: ", rang)

for x in rang:
    #print("\n", input[x-1], "\n", input[x] ,"\n")
    if input[x] > input[x-1]:
        out += 1

print(out)

with open("output.txt", "w") as o:
    o.write(str(out))