from __future__ import print_function

choices = []

for x in range (0, 9) :
    choices.append(str(x + 1))

playerOneTurn = True
winner = False

def printBoard() :
    print( '\n -----')
    print( '|' + choices[1] + '|' + choices[2] + '|' + choices[3] + '|')
    print( ' -----')
    print( '|' + choices[4] + '|' + choices[5] + '|' + choices[6] + '|')
    print( ' -----')
    print( '|' + choices[7] + '|' + choices[8] + '|' + choices[9] + '|')
    print( ' -----\n')

while not winner :
    printBoard()

    if playerOneTurn :
        print( "Player 1:")
    else :
        print( "Player 2:")

    try:
        choice = int(input(">> "))
    except:
        print("please enter a valid field")
        continue
    if choices[choice - 1] == 'X' or choices [choice-1] == 'O':
        print("illegal move, plase try again")
        continue

    if playerOneTurn :
        choices[choice - 1] = 'X'
    else :
        choices[choice - 1] = 'O'

    playerOneTurn = not playerOneTurn

    for x in range (0, 3) :
        y = x * 3
        if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) :
            winner = True
            printBoard()
        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) :
            winner = True
            printBoard()

    if((choices[0] == choices[4] and choices[0] == choices[8]) or 
       (choices[2] == choices[4] and choices[4] == choices[6])) :
        winner = True
        printBoard()

print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")