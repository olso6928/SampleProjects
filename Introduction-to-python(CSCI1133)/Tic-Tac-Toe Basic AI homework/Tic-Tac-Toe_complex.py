#CSCI 1133 Homework 3
#Elizabeth Olson
#Bonus Problem

import random
x = True
y = True

while y == True:  #allows for the user to decide if they want to play again later in the code
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]  #initialize the empty board
    while x == True:

        #initialize the counts for the column totals
        totalx0 = 0
        totalx1 = 0
        totalx2 = 0
        totalo0 = 0
        totalo1 = 0
        totalo2 = 0

        play1 = int(input("Player 1, where would you like to move? "))  #ask the user where they want to move
        if play1 == 0 or play1 == 1 or play1 == 2:  #first list/row conditions
            if board[0][play1] is 'x' or board[0][play1] is 'o':
                print('Sorry, that space is already taken')
                continue
            else:
                board[0][play1] = 'x'
        if play1 == 3 or play1 == 4 or play1 == 5:  #second list/row conditions
            if board[1][play1-3] is 'x' or board[1][play1-3] is 'o':
                print('Sorry, that space is already taken')
                continue
            else:
                board[1][play1-3] = 'x'
        if play1 == 6 or play1 == 7 or play1 == 8:  #third list/row conditions
            if board[2][play1-6] is 'x' or board[2][play1-6] is 'o':
                print('Sorry, that space is already taken')
                continue
            else:
                board[2][play1-6] = 'x'

        for i in board:  #prints the board in the desired way, with each list on separate lines
            print(i)

        #calculations for the number of x's or o's in a row
        ax = board[0].count('x') + board[1].count('x') + board[2].count('x')
        ao = board[0].count('o') + board[1].count('o') + board[2].count('o')

        if ax == 5 and ao == 4:  #if the board is full and no win conditions are met
            print("It's a tie!")
            x = False

        #if the player has a winning row
        if board[0].count('x') == 3 or board[1].count('x') == 3 or board[2].count('x') == 3:
            print("You win!")
            x = False

        #if the player has a winning column
        for i in [0,1,2]:
            if board[0][i] == 'x' and board[1][i] == 'x' and board[2][i] == 'x':
                print("You win!")
                x = False

        #if the player has a winning diagonal
        if board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
            print("You win!")
            x = False
        if board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x':
            print("You win!")
            x = False

        #beginning of the code for the computer's turn
        #counts the number of x's and o's in a column to be used later
        for i in range(3):
            totalx0 += board[i][0].count('x')
            totalx1 += board[i][1].count('x')
            totalx2 += board[i][2].count('x')
            totalo0 += board[i][0].count('o')
            totalo1 += board[i][1].count('o')
            totalo2 += board[i][2].count('o')

        #will only print this if the player has not won already
        if x == True:
            print("My turn!")
        while x == True:

            #if computer has 2 in any row, place o in left over spot to win accounting for not having any x's
            if board[0].count('o') == 2 and board[0].count('x') == 0:
                for i in range(3):
                    if board[0][i] != 'x':
                        board[0][i] = 'o'
                print("I win!")
                x = False
            elif board[1].count('o') == 2 and board[1].count('x') == 0:
                for i in range(3):
                    if board[1][i] != 'x':
                        board[1][i] = 'o'
                print("I win!")
                x = False
            elif board[2].count('o') == 2 and board[2].count('x') == 0:
                for i in range(3):
                    if board[2][i] != 'x':
                        board[2][i] = 'o'
                print("I win!")
                x = False

            #if computer has 2 in any column, place o in left over spot to win accounting for not having any x's
            elif totalo0 == 2 and totalx0 == 0:
                for i in range(3):
                    if board[i][0] != 'o':
                        if board[i][0] != 'x':
                            board[i][0] = 'o'
                            print("I win!")
                            x = False
                continue
            elif totalo1 == 2 and totalx1 == 0:
                for i in range(3):
                    if board[i][1] != 'o':
                        if board[i][1] != 'x':
                            board[i][1] = 'o'
                            print("I win!")
                            x = False
                continue
            elif totalo2 == 2 and totalx2 == 0:
                for i in range(3):
                    if board[i][2] != 'o':
                        if board[i][2] !='x':
                            board[i][2] = 'o'
                            print("I win!")
                            x = False
                continue

            #if computer has 2 in a diagonal position, place an o in the last diagonal position to win accounting for not having any x's
            elif board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] != 'x':
                board[2][2] = 'o'
                print("I win!")
                x = False
            elif board[0][0] == 'o' and board[2][2] == 'o' and board[1][1] != 'x':
                board[1][1] = 'o'
                print("I win!")
                x = False
            elif board[1][1] == 'o' and board[2][2] == 'o' and board[0][0] != 'x':
                board[0][0] = 'o'
                print("I win!")
                x = False
            elif board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] != 'x':
                board[2][0] = 'o'
                print("I win!")
                x = False
            elif board[0][2] == 'o' and board[2][0] == 'o' and board[1][1] != 'x':
                board[1][1] = 'o'
                print("I win!")
                x = False
            elif board[1][1] == 'o' and board[2][0] == 'o' and board[0][2] != 'x':
                board[0][2] = 'o'
                print("I win!")
                x = False

            #if player 1 has 2 in any row, place o in left over spot to block
            elif board[0].count('x') == 2 and board[0].count('o') == 0:
                for i in range(3):
                    if board[0][i] != 'x':
                        board[0][i] = 'o'
                break
            elif board[1].count('x') == 2 and board[1].count('o') == 0:
                for i in range(3):
                    if board[1][i] != 'x':
                        board[1][i] = 'o'
                break
            elif board[2].count('x') == 2 and board[2].count('o') == 0:
                for i in range(3):
                    if board[2][i] != 'x':
                        board[2][i] = 'o'
                break

            #if player 1 has 2 in any column, place o in left over spot to block
            elif totalx0 == 2 and totalo0 == 0:
                for i in range(3):
                    if board[i][0] != 'x':
                        if board[i][0] != 'o':
                            board[i][0] = 'o'
                break
            elif totalx1 == 2 and totalo1 == 0:
                for i in range(3):
                    if board[i][1] != 'x':
                        if board[i][1] != 'o':
                            board[i][1] = 'o'
                break
            elif totalx2 == 2 and totalo2 == 0:
                for i in range(3):
                    if board[i][2] != 'x':
                        if board[i][2] !='o':
                            board[i][2] = 'o'
                break

            #if player 1 has 2 in a diagonal position, place an o in the last diagonal position to block
            elif board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] !='o':
                board[2][2] = 'o'
                break
            elif board[0][0] == 'x' and board[2][2] == 'x' and board[1][1] !='o':
                board[1][1] = 'o'
                break
            elif board[1][1] == 'x' and board[2][2] == 'x' and board[0][0] !='o':
                board[0][0] = 'o'
                break
            elif board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] !='o':
                board[2][0] = 'o'
                break
            elif board[0][2] == 'x' and board[2][0] == 'x' and board[1][1] !='o':
                board[1][1] = 'o'
                break
            elif board[1][1] == 'x' and board[2][0] == 'x' and board[0][2] !='o':
                board[0][2] = 'o'
                break

            #if none of the winning or blocking conditions are met, get a random number for the computer to move to
            else:
                play2 = random.randint(0,8)
                if play2 == 0 or play2 == 1 or play2 == 2:
                    if board[0][play2] is 'x' or board[0][play2] is 'o':
                        continue
                    else:
                        board[0][play2] = 'o'
                if play2 == 3 or play2 == 4 or play2 == 5:
                    if board[1][play2-3] is 'x' or board[1][play2-3] is 'o':
                        continue
                    else:
                        board[1][play2-3] = 'o'
                if play2 == 6 or play2 == 7 or play2 == 8:
                    if board[2][play2-6] is 'x' or board[2][play2-6] is 'o':
                        continue
                    else:
                        board[2][play2-6] = 'o'
                break

        for i in board:
            print(i)

    #allows for the quick replaying and testing
    again = str(input("Would you like to play again? (y/n) "))
    if again == 'y':
        x = True
    elif again == 'n':
        y = False
