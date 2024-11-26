magnets = int(input())

l = []

for i in range(1,magnets+1):
    num = int(input())
    l.append(num)

old = None
count = 1
for i in range(0,len(l)):
    if old:
        if old != l[i]:
            count += 1
    old = l[i]

print(count)