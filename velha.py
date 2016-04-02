import random

def drawBoard(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' | ')
    print('---------------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' | ')
    print('---------------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ')
    


def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print("Do you Want to be X or O? ")
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'Computer'
    else:
        return 'Player'

def playAgain():
    print("Play Again Y or N? ")
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))


def getBoardCopy(board):
    dupeboard = []
    for i in board:
        dupeboard.append(i)
    return dupeboard


def isBoardFree(board, move):
    return board[move] == ' '

def playerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isBoardFree(board, int(move)):
        print('Whats your next move (1-9)? ')
        move = input()
    return int(move)


def chooseRandomMove(board, moveList):
    possibleMoves = []
    for i in moveList:
        if isBoardFree(board, i):
            possibleMoves.append(i)
        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

def getCompMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isBoardFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isBoardFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    move = chooseRandomMove(board, [1,3,7,9])
    if move != None:
        return move
    if isBoardFree(board, 5):
        return 5
    return chooseRandomMove(board, [2,4,6,8])


def isBoardFull(board):
    for i in range(1,10):
        if isBoardFree(board,i):
            return False
    return True

print("WelCome to Tic Tac Toe")

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = playerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('You Won')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is tied")
                    break
                else:
                    turn = 'computer'
        else:
            move = getCompMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('You Lose')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is tied')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break