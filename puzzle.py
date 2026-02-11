import heapq

#0 represents the empty space in puzzle
default = ([1,2,3],
           (4,0,6),
           (7,5,8))
goal =  ([1,2,3],
         [4,5,6],
         [7,8,0])

#goal is to develop one general search algorithim that can select 
#between h(n) = 0, H(n)= #o of misplaced tiles, h(n) = # of wrong tiles shiftings ++
#f(n) = h(n) + g(n)

class Node:
    state: State

def main():
    choice = input(("Welcome to an 8-piece Puzzle Solver!"
    "Please enter '1' if you would like to use the default puzzle or '2' to create your own own \n" ))
    if choice == '1':
        puzzle_build(default)
    if choice == '2':
        print("TODO")
    

def puzzle_build(initial_s):
     algorithm_choice = input("Select '1' for UCS, '2' for Misplaced Tiles, and '3' for Manhattan Tiles")
     if algorithm_choice == '1':
       print("Choosing UCS")
       general_search(initial_s,0)
     if algorithm_choice == '2':
         print("Choosing Misplaced")
         general_search(initial_s,0)
     if algorithm_choice == '3':
         print("Choosing Manhattan")
         general_search(initial_s,0)


def general_search(initial_state, heursitic):
    return 0


if __name__ == "__main__":
    main()


#check if goal has been met 
def if_goal(state): 
    if state == goal:
        return True
    