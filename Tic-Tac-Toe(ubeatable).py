#AYESHA
#SP21-BAI-009
#ARTIFICAL INTELLEGENCE
#*ALL CONDITIONS OF PROJECT ARE FULLFILED WITH COMMENTS BESIDE THEM*
#---------------------------------------------------------------------------------------------------#
# CHECKING IF USER ENTER RIGHT BOX NUMBER
# HUMAN MOVE
def Humanmove(board):
    print(player, end=" ")
    Box = input("Enter your move, between 1-9: ")
    if Box.isdigit() == False:
        # IF USER ENTER OTHER THEN INTEGR
        print("Please enter an integer:")
        Humanmove(board)
    elif int(Box) > 9 or int(Box) < 1:
        # IF USER ENTER NUMBER OUT OF RANGE
        print("Enter a number between 1 and 9:")
        Humanmove(board)
    # IF USER SELECT ALREADY OCCUPIED BOX
    elif int(Box) == 1:
        if (board[0][0] == S1 or board[0][0] == S2):
            print("Box is already occupied,choose any other box")
            Humanmove(board)
        else: 
            board[0][0] = S1
    elif int(Box) == 2:
        if (board[0][1] == S1 or board[0][1] == S2):
            print("Box is already occupied,choose any other box")
            Humanmove(board)
        else:
            board[0][1] = S1
    elif int(Box) == 3: 
        if (board[0][2] == S1 or board[0][2] == S2):
            print("Box is already occupied,choose any other box")
            Humanmove(board)
        else:
            board[0][2] = S1
    elif int(Box) == 4:
        if (board[1][0] == S1 or board[1][0] == S2):
            print("Box is already occupied,choose any other box")
            Humanmove(board)
        else:
            board[1][0] = S1
    elif int(Box) == 5:
        if (board[1][1] == S1 or board[1][1] == S2):
            print("Box is already occupied,choose any other box")
            Humanmove(board)
        else:
            board[1][1] = S1
    elif int(Box) == 6:
        if (board[1][2] == S1 or board[1][2] == S2):
            print("Box is already occupied,choose any other box")
            Humanmove(board)
        else:
            board[1][2] = S1
    elif int(Box) == 7:
        if (board[2][0] == S1 or board[2][0] == S2):
            print("Box is already occupied,choose any other box")
            Humanmove(board)
        else:
            board[2][0] = S1
    elif int(Box) == 8: 
        if (board[2][1] == S1 or board[2][1] == S2):
            print("Box is already occupied,choose any other box")
            Humanmove(board)
        else:
            board[2][1] = S1
    elif int(Box) == 9:
        if (board[2][2] == S1 or board[2][2] == S2):
            print("Box is already occupied,choose any other box")
            Humanmove(board)
        else:
            board[2][2] = S1

# MAKING COMPUTER MOVE BY LOGICS
def computermove(board, computerturn):
    moved = False
    # TURNDONE IS CONDITION FOR COMPUTER MOVES

    def cornermove(board, moved):
        # SELF EXPLANATORY MOVE CHOOSE A CORNER
        if not moved:
            if board[0][0]==S1 and board[2][1]==S1 and board[2][0]=="_":
                board[2][0]=S2        
            elif board[0][2]==S1 and board[2][1]==S1 and board[2][2]=="_":
                board[2][2]=S2
            elif board[0][0] == "_":
                board[0][0] = S2
                moved = True
            elif board[0][2] == "_":
                board[0][2] = S2
                moved = True
            elif board[2][0] == "_":
                board[2][0] = S2
                moved = True
            elif board[2][2] == "_":
                board[2][2] = S2
                moved = True
            else:
                sidemove(board,moved)
                
    def sidemove(board,moved):
        if moved == False:
            if board[0][1] == "_":
                board[0][1] = S2
                moved = True
            elif board[1][0] == "_":
                board[1][0] = S2
                moved = True
            elif board[1][2] == "_":
                board[1][2] = S2
                moved = True
            elif board[2][1] == "_":
                board[2][1] = S2
                moved = True
            else:
                cornermove(board, moved)
 #POINT#2
 #You have to make sure that either computer wins or the game is a draw. Your logic should not let player win the game.
    # IF USER DON'T SELECT CENTER COMPUTER SELECT CENTER PLACE
    if computerturn == 1:
        if board[1][1] != S1:
            board[1][1] = S2
            moved = True
        else:
            cornermove(board, moved)
            moved = True
    # IF CENTER IS TAKEN COMPUTER CHOOSE A CORNER
    else:
        # MAKING SURE IF TWO BOX ARE FILLED BY COMPUTER THEN IF FILLS THE THIRD ONE
        # LOGIC#1 PART(A)                           
        # 1 =(0, 3, 6), ,,,,,,
        if board[0][0] == S2 and board[1][0] == S2 and board[2][0] == "_":
            board[2][0] = S2
            moved = True
        #2=(1, 4, 7)
        elif board[0][1] == S2 and board[1][1] == S2 and board[2][1] == "_":
            board[2][1] = S2
            moved = True
        #3=(2, 5, 8)
        elif board[0][2] == S2 and board[1][2] == S2 and board[2][2] == "_":
            board[2][2] = S2
            moved = True
        #4=(0, 1, 2)
        elif board[0][0] == S2 and board[0][1] == S2 and board[0][2] == "_":
            board[0][2] = S2
            moved = True
        #5=(3, 4, 5)
        elif board[1][0] == S2 and board[1][1] == S2 and board[1][2] == "_":
            board[1][2] = S2
            moved = True
        #6=(6, 7, 8)
        elif board[2][0] == S2 and board[2][1] == S2 and board[2][2] == "_":
            board[2][2] = S2
            moved = True
        #7=(0, 4, 8)
        elif board[0][0] == S2 and board[1][1] == S2 and board[2][2] == "_":
            board[2][2] = S2
            moved = True
        #8=(2, 4, 6)
        elif board[0][2] == S2 and board[1][1] == S2 and board[2][0] == "_":
            board[2][0] = S2
            moved = True
        # LOGIC#1 PART(B)
        # 1=(3,6,0),2=( 4,7,1),3=(5, 8,2),4=(1, 2,0),5=(4, 5,3),6=(7, 8,6),7=(4, 8,0),8=(4, 6,2)
        elif board[1][0] == S2 and board[2][0] == S2 and board[0][0] == "_":
            board[0][0] = S2
            moved = True
        #2=( 4,7,1)
        elif board[1][1] == S2 and board[2][1] == S2 and board[0][1] == "_":
            board[0][1] = S2
            moved = True
        #3=(5, 8,2)
        elif board[1][2] == S2 and board[2][2] == S2 and board[0][1] == "_":
            board[0][1] = S2
            moved = True
        #4=(1, 2,0)
        elif board[0][1] == S2 and board[0][2] == S2 and board[0][0] == "_":
            board[0][0] = S2
            moved = True
        #5=(4, 5,3)
        elif board[1][1] == S2 and board[1][2] == S2 and board[1][0] == "_":
            board[1][0] = S2
            moved = True
        #6=(7, 8,6)
        elif board[2][1] == S2 and board[2][2] == S2 and board[2][0] == "_":
            board[2][0] = S2
            moved = True
        #7=(4, 8,0)
        elif board[1][1] == S2 and board[2][2] == S2 and board[0][0] == "_":
            board[0][0] = S2
            moved = True
        #8=(4, 6,2)
        elif board[1][1] == S2 and board[2][0] == S2 and board[0][2] == "_":
            board[0][2] = S2
            moved = True
        # LOGIC#1 PART(C)
        # 1=(0,6,3) 2=(1,7,4) 3=(2,8,5) 4=(0,2,1) 5=(3,5,4) 6=(6,8,7) 7=(0,8,4) 8=(2,6,4)
        elif board[0][0] == S2 and board[2][0] == S2 and board[1][0] == "_":
            board[1][0] = S2
            moved = True
        #2=(1,7,4)
        elif board[0][1] == S2 and board[2][1] == S2 and board[1][1] == "_":
            board[1][1] = S2
            moved = True
        #3=(2,8,5)
        elif board[0][2] == S2 and board[2][2] == S2 and board[1][2] == "_":
            board[1][2] = S2
            moved = True
        #4=(0,2,1)
        elif board[0][0] == S2 and board[0][2] == S2 and board[0][1] == "_":
            board[0][1] = S2
            moved = True
        #5=(3,5,4)
        elif board[1][0] == S2 and board[1][2] == S2 and board[1][1] == "_":
            board[1][1] = S2
            moved = True
        #6=(6,8,7)
        elif board[2][0] == S2 and board[2][2] == S2 and board[2][1] == "_":
            board[2][1] = S2
            moved = True
        #7=(0,8,4)
        elif board[0][0] == S2 and board[2][2] == S2 and board[1][1] == "_":
            board[1][1] = S2
            moved = True
        #8=(2,6,4)
        elif board[0][2] == S2 and board[2][0] == S2 and board[1][1] == "_":
            board[1][1] = S2
            moved = True
        if not moved:
        # STOPING USER FROM WINNING (IF TWO BOXES ARE ALREADY FILLED BY USER COMPUTER FILL THIRD)
        # LOGIC#2 PART(A)
        # 1=(3, 6,0),2=( 4, 7,10),3=(5, 8,2),4=(1, 2,0),5=(4, 5,3),6=(7,8,6),7=(4, 8,0),8=(4, 6,2)
        # 1 =(0, 3, 6)
            if board[0][0] == S1 and board[1][0] == S1 and board[2][0] == "_":
                board[2][0] = S2
                moved = True
            #2=(1, 4, 7)
            elif board[0][1] == S1 and board[1][1] == S1 and board[2][1] == "_":
                board[2][1] = S2
                moved = True
            #3=(2, 5, 8)
            elif board[0][2] == S1 and board[1][2] == S1 and board[2][2] == "_":
                board[2][2] = S2
                moved = True
            #4=(0, 1, 2)
            elif board[0][0] == S1 and board[0][1] == S1 and board[0][2] == "_":
                board[0][2] = S2
                moved = True
            #5=(3, 4, 5)
            elif board[1][0] == S1 and board[1][1] == S1 and board[1][2] == "_":
                board[1][2] = S2
                moved = True
            #6=(6, 7, 8)
            elif board[2][0] == S1 and board[2][1] == S1 and board[2][2] == "_":
                board[2][2] = S2
                moved = True
            #7=(0, 4, 8)
            elif board[0][0] == S1 and board[1][1] == S1 and board[2][2] == "_":
                board[2][2] = S2
                moved = True
            #8=(2, 4, 6)
            elif board[0][2] == S1 and board[1][1] == S1 and board[2][0] == "_":
                board[2][0] = S2
                moved = True
            # LOGIC#2 PART(B)
            # 1=(3, 6,0),2=( 4, 7,10),3=(5, 8,2),4=(1, 2,0),5=(4, 5,3),6=(7, 8,6),7=(4, 8,0),8=(4, 6,2)
            elif board[1][0] == S1 and board[2][0] == S1 and board[0][0] == "_":
                board[0][0] = S2
                moved = True
            elif board[1][1] == S1 and board[2][1] == S1 and board[0][1] == "_":
                board[0][1] = S2
                moved = True
            elif board[1][2] == S1 and board[2][2] == S1 and board[0][2] == "_":
                board[0][2] = S2
                moved = True
            elif board[0][1] == S1 and board[0][2] == S1 and board[0][0] == "_":
                board[0][0] = S2
                moved = True
            elif board[1][1] == S1 and board[1][2] == S1 and board[1][0] == "_":
                board[1][0] = S2
                moved = True
            elif board[2][1] == S1 and board[2][2] == S1 and board[2][0] == "_":
                board[2][0] = S2
                moved = True
            elif board[1][1] == S1 and board[2][2] == S1 and board[0][0] == "_":
                board[0][0] = S2
                moved = True
            elif board[1][1] == S1 and board[2][0] == S1 and board[0][2] == "_":
                board[0][2] = S2
                moved = True
            # LOGIC#2 PART(C)
            # 1=(0,6,3) 2=(1,7,4) 3=(2,8,5) 4=(0,2,1) 5=(3,5,4) 6=(6,8,7) 7=(0,8,4) 8=(2,6,4)
            elif board[0][0] == S1 and board[2][0] == S1 and board[1][0] == "_":
                board[1][0] = S2
                moved = True
            elif board[0][1] == S1 and board[2][1] == S1 and board[1][1] == "_":
                board[1][1] = S2
                moved = True
            elif board[0][2] == S1 and board[2][2] == S1 and board[1][2] =="_":
                board[1][2] = S2
                moved = True
            elif board[0][0] == S1 and board[0][2] == S1 and board[0][1] == "_":
                board[0][1] = S2
                moved = True
            elif board[1][0] == S1 and board[1][2] == S1 and board[1][1] == "_":
                board[1][1] = S2
                moved = True
            elif board[2][0] == S1 and board[2][2] == S1 and board[2][1] == "_":
                board[2][1] = S2
                moved = True
            elif board[0][0] == S1 and board[2][2] == S1 and board[1][1] == "_":
                board[1][1] = S2
                moved = True
            elif board[0][1] == S1 and board[2][0] == S1 and board[1][1] == "_":
                board[1][1] = S2
                moved = True
    if not moved:
        # The 'and board[4] == "O"' part was added because of another exploit similar to the last one mentioned above
        if computerturn == 2 and board[1][1] == S1:
        # IF COMPUTER TURN IS SECONDE THEN IT SELECTS ANOTHER CORNER
            cornermove(board, moved)
            moved = True
    if moved == False:
        human = 0
        if board[0][1] == S1:
            human += 1
        if board[1][0] == S1:
            human += 1
        if board[1][2] == S1:
            human += 1
        if board[2][1] == S1: 
            human += 1

        if human >= 1:
            cornermove(board,moved)
            moved = True
        else:               
            sidemove(board,moved)
            moved = True

# PRINTING FINAL BOARD
def printboard(board):
    print("_______")
    print("|"+board[0][0] + "|" + board[0][1] + "|" + board[0][2] + "|")
    print("|"+board[1][0] + "|" + board[1][1] + "|" + board[1][2] + "|")
    print("|"+board[2][0] + "|" + board[2][1] + "|" + board[2][2] + "|")
# USER CAN WIN IN FOLLOWING METHODE
#[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]
# WINNING CONDITION OF COMPUTER
                                                 #FOURTH CONDITION OF PROJECT
#POINT#3
#While checking winning conditions in selection statements use and / or keywords to make your code compact
def ComputerWin(board):
    return (board[0][0] == S2 and board[1][0] == S2 and board[2][0] == S2) or (board[0][1] == S2 and board[1][1] == S2 and board[2][1] == S2) or\
        (board[0][2] == S2 and board[1][2] == S2 and board[2][2] == S2) or (board[0][0] == S2 and board[0][1] == S2 and board[0][2] == S2) or\
        (board[1][0] == S2 and board[1][1] == S2 and board[1][2] == S2) or (board[2][0] == S2 and board[2][1] == S2 and board[2][2] == S2)\
        or (board[0][0] == S2 and board[1][1] == S2 and board[2][2] == S2) or (board[0][2] == S2 and board[1][1] == S2 and board[2][0] == S2)

# WINNING CONDITION OF PLAYER


def PlayerWin(board):
    return (board[0][0] == S1 and board[1][0] == S1 and board[2][0] == S1) or (board[0][1] == S1 and board[1][1] == S1 and board[2][1] == S1) or\
        (board[0][2] == S1 and board[1][2] == S1 and board[2][2] == S1) or (board[0][0] == S1 and board[0][1] == S1 and board[0][2] == S1) or\
        (board[1][0] == S1 and board[1][1] == S1 and board[1][2] == S1) or (board[2][0] == S1 and board[2][1] == S1 and board[2][2] == S1)\
        or (board[0][0] == S1 and board[1][1] == S1 and board[2][2] == S1) or (board[0][2] == S1 and board[1][1] == S1 and board[2][0] == S1)

# DRAW CONDITION (IF PLAYER AND COMPUTER BOTH DON'T WIN)


def Draw(board):
    filledspaces = 0
    for i in range(8):
        if board[0][0] != "_" and board[0][1] != "_" and board[0][2] != "_" and board[1][0] != "_" and\
         board[1][1] != "_" and board[1][2] != "_"\
                and board[2][0] != "_" and board[2][1] != "_" and board[2][2] != "_":
            filledspaces += 1
    return filledspaces == 8
#POINT#4
#For step 5 above you should be using while loop with user feedback. Moreover
# ensure that the player only enters the valid box number to make his/her mov

# CONDITON TO REPLAY GAME                                   #FIFTH CONDTION OF PROJECT
replay_condition = True
while replay_condition == True:
    print("Welcome to tic tac toe game")                             #FIRST CONDITION OF PROJECT
    print("Board numbers will be as follows:")
    print("|1|2|3|")
    print("|4|5|6|")
    print("|7|8|9|")
    # BOARD WITH 2D LIST OF 3*3
    board = [            #POINT 1
        ["_", "_", "_"], #Instead of using nine variable use 2D list of 3x3 to represent the grid locations.
        ["_", "_", "_"],
        ["_", "_", "_"]
    ]
    # Asking  for player name
    while True:                                                         #SECONDE CONDITION OF PROJECT
        player = input("Enter your name:")
        if len(player) == 0:  # IF USER DON'T ENTER NAME
            print("You do have a name?Enter name please:")
            continue
        else:
            break
    # ASKING PLAYER FOR NAME
    while True:
        symbol = input("Choose your symbol as X or O:")
        symbol1 = symbol.upper()  # INCASE USER ENTER LOWERCASE
        if symbol1 != "O" and symbol1 != "X":
            print("Choose  symbol between 'O' OR 'X'")
            continue
        else:
            break
    if symbol1 == "O":
        print("your symbol is'O'")
        S1 = "O"  # S1 IS SYMBOL OF PLAYER
        S2 = "X"
    if symbol1 == "X":  # ASSIGNING SYMBOLS
        print("Your symbol is 'X'")
        S1 = "X"
        S2 = "O"
    # PERFOMING TOSS BETWEEN USER AND COMPUTER
    import random                                                           #THIRD CONDITION OF PROJECT
    toss = random.randint(1, 9)
    if toss % 2 == 0:
        print(player, " Won Toss")
        turn = "PLAYER"
    else:
        print("Computer Won Toss")
        turn = "Computer"
    computerturn = 0
    printboard(board)
    # KEEPING USER AND COMPUTER MAKING MOVE UNLESS ONE OF THEN WINS
    while ComputerWin(board) == False and PlayerWin(board) == False and Draw(board) == False:
        if turn == "PLAYER":
            Humanmove(board)
            printboard(board)
            turn = "Computer"
        elif turn == "Computer":
            computerturn += 1
            computermove(board, computerturn)
            print("Computer Turn")
            printboard(board)
            turn = "PLAYER"
    # PRINTING FINAL BOARD
    print("THE FINAL BOARD")
    printboard(board)
    # DECIDING WHO WON THE GAME
    if ComputerWin(board) == True:
        print("Computer Won")  # IF COMPUTER WINS
    elif PlayerWin(board) == True:
        print(player, end=" ")
        print("Won! Did you cheet.IMPOSSIBLE")  # IF USER WIN
    elif Draw(board) == True:
        print("Game draw!")  # IF BOTH DON'T WIN
    replay_condition = input(
        "If you want to replay game press Y or another key to exit:")
    # CONVERTING INPUT INTO UPPERCASE
    replay_condition = replay_condition.upper()
    if replay_condition == "Y":
        replay_condition = True
    else:
        replay_condition = False
# FINAL MESSAGE
print("Thanks for playing Tic Tac Toe with me:)")
