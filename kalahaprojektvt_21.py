import random #import random for the copmuter to be able to play kalaha, and to select wich player starts randomly
import time #time between each turn.


def move_stones_player_one(amountStones,chosen_pot,board):
    """ A function that moves the stones for player 1 between the pots and its store."""
    while amountStones > 0: #sista man ska göra är att minska antal kulor med 1.
        if chosen_pot <= 5 and chosen_pot > 0:
            board[chosen_pot -1] += 1
            chosen_pot = chosen_pot - 1
        elif chosen_pot == 0: #om vi har  noll ska man automatiskt lägga till i bo.
            board[6] += 1
            chosen_pot = 6
        elif chosen_pot == 6:
            board[12] += 1
            chosen_pot = 12

        elif chosen_pot <= 12 and chosen_pot >7:
            board[chosen_pot - 1] += 1
            chosen_pot = chosen_pot -1

        elif chosen_pot == 7:
            board[5] += 1
            chosen_pot = 5
        amountStones -= 1 #"Kulorna i min hand som minskas. minska kulorna med 1
    return chosen_pot



def move_stones_player_two(amountStones,chosen_pot,board):
    """"A function that moves the stones for player two between the pots and store.."""
    while amountStones > 0:

        if chosen_pot <= 12 and chosen_pot > 7:
            board[chosen_pot -1 ] += 1
            chosen_pot = chosen_pot - 1

        elif chosen_pot == 7:
            board[13] += 1
            chosen_pot = 13

        elif chosen_pot <= 5 and chosen_pot > 0:
            board[chosen_pot -1] += 1
            chosen_pot = chosen_pot -1

        elif chosen_pot == 0:
            board[12] += 1
            chosen_pot = 12

        elif chosen_pot == 13:
            board[5] += 1
            chosen_pot = 5
        amountStones -= 1
    return chosen_pot

def pot_that_player_chooses(playerOnesTurn,userInput ):
    """ function for the players to be able to choose pots."""
    chosen_pot = -1

    if playerOnesTurn and userInput == "5":
        chosen_pot = 5
    elif playerOnesTurn and userInput == "4":
        chosen_pot = 4
    elif playerOnesTurn and userInput == "3":
        chosen_pot = 3
    elif playerOnesTurn and userInput == "2":
        chosen_pot = 2
    elif playerOnesTurn and userInput == "1":
        chosen_pot = 1
    elif playerOnesTurn and userInput == "0":
        chosen_pot = 0

    elif not (playerOnesTurn) and userInput == "12":
        chosen_pot = 12
    elif not (playerOnesTurn) and userInput == "11":
        chosen_pot = 11
    elif not (playerOnesTurn) and userInput == "10":
        chosen_pot = 10
    elif not (playerOnesTurn) and userInput == "9":
        chosen_pot = 9
    elif not (playerOnesTurn) and userInput == "8":
        chosen_pot = 8

    elif not (playerOnesTurn) and userInput == "7":
        chosen_pot = 7

    return chosen_pot


def playing_kalaha_game(playerOnesTurn, board, playerOneHuman, playerTwoHuman):#
    """function that implements the rule for kalaha."""
    playThegame = True
    if playerOnesTurn: #vi kollar om spelare 1 startar så är spelaren som inte startar lika med 2, ifall det blir oavgjort så är spelaren som inte startar vinnaren.
        playerNotStarting = 2
    else:
        playerNotStarting = 1
    while (playThegame):  # spelar spelet
        if playerOnesTurn:
            print("Player 1:s turn, please choose a pot (1-5), where 0 is closest to you store!")
            print(" 0  1  2  3  4  5")

        print([board[0], board[1], board[2], board[3], board[4], board[5]])
        print([board[6], "--------", board[13]])
        print([board[12], board[11], board[10], board[9], board[8], board[7]])
        print("")
        chosen_pot = 0
        if not playerOnesTurn:
            print(" 12  11  10  9  8  7")
            print("Player 2:s turn, Please choose a pot(7-12) where 7 is closest to your store!")
            print("")
        if playerOneHuman  and playerOnesTurn   :
            userInput = input("type q to quit the game :")
            if userInput == "q":
                playThegame = False
            elif userInput not in ["0","1","2","3","4","5"]:
                print("choose a number 1-5, make sure there is no spacing in between!")# har vi mellanslag så godkänns det inte.
                continue
            else:

                chosen_pot = pot_that_player_chooses(playerOnesTurn,userInput) #sparar det valda skålet
                if board[chosen_pot] == 0:
                    print("you chose an empty pot, please choose again!")
                    continue
        elif playerTwoHuman  and not playerOnesTurn   :
            userInput = input("type q to quit the game:")
            if userInput == "q":
                playThegame = False
            elif userInput not in ["7","8","9","10","11","12"]:
                print("choose a number 7-12, make sure there is no spacing in between!!")
                continue
            else:
                chosen_pot = pot_that_player_chooses(playerOnesTurn,userInput) #sparar det valda skålet
                if board[chosen_pot] == 0:
                    print("you chose an empty pot, please choose again!")
                    continue # bryter while loopen men går inte ut den så att den avslutas.
        elif not playerOneHuman and playerOnesTurn: #Om spelare ett inte är människa och det är playerOnesTurn tur välj spelare 1 skål slumpmässigt
            selectable_pots = []
            for pot_number in range(6):# väljer skålar som har kulor i sig och lägger i en lista för spelare 1.
                if board[pot_number] != 0: # väljer en skål som inte är tom och lägger i en ny lista som sparar icke tomma skålar
                    selectable_pots.append(pot_number)
            chosen_pot = random.choice(selectable_pots) #väljer en skål som inte är tom och sparar
            print("The computer chose pot number", chosen_pot,"\n")
        elif not playerTwoHuman and not playerOnesTurn :# spelare två ej människa välj spelare två skål slumpmässigt.
            selectable_pots = []
            for pot_number in range(7,13):# väljer skålar som har kulor i sig och lägger i en lista för spelare 2
                if board[pot_number] != 0: # väljer en skål som inte är tom och lägger i en ny lista som sparar icke tomma skålar
                    selectable_pots.append(pot_number)
            chosen_pot = random.choice(selectable_pots) #väljer en skål som inte är tom och sparar
            print("the computer chose pot number", chosen_pot,"\n")
        amountStones = board[chosen_pot]
        last_pot = 0
        board[chosen_pot] = 0
        if playerOnesTurn:
            last_pot = move_stones_player_one(amountStones, chosen_pot,
                                              board)  # funktionsanrop, flytta kulor för spelare ett, skicka med vilket index startar vi på, hur många kulor fanns det i
        elif not playerOnesTurn:
            last_pot = move_stones_player_two(amountStones, chosen_pot, board)
        if last_pot != 6 and last_pot != 13:  # Om spelare inte lägger kulorna på rätt bo så byt spelare
            playerOnesTurn = not (playerOnesTurn)
        if board[0] == 0 and board[1] == 0 and board[2] == 0 and board[3] == 0 and board[4] == 0 and board[5] == 0:
            for i in range(7,13): #om spelare 1 har tomma skålar så flyttar spelare 2 sina kulor till sitt bo.
                board[13] += board[i]
                board[i] = 0
            playThegame = False
        elif board[7] == 0 and board[8] == 0 and board[9] == 0 and board[10] == 0 and board[11] == 0 and board[12] == 0:
            for i in range(0,6):  # om spelare 2 har tomma skålar så flyttar spelare 1 sina kulor till sitt bo.
                board[6] += board[i]
                board[i] = 0
            playThegame = False
        if playThegame == False:
            print([board[0], board[1], board[2], board[3], board[4], board[5]]) #printar brädan så man kan se hur många kulor varje spelare hade i sitt bo.
            print([board[6], "--------", board[13]])
            print([board[12], board[11], board[10], board[9], board[8], board[7]])
            print("")
            if board[13] == board[6]:
                print("Player 1 and player 2 have the same amount of stones in their stores, player",playerNotStarting, "won!")# printar ut vilken när det blir oavgjort
            elif board[13] > board[6] :
                print("Player 2 hade had more stones in their store, player 2 won!")#printar ut att spelare 2 vann
            elif board[6] > board[13]:
                print("Player 1 hade had more stones in their store, player 1 won!")#printar ut att spelare 1 vann
        time.sleep(1)# ändrar tiden mellan spelen. Den är satt till 1 sekund.





print("Welcome to Kalaha!") # här har vi att spelare kan välja kulor samt att programmet inte kraschar om vi matar in fel.
stones = 0
while stones < 3 or  stones > 6:
    try: # felhantering så programmet inte kraschar om vi matar in fel data.

        stones = int(input("How many stones in each pot?, you can choose 3 to 6 ! "))
        if stones < 3 or stones > 6:
            print("You didn't type a number between 3 and 6, please do so!.")

    except ValueError :
        print("You must type a number between 3 and 6 !")
    except:
         print("Type a number between 3 and 6, thank you!")

board = [stones,stones,stones,stones,stones,stones,0,stones,stones,stones,stones,stones,stones,0]#brädan som är en lista.
player1  = input("Is player 1 a human? if true type Y,y:") #input gör om strängen Y/y till en bool om sann sätt att spelare 1 människa, annars är spelare1människa False
if player1 == "Y" or player1 == "y":
    player1human = True

else:
    player1human = False

player2 = input("Is player 2 a human? if true type Y,y:")
if player2 == "Y" or player2 == "y":
    player2human = True

else:
    player2human = False #Sätter alla strängar förutom Y,y till false  playerNotStarting

startPlayer = 0
while startPlayer == 0:

    playerThatStarts = input("which player starts the game ,(1/2/random)")

    if playerThatStarts == "random":# väljer spelare 1 eller 2 ska börja slumpmässigt
        startPlayer = random.randint(1,2)

    elif playerThatStarts == "1" or playerThatStarts == "2":
        startPlayer = int(playerThatStarts)
    else :
        print("you must type 1/2 or random")
if startPlayer == 1: #om startPlayer är 1 då börjar spelare 1
    playing_kalaha_game(True,board,player1human,player2human)
else:
    playing_kalaha_game(False, board, player1human, player2human)  #om startPlayer = 2 då börjar spelare 2.