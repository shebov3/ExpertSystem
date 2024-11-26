class vector():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def __add__(self, vec):
        return vector(self.x+vec.x, self.y+vec.y)
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

rows, cols = tuple(map(int,input().split(" ")))

matrix = []
array = []
critical = set()
dirChanged = True

for col in range(0,rows):
    matrix.append(list(map(int,input().split())))

num = vector(-1,0)
dirSequence = [vector(1,0), vector(0,-1), vector(-1,0), vector(0,1)]
currentDir = 0

while len(array) < rows*cols:
    num += dirSequence[currentDir]
    element = matrix[-num.y][num.x]
    if dirChanged == True:
        critical.add((-num.y,num.x))
    array.append(element)
    next = num + dirSequence[currentDir]
    dirChanged = False
    if next.y == -rows or next.x == cols or next.x < 0:
        currentDir = (currentDir+1)%len(dirSequence)
        dirChanged = True
    elif (-next.y,next.x) in critical:
        currentDir = (currentDir+1)%len(dirSequence)
        dirChanged = True

print(' '.join([str(element) for element in array]))
