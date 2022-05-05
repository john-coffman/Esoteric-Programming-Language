import struct
from lark import Lark

my_grammar = """
?start: room_list
room_list: room+

room: "(" id size door+  ")"
id: WORD
size: NUMBER "by" NUMBER

door: "[" direction location "]"
direction: WORD "wall"
location: NUMBER "->" WORD

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
    env['num_rooms'] += 1
    for child in t.children:
      run_tree(child, env)
  elif t.data == 'id':
    for t in t.children:
      print(t)
  elif t.data == 'size':
    for t in t.children:
      print(t)
  elif t.data == 'door':
    print("found door")
    for child in t.children:
      run_tree(child, env)
  elif t.data == 'direction':
    for t in t.children:
      print(t)
  elif t.data == 'location':
    for t in t.children:
      print(t)
  else:
    raise SyntaxError("unknown tree")
  
parser = Lark(my_grammar)
program = "(A 50 by 40 [north wall 4 -> B]) (B 30 by 30 [east wall 4 -> C])"
parse_tree = parser.parse(program)
#print(parse_tree.pretty())

env = {
  'num_rooms': 0 
}
print(run_tree(parse_tree, env))
print(env)




