inp = int(input())
valid = False

while (inp%2==0):
    inp /= 2
    if inp == 1:
        valid = True
        break
if valid:
    print("YES")
else:
    print("NO")