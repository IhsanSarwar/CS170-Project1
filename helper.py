
def puzzle_build(initial_s):
     algorithm_choice = input("Select '1' for UCS, '2' for Misplaced Tiles, and '3' for Manhattan Tiles")
     if algorithm_choice == '1':
       print("Choosing UCS")
       general_search(initial_s,zero_heuristic)
     if algorithm_choice == '2':
         print("Choosing Misplaced")
         general_search(initial_s,2)
     if algorithm_choice == '3':
         print("Choosing Manhattan")
         general_search(initial_s,3)

def general_search(initial_state, choice):
    return 0



def zero_heuristic(state):
    return 0

def misplaced_heurisitc(state):
    cost = 1+1 #TODO develop this to count how many tiles are in the wrong place
    return cost

def manhattan_heurisitc(state):
    cost = 1+1 #TODO develop this to count how many moves needed to get each piece in the right place, total
    return cost
