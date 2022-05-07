# PL

(1) describes in detail the language you're parsing
The Language I am parsing is an English to ascii layout that resembles rooms.

To make a room you must give an string of id, a width and hieght of the room, followed by a door. 
Important every room must have a door
the syntax for this is (id size door)

To make a door you must give a direction the door leads and to what other room the door leads.
the syntax for this is [direction "wall" -> location]

You can have as many rooms and doors as you want but to end the program you must put a period which indicated that the
output can start for your program. 

After you write all the rooms and doors you want you will get an output of your first Room which has to have an id of "A"
you can then choose to move "North", "South","East", or "West" and to end this prompt simply enter "exit". Capitalization does not matter


(2) tells me any interesting things I should take note of in your grammar or code

*** rewrite since fixing the errors***

(3) gives me clear instructions on how to run your code from the command line. 

To run from command line it is a simple python script so 
python3 lang.py
should run the code for you
