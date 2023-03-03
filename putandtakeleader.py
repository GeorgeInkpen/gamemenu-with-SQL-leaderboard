import random
from databaseheaders import *

def CheckUserInput(number):  # to check user input is a number

        try:
            #convert into an integer
            value=int(number)
            return(value,True)
        except ValueError:
            print('That is not a number, please try again: ')
            return(-1,False)


def CheckNameDuplicates(name,counterlist):
    
    if name in counterlist.keys():
        
        print('The name '+ name + ' is taken, please try agan: ')
    
    elif name =='pot':
        print('That will be confusing, try again: ')

    else:

        return(True)

    return(False)


def PrintCounters(counterlist):

    print('Remaining players and counters\n')
    for person in counterlist:
        if counterlist[person]>0 or person=='Pot':
            print(person, '\t:',counterlist[person],'\n' )  
    input('Press return to continue: ')


def OutputResult(counterlist,dice,person):
   
    if dice !=0:
        print ('You rolled a ',dice,'\n')
    if dice==1:
        print('You get a counter from the pot')
        counterlist[person]+=1
        counterlist['Pot']-=1
    elif dice==2 or dice==0:
        print('You all put a counter in the pot')
        
        for item in counterlist:
            if item=='Pot' or counterlist[item]<=0:
                pass
            else:
                counterlist[item]-=1
                counterlist['Pot']+=1        
    elif dice==3:
        print('You take all the counters from the pot')
        counterlist[person]+=counterlist['Pot']
        counterlist['Pot']=0
    elif dice==4:
        print('You put two counters in the pot')
        if counterlist[person]==1:
            counterlist[person]-=1
            counterlist['Pot']+=1
        else:
            counterlist[person]-=2
            counterlist['Pot']+=2
    elif dice==5:
        print('You take two counters from the pot')
        if counterlist['Pot']==1:
            counterlist[person]+=1
            counterlist['Pot']-=1
        else:
            counterlist[person]+=2
            counterlist['Pot']-=2
    elif dice==6:
        print('You put a counter in the pot')
        counterlist[person]-=1
        counterlist['Pot']+=1
    else:
        pass

             
    return (counterlist)

    
 
def PutandTake():

    loop=False
    while loop==False:
        playernum=input('How many players: ')
        players,loop=CheckUserInput(playernum)

    loop=False
    while loop==False:
        counternum=input('How many starting counters: ')
        counters,loop=CheckUserInput(counternum)

    counterlist={'Pot':0}
    loop=1
    x=''
    while loop<=players:
        loop2=False
        while loop2==False:
            name = input(f"Please enter player number {loop}'s name: ") 
            loop2=CheckNameDuplicates(name,counterlist)   
            if loop2==True:
                print(name)
                counterlist[name]=counters
                sql1="SELECT name1 FROM players WHERE name1 = %s LIMIT 1"
                val1=name,
                mycursor.execute(sql1,val1)

                if mycursor.fetchone():
                    print('Welcome Back',name)  
                else:
                    print('Welcome Newbie',name)
                    sql = "INSERT INTO players (name1, wins,draws,loses) VALUES (%s, %s,%s,%s)"
                    val = (name,0,0,0)
                    mycursor.execute(sql,val)
                    mydb.commit()

        loop+=1    
    
    
    PrintCounters(counterlist)

    counterlist=OutputResult(counterlist,0,'Pot')
    PrintCounters(counterlist)

    playersleft=players
  
    while playersleft>2:
        
        for person in counterlist:
            
            if person=='Pot' or counterlist[person]<=0:
                pass
            else:
                input(person+ ' please roll the die: ' )   
                dice = [1,2,3,4,5,6] 
                diceresult=random.choice(dice)
                counterlist=OutputResult(counterlist,diceresult,person)
                PrintCounters(counterlist)
           
            if counterlist['Pot']==0:
                counterlist=OutputResult(counterlist,0,'Pot')
                PrintCounters(counterlist)
            playersleft=0
            for playercheck in counterlist:
                if counterlist[playercheck]>0:
                    playersleft+=1
            if playersleft==2:
                break
    for player in counterlist:
        if counterlist[player]>0 and player!='Pot':
            print(f'Well done '+ player + ' you have won')
             
            sql="UPDATE players SET wins=wins+1 WHERE name1= %s"
            val=player,
            mycursor.execute(sql,val)
            mydb.commit()
        elif player=='Pot':
            pass           
        else:
            sql="UPDATE players SET loses=loses+1 WHERE name1= %s"
            val=player,
            mycursor.execute(sql,val)
            mydb.commit()


            #mycursor.execute('UPDATE players SET wins = wins+1 WHERE ')


            
        
            



