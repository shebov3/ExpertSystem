import math

class vector():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distance(self, vec2) -> float:
        return math.sqrt((vec2.y-self.y)**2 + (vec2.x-self.x)**2)

    def __add__(self, vec):
        return vector(self.x+vec.x, self.y+vec.y)

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

def func():
    pass

array = list(map(int,input().split()))
vec1 = vector(array[0], array[1])
vec2 = vector(array[2], array[3])
vec3 = vector(array[4], array[5])

A, B, C = vec1.distance(vec2), vec2.distance(vec3), vec3.distance(vec1)
array = [A,B,C]
longestSide = max(array)
array.remove(longestSide)

if array[0]**2 + array[1]**2 == longestSide**2:
    print("RIGHT")
else:
    if func():
        print("ALMOST")
    else:
        print("NEITHER")