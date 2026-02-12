import heapq #for the min heap since we want to pop the lowest cost, lowest f(n) = g(n)+h(n)
from helper import puzzle_build 
MOVES = {
    "Up" : (0),
    "Down"  :(0),
    "Left" : (0),
    "Right" : (0)
}

#0 represents the empty space in puzzle, State is the board,
State = ([],[],[])
default = ([1,2,3],
           (4,0,6),
           (7,5,8))
goal =  ([1,2,3],
         [4,5,6],
         [7,8,0])

# projectgoal is to develop one general search algorithim that can select 
#between UCS -> h(n) = 0, Misplaced-> H(n)= # of misplaced tiles, Manhattan-> h(n) = # of wrong tiles shiftings ++

class Node:
    state: int #for now
    g: int #cost so far, # of moves so far
    h: int #expected cost to goal
    f: int #f= g+h

def main():
    choice = input(("Welcome to an 8-piece Puzzle Solver!"
    "Please enter '1' if you would like to use the default puzzle or '2' to create your own. \n" ))
    if choice == '1':
        puzzle_build(default)
    if choice == '2':
        print("TODO")
    


if __name__ == "__main__":
    main()


#check if goal has been met 
def if_goal(state): 
    if state == goal:
        return True
    