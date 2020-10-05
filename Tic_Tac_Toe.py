import os

clear = lambda : os.system("cls")

def display_board(board):
    print("\n" *100)
    print("  "+" | " +"   "+" | "+"  ")
    print(" "+board[7]+" | " +" "+board[8]+" "+" | "+" "+board[9])
    print("  "+" | " +"   "+" | "+"  ")
    print(" -----------")
    print("  "+" | " +"   "+" | "+"  ")
    print(" "+board[4]+" | " +" "+board[5]+" "+" | "+" "+board[6])
    print("  "+" | " +"   "+" | "+"  ")
    print(" -----------")
    print("  "+" | " +"   "+" | "+"  ")
    print(" "+board[1]+" | " +" "+board[2]+" "+" | "+" "+board[3])
    print("  "+" | " +"   "+" | "+"  ")

def player_input():
    marker =""
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
        board[position]=marker

def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3]==mark)or
           (board[4] == mark and board[5] == mark and board[6]==mark)or
           (board[9] == mark and board[8] == mark and board[7]==mark)or
            (board[1] == mark and board[5] == mark and board[9]==mark)or
           (board[7] == mark and board[5] == mark and board[3]==mark)or 
           (board[1] == mark and board[4] == mark and board[7]==mark)or 
           (board[9] == mark and board[6] == mark and board[3]==mark))

import random
def choose_first():
    if random.randint(1,2) == 1:
        print("player 1 will go first")
        return "Player 1"
    else:
        print("player 2 will go first")
        return "Player 2"
    
def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for x in board:
        if x!=" ":
            return True
        else:
            return False

def player_choice(board):
    p_input  = int(input("Enter you Move(1-9): "))
    if space_check(board,p_input):
        return p_input

def replay():
    p_choice = input("Do you want to Continue : Y or N")
    if p_choice.upper() == "Y":
        return True
    else:
        return False

print('Welcome to Tic Tac Toe!')
while True:
    board=[" "]*10
    p1_sign,p2_sign = player_input()
    pl_turn = choose_first()

    game_on=True
    play_on=input("Are you ready to Play Yes or No: ")
    if play_on.upper() == "YES":
        game_on = True
        

        while game_on:
            if pl_turn == "Player 1":
                
                display_board(board)
                print("asking player 1"+ p1_sign)
                position = player_choice(board)
                
                if space_check(board,position):
                    place_marker(board,p1_sign,position)
                else:
                    print("ALready Taken")
                
                if win_check(board,p1_sign):
                    print(f"Congrats {pl_turn} wins")
                    display_board(board)
                    game_on = False
                else:
                    if full_board_check(board):
                        print("Draw!!")
                        break
                    else:
                        pl_turn = "Player 2"

            else:
                
                display_board(board)
                print("asking player 2"+ p2_sign)
                position = player_choice(board)
                
                if space_check(board,position):
                    place_marker(board,p2_sign,position)
                else:
                    print("ALready Taken")
                
                if win_check(board,p2_sign):
                    print(f"Congrats {pl_turn} wins")
                    game_on = False
                else:
                    if full_board_check(board):
                        print("Draw!!")
                        break
                    else:
                        pl_turn = "Player 1"

    if not replay():
        break