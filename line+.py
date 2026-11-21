f = open("sample.txt", "r")

lines = []

for line in f:
    lines.append(line.strip())

print("List:", lines)

f.close()
