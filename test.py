from dataclasses import dataclass

@dataclass
class room:
    id: int
    outline: list
    directions: dict

A = ["@","@","@","@","@","@"]
B = ["@"]
C = ["@","@", "@", "@", "@", "@", "@" ]
D = ["@", "@", "@", ]

rooms = {
    "north": None,
    "south": 1,
    "east": None,
    "west": None,
}
rooms1 = {
    "north": 0,
    "south": None,
    "east": 2,
    "west": None,
}
rooms2 = {
    "north": None,
    "south": None,
    "east": None,
    "west": 1,
}

r = room(0, A, rooms)
r1 = room(1, B, rooms1)
r2 = room(2, C, rooms2)

map = [r, r1, r2]
x = map[0]
while(1):
    print(x.outline)
    userInput = input()
    if (x.directions[userInput] != None):
        x = map[x.directions[userInput]]
        
