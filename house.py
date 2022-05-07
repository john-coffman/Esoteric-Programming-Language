from dataclasses import dataclass

@dataclass
class room:
    id: int
    outline: list
    directions: dict

asciiChar = "@"
def makeHouse(w,h):
    top = []
    bottom = []
    side = []
    twoDHouse = []
    for x in range(w):
        top.append(asciiChar)
        bottom.append(asciiChar)
    for y in range(w):
        if(y == 0): side.append(asciiChar)
        elif(y == w-1): side.append(asciiChar)
        else: side.append(" ")
    for u in range(h):
        if(u == 0): twoDHouse.append(top)
        elif(u == h-1): twoDHouse.append(bottom)
        else: twoDHouse.append(side)
    return twoDHouse

def printHouse(house):
    for i in house:
        print(i)

def addDoor(room, wall, spot, height):
    if(wall == "north"): room[0][spot] = '#'
    elif(wall == "south"): room[height-1][spot] = '#'
    elif(wall == "west"): room[spot][0] = '#'
    elif(wall == "east"): room[spot][0] = '#'

A = makeHouse(15,14)
B = makeHouse(10,10)
C = makeHouse(4,4)

doors = {
    "north": None,
    "south": "B",
    "east": None,
    "west": None,
}
doors1 = {
    "north": "A",
    "south": None,
    "east": "C",
    "west": None,
}
doors2 = {
    "north": None,
    "south": None,
    "east": None,
    "west": "B",
}

r = room("A", A, doors)
r1 = room("B", B, doors1)
r2 = room("C", C, doors2)

map = {
    "A": r,
    "B": r1,
    "C": r2,
    }
curr_location = map["A"]
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
