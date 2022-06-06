import random
currentPlayer = 'X'
winner = None
gameRunning = True
board = [
    "_", "_", "_",
    "_", "_", "_",
    "_", "_", "_"
]


# Print the Board
def printboard(board):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('----------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('----------')
    print(f'{board[6]} | {board[7]} | {board[8]}')


# Get User Input
def userInput(board):
    userOpt = int(input("Enter a number 1-9: "))
    if userOpt >= 1 and userOpt <= 9 and board[userOpt-1] == '_':
        board[userOpt-1] = currentPlayer
    else:
        print('Play is invalid! Try again')


def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '_':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '_':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '_':
        winner = board[6]
        return True


def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '_':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '_':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '_':
        winner = board[2]
        return True


def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '_':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '_':
        winner = board[2]
        return True


def checkTie(board):
    global gameRunning
    if '_' not in board:
        printboard(board)
        print("Game is a Tie")
        gameRunning = False



def checkWinner():
    global gameRunning
    if checkHorizontal(board) or checkDiagonal(board) or checkVertical(board):
        print(f"{winner} wins!")
        printboard(board)
        gameRunning = False


def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'

def computer(board):
    while currentPlayer == "O":
        comp_guess = random.randint(0,8)
        if board[comp_guess] == "_":
            board[comp_guess] = "O"
            switchPlayer()
        else:
            continue

while gameRunning:
    printboard(board)
    userInput(board)
    checkWinner()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWinner()
    checkTie(board)

