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

door: "[" direction location "]"
direction: WORD "wall"
location: "->" WORD

end: "."

%import common.WORD
%import common.NUMBER
%import common.WS
%ignore WS
"""

def run_tree(t, env):
  if t.data == 'room_list':
    for child in t.children:
      run_tree(child, env)
  elif t.data == 'room':
    for child in t.children:
      run_tree(child, env)
    for i in env['already_made']:
        if(str(env['curr_id']) != i):
            y = str(env['curr_id'])
            env['room'] = room(str(env['curr_id']) , env['curr_room'], env['doors'])
            env['map'][str(env['curr_id'])] = env['room']
            print(env['doors'])
            env['already_made'].append(str(env['curr_id']))
            if(i == None):
                env['already_made'].remove(None)
            env['curr_room'] = None  
  elif t.data == 'id':
    for t in t.children:
      env['curr_id'] = t
  elif t.data == 'size':
    for t in t.children:
      env['size'].append(t)
    x = int(env['size'][0])
    y = int(env['size'][1])
    env['curr_room'] = makeHouse(x,y)
    env['size'].clear()
  elif t.data == 'door':
    for child in t.children:
      run_tree(child, env)
    env['doors'][str(env['direction'])] = str(env['location'])
  elif t.data == 'direction':
    for t in t.children:
      env['direction'] = t
  elif t.data == 'location':
    for t in t.children:
      env['location'] = t
  elif t.data == 'end':
      curr_location = env['map']['A']
      newRoom = True
      while(1):
         
          if (newRoom == True):
            printHouse(curr_location.outline)
          userInput = input("Where do you want to move: ").lower()
          
          if (userInput == "exit"):
              break
          if (curr_location.directions[userInput] != None):
            curr_location = env['map'][curr_location.directions[userInput]]
            newRoom = True
          else:
            print("No Door in that direction")
            newRoom = False
  else:
    raise SyntaxError("unknown tree")
  
parser = Lark(my_grammar)
program = "(A 10 by 10 [north wall -> B]) (B 20 by 10 [south wall -> A])."
parse_tree = parser.parse(program)
#print(parse_tree.pretty())
env = {
  'curr_id': 0,
  'size': [],
  'direction': None,
  'location': None,
  'curr_room': None,
  'room': None,
  'already_made': [None],
  'door_count': 0,
  'map': {},
  'doors': {
    "north": None,
    "south": None,
    "east": None,
    "west": None,
   } 
}
run_tree(parse_tree, env)


