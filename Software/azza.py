inp = input()
l = list(inp)
valid = 1
odd = False
if len(l)%2 == 1:
    odd = True

half = int(len(l)/2)
if odd:
    half = int((len(l)+1)/2)

for i in range(0,half):
    j = len(l)-i-1
    if l[i] == "?" and l[j] == "?":
        l[i] = "a"
        l[j] = "a"
    elif l[i] == "?" and l[j] != "?":
        l[i] = l[j]
    elif l[j] == "?" and l[i] != "?":
        l[j] = l[i]
    elif l[i] != l[j]:
        valid = -1
        break

l = ''.join(l)
if valid == -1:
    print(valid)
else:
    print(l)

