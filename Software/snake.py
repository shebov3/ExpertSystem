inp = input().split()
n, m = int(inp[0]), int(inp[1])

string = ""

first = "#"*m
second = ("."*(m-1))+"#"
third = "#"+("."*(m-1))

lol = 1

for i in range(1,n+1):
    if i%2==1:
        string += first
    else:
        if lol == 1:
            string += second
            lol+=1
        else:
            string += third
            lol-=1
    string += "\n"
print(string[:-1])