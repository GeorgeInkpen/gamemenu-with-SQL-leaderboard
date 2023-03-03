
from putandtakeleader import *
from databaseheaders import *

gamenum=0

while gamenum !=3:
    loop=False
    while loop==False:
        print('\nGame options.\n')
        print('1. Put and Take, by G. Inkpen.')    #menu for different games
        print('2. Tic Tak Toe, coming soon.')
        print('3. Exit.')
        select=input('\nPlease select the game to play\n')
        gamenum,loop=CheckUserInput(select)

    if gamenum==1:
        PutandTake()  #play the first game

      
    elif gamenum==2:
        print('coming soon')
        input('Press any key to return to the menu. ')

    elif gamenum==3:
        print('Goodbye')   
    else:
        print('Try again. ')
