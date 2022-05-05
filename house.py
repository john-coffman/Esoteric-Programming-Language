from dataclasses import dataclass

@dataclass
class room:
    id: int
    outline: list
    directions: dict

asciiChar = "@"

def makeHouse(w,h):
    top = []
    side = []
    twoDHouse = []
    for x in range(w):
        top.append(asciiChar)
    for y in range(w):
        if(y == 0): side.append(asciiChar)
        elif(y == w-1): side.append(asciiChar)
        else: side.append(" ")
    for u in range(h):
        if(u == 0 or u == h-1): twoDHouse.append(top)
        else: twoDHouse.append(side)
    return twoDHouse


def printHouse(house):
    for i in house:
        print(i)


A = makeHouse(15,14)
B = makeHouse(10,10)
C = makeHouse(4,4)



doors = {
    "north": None,
    "south": 1,
    "east": None,
    "west": None,
}
doors1 = {
    "north": 0,
    "south": None,
    "east": 2,
    "west": None,
}
doors2 = {
    "north": None,
    "south": None,
    "east": None,
    "west": 1,
}

r = room(0, A, doors)
r1 = room(1, B, doors1)
r2 = room(2, C, doors2)

map = [r, r1, r2]
curr_location = map[0]
newRoom = True
while(1):
    if (newRoom == True):
        printHouse(curr_location.outline)
    userInput = input("Where do you want to move: ")
    if (curr_location.directions[userInput] != None):
        curr_location = map[curr_location.directions[userInput]]
        newRoom = True
    else:
        print("No Door in that direction")
        newRoom = False
    
