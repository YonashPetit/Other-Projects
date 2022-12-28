#This inverts the orientation of the list from the initialize board function it prints it out in string format
def print_board(board):
    newlist = []
    for i in range(height):
        newlist.append([])
    for i in range(height):
        for c in range(length):
            newlist[i].append(board[c][-(i+1)])
    for i in range(height):
        print(" ".join(newlist[i]))

#creates a nested list consisting of "-" with each nested list in the mother list representing all of the "-'s" within a collum
#ie) the first element within the all of the nested lists would create the top row of the grid
def initialize_board(num_rows, num_cols):
    for i in range(num_rows):
        list.append([])
    for i in range(num_rows):
        for c in range(num_cols):
            list[i].append("-")
    return list
    pass

#This replaces "-" with either "x" or "o" depending on who's placing the chip
def insert_chip(board, col, chip_type):
    i = 0
    if chip_type == "x":
        while True:
            if list[col][i] == "-":
                list[col][i] = "x"
                break
            else:
                i += 1

    elif chip_type == "o":
        while True:

            if list[col][i] == "-":
                list[col][i] = "o"
                break
            else:
                i += 1
    return list


def check_if_winner(board, col, row, chip_type):
#Checks for who placed the chip and the winner conditions are decided based on that
#The first pair of if/elif statements tally up if one spefic token appears four times in a row, if so, that token type wins (only connect 4 vertically)
    tally_up = 0
    if chip_type == "x":
        for i in range(col):
            tally_up = 0
            for c in range(row):
                if board[i][c] == "x":
                    tally_up += 1
                if board[i][c] == "o":
                    tally_up = 0
            if tally_up == 4:
                print("\nPlayer 1 won the game!")
                StopGame = True
                return StopGame

    elif chip_type == "o":
        for i in range(col):
            tally_up = 0
            for c in range(row):
                if board[i][c] == "o":
                    tally_up += 1
                if board[i][c] == "x":
                    tally_up = 0
            if tally_up == 4:
                print("\nPlayer 2 won the game!")
                StopGame = True
                return StopGame

#This figures out if all of the "-" have been replaced with "x" or "o", and if so, it's a draw
    tally = 0
    for i in range(col):
        for c in range(row):
            if board[i][c] != "-":
                tally += 1
            if tally == col*row:
                print("Draw. Nobody wins.")
                StopGame = True
                return StopGame

#This figures out if there are four "x's" or "o's" horizontally
    tally_across = 0
    if chip_type == "x":
        for i in range(col-3):
            for c in range(row):
                if board[i][c] == "x" and board[i+1][c] == "x" and board[i+2][c] == "x" and board[i+3][c] == "x":
                    print("\nPlayer 1 won the game!")
                    StopGame = True
                    return StopGame

    elif chip_type == "o":
        for i in range(col - 3):
            for c in range(row):
                if board[i][c] == "o" and board[i + 1][c] == "o" and board[i + 2][c] == "o" and board[i + 3][c] == "o":
                    print("\nPlayer 2 won the game!")
                    StopGame = True
                    return StopGame

#if function containing all of the function calls and variables etc.
if __name__ == "__main__":
    #bunch of variables, inputs, initial calles etc
    list = []
    ContinueGame = True
    height = int(input("What would you like the height of the board to be? "))
    length = int(input("What would you like the length of the board to be? "))
    initialize_board(length, height)
    print_board(list)
    print("\nPlayer 1: x \nPlayer 2: o")

    #this is a loop which asks for the column each user wants to put thier token in; this loop will continue until the game ends via a win or draw
    while ContinueGame:
        #this is the logic that prompts player one to make their move, and for each of their moves, the check_if_winner function gets called to check if there's a winner
        print("")
        choose1= int(input("Player 1: Which column would you like to choose? "))
        insert_chip(list, choose1, "x")
        print_board(list)
        if check_if_winner(list, length, height, "x") == True:
            ContinueGame = False
            break

        # this is the logic that prompts player one to make their move, and for each of their moves, the check_if_winner function gets called to check if there's a winner
        print("")
        choose2= int(input("Player 2: Which column would you like to choose? "))
        insert_chip(list, choose2, "o")
        print_board(list)
        if check_if_winner(list, length, height, "o") == True:
            ContinueGame = False
            break







