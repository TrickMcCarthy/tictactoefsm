#Tac Toe

import random
from sense_hat import SenseHat
from time import sleep
#Player pick grid position from a 9-box layout and these are matched to sensorhat grid
GridPos = {
          1:48, #botleft
          2:51, #botmid
          3:54, #botright
          4:24, #midleft
          5:27, #midmid
          6:30, #midright
          7:0,  #topleft
          8:3,  #topmid
          9:6   #topright
          }

blue = (0, 0, 255)
red = (255, 0, 0)

w = (150, 150, 150)
e = (0, 0, 0)

grid = [
e,e,w,e,e,w,e,e,
e,e,w,e,e,w,e,e,
w,w,w,w,w,w,w,w,
e,e,w,e,e,w,e,e,
e,e,w,e,e,w,e,e,
w,w,w,w,w,w,w,w,
e,e,w,e,e,w,e,e,
e,e,w,e,e,w,e,e
]

global sense
global sensehat_available
no_players = 0

try:
  sense = SenseHat()
  sensehat_available = True
except Exception as e:
  print(e)
  print("Text mode only")
  sensehat_available = False


def updateGrid(pos,color):
    global grid
    if isinstance(pos, int):
       grid[GridPos[pos]]   = color
       grid[GridPos[pos]+1] = color
       grid[GridPos[pos]+8] = color
       grid[GridPos[pos]+9] = color
    
def drawBoard(board):
# This function prints out the board that it was passed.
# "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    if sensehat_available:
       try:
         global grid
         sense.set_pixels(grid)
       except Exception as e:
         print(e)
        

def inputPlayerLetter(letterChoice = ''):
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    global no_players
    while not (no_players == 1 or no_players == 2):
       print('1 or 2 Players?')
       no_players = int(input())
   
    letter = letterChoice.upper()
    while not (letter == 'X' or letter == 'O'):
       print('Do you want to be X or O?')
       letter = input().upper()
       if sensehat_available:
          sense.clear((0, 0, 0))
       drawBoard(theBoard)
    # the first element in the tuple is the player's letter, the second is the computer's letter.
    if letter == 'X':
       return ['X', 'O']
    else:
       return ['O', 'X']

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
       return 'Player2Turn'
    else:
       return 'Player1Turn'

def anotherGame():
    global device, grid, theBoard, playerLetter, computerLetter
    w = (150, 150, 150)
    e = (0, 0, 0)
    if sensehat_available:
       sense.clear((0, 0, 0))
    if playAgain():
       # Reset the board
       theBoard = [' '] * 10
       grid = [e,e,w,e,e,w,e,e,e,e,w,e,e,w,e,e,w,w,w,w,w,w,w,w,e,e,w,e,e,w,e,e,e,e,w,e,e,w,e,e,w,w,w,w,w,w,w,w,e,e,w,e,e,w,e,e,e,e,w,e,e,w,e,e]
       if sensehat_available:
          try:
              sense.set_pixels(grid)
          except Exception as e:
              print("Exception {}",e)
           
       playerLetter, computerLetter = inputPlayerLetter()
       turn = whoGoesFirst()
       print('The ' + turn + ' will go first.')
       device.on_event(turn)

def playAgain(choice = ''):
    # This function returns True if the player wants to play again, otherwise it returns False.
    # input paramter given for testing
    if choice == '':
       print('Do you want to play again? (yes or no)')
       return input().lower().startswith('y')
    else:
       return choice.lower().startswith('y')
       

def makeMove(board, letter, move, who):
    global blue, red
    board[move] = letter
    color = blue
    if who == "computer":
       color = red

    updateGrid(move,color)
    if sensehat_available:
       try:
          global grid 
          sense.set_pixels(grid)
       except Exception as e:
          print("Exception {}",e)


def checkMove(board, letter, move, who):
    global blue, red
    board[move] = letter
    color = blue
    

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
          print('What is your next move? (1-9)')
          move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the list
    # Returns None if there no no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i ):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
       playerLetter = 'O'
    else:
       playerLetter = 'X'
    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
           checkMove(copy, computerLetter, i, "computer")
           if isWinner(copy, computerLetter):
              return i
    
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
       return move
    #Try to take the center if its is free
    if isSpaceFree(board, 5):
        return 5
    #Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
           return False
    return True


def setupGame(arg_device):
    global device
    global theBoard 
    global playerLetter, computerLetter
    device = arg_device
    if sensehat_available:
       try:
          sense.clear((0, 0, 0))
       except Exception as e:
          print("Exception {}",e)

    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    device.on_event(turn)


def playerActions():
    # Player's turn.
    opponent = "Computer"
    global no_players
    if no_players == 2:
       opponent = "Player2"
    move = getPlayerMove(theBoard)
    makeMove(theBoard, playerLetter, move, "player")
    drawBoard(theBoard)

    if isWinner(theBoard, playerLetter):
       drawBoard(theBoard)
       print('Hooray! Player1 has won the game!')
       device.on_event('PlayerWin')
    else:
       if isBoardFull(theBoard):
          drawBoard(theBoard)
          print('The game is a tie!')
          device.on_event('Tie')
       else:
          print('The next turn is {}!'.format(opponent))
          device.on_event('Player2Turn')


def computerActions():
    opponent = "Computer"
    global no_players
    if no_players == 2:
       move = getPlayerMove(theBoard)
       opponent = "Player2"
    else: #computers turn
       move = getComputerMove(theBoard, computerLetter)

    makeMove(theBoard, computerLetter, move, "computer")
    drawBoard(theBoard)

    if isWinner(theBoard, computerLetter):
       drawBoard(theBoard)
       print('The {} has beaten you! You lose.'.format(opponent))
       device.on_event('ComputerWin')
    else:
       if isBoardFull(theBoard):
          drawBoard(theBoard)
          print('The game is a tie!')
          device.on_event('Tie')
       else:
          print('The next turn is Player1!')
          device.on_event('Player1Turn')

