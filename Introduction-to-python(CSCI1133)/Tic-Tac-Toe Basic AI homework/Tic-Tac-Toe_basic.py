#CSCI 1133 Homework 3
#Elizabeth Olson
#Problem D

x = True
board = [[' ', ' ', ' ',], [' ', ' ', ' '], [' ', ' ', ' ']] #initialize the empty board

while x == True:
    play1 = int(input("Player 1, where would you like to move? ")) #ask the user where they want to move
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
    if play1 == 6 or play1 == 7 or play1 == 8:  #second list/row conditions
        if board[2][play1-6] is 'x' or board[2][play1-6] is 'o':
            print('Sorry, that space is already taken')
            continue
        else:
            board[2][play1-6] = 'x'

    for i in board:  #prints the board in the desired way, with each list on separate lines
        print(i)

    #if player 1 has a winning row
    if board[0].count('x') == 3 or board[1].count('x') == 3 or board[2].count('x') == 3:
        print("Player 1 wins!")
        x = False

    #if the player has a winning column
    for i in [0,1,2]:
        if board[0][i] == 'x' and board[1][i] == 'x' and board[2][i] == 'x':
            print("Player 1 wins!")
            x = False

    #if the player has a winning diagonal
    if board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
        print("Player 1 wins!")
        x = False
    if board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x':
        print("Player 1 wins!")
        x = False

    #calculations for the number of x's or o's in a row
    ax = board[0].count('x') + board[1].count('x') + board[2].count('x')
    ao = board[0].count('o') + board[1].count('o') + board[2].count('o')

    if ax == 5 and ao == 4:  #if the board is full and no win conditions are met
        print("It's a tie!")
        x = False

    #beginning of player 2's turn, everything is the same as above just with the x's and o's switched accordingly
    while x == True:
        play2 = int(input("Player 2, where would you like to move? "))
        if play2 == 0 or play2 == 1 or play2 == 2:
            if board[0][play2] is 'x' or board[0][play2] is 'o':
                print('Sorry, that space is already taken')
                continue
            else:
                board[0][play2] = 'o'
        if play2 == 3 or play2 == 4 or play2 == 5:
            if board[1][play2-3] is 'x' or board[1][play2-3] is 'o':
                print('Sorry, that space is already taken')
                continue
            else:
                board[1][play2-3] = 'o'
        if play2 == 6 or play2 == 7 or play2 == 8:
            if board[2][play2-6] is 'x' or board[2][play2-6] is 'o':
                print('Sorry, that space is already taken')
                continue
            else:
                board[2][play2-6] = 'o'

        for i in board:
            print(i)

        if board[0].count('o') == 3 or board[1].count('o') == 3 or board[2].count('o') == 3:
            print("Player 2 wins!")
            x = False

        for i in [0,1,2]:
            if board[0][i] == 'o' and board[1][i] == 'o' and board[2][i] == 'o':
                print("Player 2 wins!")
                x = False

        if board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
            print("Player 2 wins!")
            x = False
        if board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == 'o':
            print("Player 2 wins!")
            x = False
        break
