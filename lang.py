from lark import Lark
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

my_grammar = """
?start: room_list
room_list: room+ end

room: "(" id size door+  ")"
id: WORD
size: NUMBER "by" NUMBER

door: "[" direction "]"
direction: WORD "wall ->" WORD

end: "."

%import common.WORD
%import common.NUMBER
%import common.WS
%ignore WS
"""

def eval_door(door):
    door_pointer = {
        "north": None,
        "south": None,
        "east": None,
        "west": None,
    }
    for i in door:
        door_pointer[str(i.children[0].children[0])] = str(i.children[0].children[1])
    return (door_pointer)

def run_tree(t, env):
    if t.data == 'room_list':
        for child in t.children:
            run_tree(child, env)
    elif t.data == 'room':
        holder = []
        for child in t.children:
            holder.append(child)
        for i in range(len(holder)):
            if(i == 0):
                id = holder[i].children[0]
            if(i == 1):
                width = holder[i].children[0]
                height = holder[i].children[1]
            if(i == 2):
                doors = []
                doors.append(holder[i])
            if(i >= 3):
                doors.append(holder[i])
        doors = eval_door(doors)
        r = room(str(id), makeHouse(int(width), int(height)), doors)
        env['map'][str(id)] = r
    elif t.data == 'end':
        curr_location = env['map']['A']
        newRoom = True
        while(1):
          if (newRoom == True):
            printHouse(curr_location.outline)
          print("Your map", curr_location.directions)
          userInput = input("Where do you want to move: ").lower()
          if (userInput == "exit"):
              break
          elif (curr_location.directions[userInput] != None):
            curr_location = env['map'][curr_location.directions[userInput]]
            newRoom = True
          else:
              print("No Door in that direction")
              newRoom = False
    else:
        raise SyntaxError("unknown tree")


parser = Lark(my_grammar)
program = """
(A 10 by 15 [north wall -> B]) (B 5 by 10 [south wall -> A] [east wall -> C]) (C 5 by 5 [west wall -> B]).
"""

env = {
    'map': {}
}
parse_tree = parser.parse(program)
#print(parse_tree.pretty())
print(run_tree(parse_tree, env))
