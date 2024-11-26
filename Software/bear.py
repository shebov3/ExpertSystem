inp = input()
l = inp.split()
limak = int(l[0])
bob = int(l[1])

LIMAK_MULTIPLIER = 3
BOB_MULTIPLIER = 2
year = 0

while (limak <= bob):
    limak *= LIMAK_MULTIPLIER
    bob *= BOB_MULTIPLIER
    year += 1

print(year)