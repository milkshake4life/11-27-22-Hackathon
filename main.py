import random



global turn
global availableSpots
global board


turn = 1
availableSpots = [1, 2, 3, 4, 5, 6, 7, 8, 9]




def printBoard(gameBoard):
    for i in gameBoard:
          print(i)




def compMove():
    global availableSpots
    global board
    if len(availableSpots) == 9:
        board[0][0] = "O"
        availableSpots.remove(1)
    else:



        bestScore = -1000
        bestMove = 1000 #needs to be something random

        for i in availableSpots:
            board[int((int(i) - 1 )/3)][int((int(i)-1)%3)] = "O"
            availableSpots.remove(i)
            score = minimax(board, 0, False)
            availableSpots.append(i)
            availableSpots.sort()
            board[int((int(i) - 1 )/3)][int((int(i)-1)%3)] = "0"
            if score > bestScore:
                bestScore = score
                bestMove = i
        
        board[int((int(bestMove) - 1 )/3)][int((int(bestMove)-1)%3)] = "O"
        availableSpots.remove(bestMove)

def minimax(board, depth, isMaximizing):
    global availableSpots



    if checkWin("O"):
        return 1

    elif checkWin("X"):
        return -1

    elif checkDraw():
        return 0
    

    if isMaximizing:
        bestScore = -1000

        for i in availableSpots:
            board[int((int(i) - 1 )/3)][int((int(i)-1)%3)] = "O"
            availableSpots.remove(i)
            score = minimax(board, 0, False)
            availableSpots.append(i)
            availableSpots.sort()
            board[int((int(i) - 1 )/3)][int((int(i)-1)%3)] = "0"
            if score > bestScore:
                bestScore = score
        
        return bestScore

    else:
        bestScore = 1000

        for i in availableSpots:
            board[int((int(i) - 1 )/3)][int((int(i)-1)%3)] = "X"
            availableSpots.remove(i)
            score = minimax(board, depth + 1, True)
            availableSpots.append(i)
            availableSpots.sort()
            board[int((int(i) - 1 )/3)][int((int(i)-1)%3)] = "0"
            if score < bestScore:
                bestScore = score
        
        return bestScore
            




def placePiece(board):
    global turn
    global availableSpots
    check = True
    if turn == 0:
        while(check):
            position = input("Player 1: ")
            if (int(position)) in availableSpots:
                availableSpots.remove(int(position))
                check = False
            else:
                print("Already taken, Please try again")
        board[int((int(position) - 1 )/3)][int((int(position)-1)%3)] = "X"
        turn = 1
    else:
        compMove()
        turn = 0

        #   while(check):
        #       position = input("Bot: ")
        #       if (int(position)) in availableSpots:
        #           availableSpots.remove(int(position))
        #           check = False
        #       else:
        #           print("Already taken, Please try again")
        #   board[int((int(position) - 1 )/3)][int((int(position)-1)%3)] = "O"
        #   turn = 0


def checkHorzontal(mark):
    global board
    list = [0, 1, 2]
    for i in list:
        if (board[i][0] == mark) and (board[i][1] == mark) and (board[i][2] == mark):
            return True
    return False

def checkVertical(mark):
    global board
    list = [0, 1, 2]
    for i in list:
        if (board[0][i] == mark) and (board[1][i] == mark) and (board[2][i] == mark):
            return True
    return False

def checkRightDiagonal(mark):
    global board
    if (board[0][0] == mark) and (board[1][1] == mark) and (board[2][2] == mark):
        return True
    return False

def checkLeftDiagonal(mark):
    global board
    if (board[0][2] == mark) and (board[1][1] == mark) and (board[2][0] == mark):
        return True
    return False

def checkWin(mark):
    mark = str(mark)
    # if checkHorzontal(mark) or checkVertical(mark) or checkRightDiagonal(mark) or checkLeftDiagonal(mark):
    #     if mark == "X":
    #         print("Player Wins!!!")
    #         return True
    #     elif mark == "O":
    #         print("AI Wins!!!")
    #         return True
    # return False

    if(board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] == mark):
        return True
    elif(board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] == mark):
        return True
    elif(board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] == mark):
        return True
    elif(board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] == mark):
        return True
    elif(board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] == mark):
        return True
    elif(board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] == mark):
        return True
    elif(board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == mark):
        return True
    elif(board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] == mark):
        return True
    else:
        return False

def checkDraw():
    if len(availableSpots) == 0:
        return True
    return False




def game():
    global board
    printBoard(board)
    print("Bot Goes First")
    while (checkWin("X") == False and checkWin("O") == False and checkDraw() == False):
        placePiece(board)
        printBoard(board)
        print()
    if checkDraw() == True:
        print("It's a draw")
        





board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
game()


