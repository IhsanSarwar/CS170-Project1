import heapq

#0 represents the empty space in puzzle
default = ([1,2,3],
           (4,5,6),
           (7,0,8))
goal =  ([1,2,3],
         [4,5,6],
         [7,8,0])

#goal is to develop one general search algorithim that can select 
#between h(n) = 0, H(n)= #o of misplaced tiles, h(n) = # of wrong tiles shiftings ++
#f(n) = h(n) + g(n)


def main():
    choice = input(("Welcome to an 8-piece Puzzle Solver!"
    "Please enter '1' if you would like to use the default puzzle or '2' to create your own own \n" ))
    if choice == '1':
        general_search(default, 0)
    if choice == '2':
        print("TODO")



def general_search(initial_state, heursitic):
    algorithm_choice = input("Select '1' for UCS, '2' for Misplaced Tiles, and '3' for Manhattan Tiles")
    if algorithm_choice == '1':
       print("Choosing UCS")
    if algorithm_choice == '2':
         print("Choosing Misplaced")
    if algorithm_choice == '3':
         print("Choosing Manhattan")


if __name__ == "__main__":
    main()