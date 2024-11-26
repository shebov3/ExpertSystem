rooms = int(input())

def take_input():
    line = input().split()
    return int(line[0]), int(line[1])

available_rooms = 0

for i in range(1, rooms+1):
    people, room = take_input()
    if room - people > 1:
        available_rooms += 1

print(available_rooms)