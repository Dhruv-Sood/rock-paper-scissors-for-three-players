import random
#0 represents p1 wins and 1 represents p2 wins if its a tie Automatically p1 wins
def pvp(p1Choice,p2Choice):
    if (p1Choice == 'rock' and p2Choice == 'scissor'):
        return 0
    elif (p1Choice == 'rock' and p2Choice == 'paper'):
        return 1
    elif (p1Choice == 'rock' and p2Choice == 'rock'):
        return 0
    elif (p1Choice == 'paper' and p2Choice == 'paper'):
        return 0
    elif (p1Choice == 'paper' and p2Choice == 'rock'):
        return 0
    elif (p1Choice == 'paper' and p2Choice == 'scissor'):
        return 1
    elif (p1Choice == 'scissor' and p2Choice == 'scissor'):
        return 0
    elif (p1Choice == 'scissor' and p2Choice == 'rock'):
        return 1
    elif (p1Choice == 'scissor' and p2Choice == 'paper'):
        return 0
while(True):
    print('''This is a game of rock,paper,scissor
    There are total 3 players in this game
    Player 1 - Bot
    Player 2 - Bot
    Player 3 - User
    ''')
    print("To Play this game type \"start\"")
    while(True):
        x=input()
        if (x == "start"):
            break
        else:
            print("Please type \"start\" to continue")
    choices = ["rock" , "paper" , "scissor"]
    print('''Please make a choice
    1.)rock
    2.)paper
    3.)scissor''')
    p3Choice = input()
    while(True):
        if(p3Choice == "rock" or p3Choice == "paper" or p3Choice == "scissor"):
            break
        else:
            print("Please enter a valid choice : ")
            p3Choice = input()
    p1Choice = random.choice(choices)
    print("\nPlayer 1 chose",p1Choice)
    p2Choice = random.choice(choices)
    print("Player 2 chose",p2Choice)
    print("Player 3 chose",p3Choice+"\n")

    result1 = pvp(p1Choice,p2Choice)
    if(result1 == 0):
        print("Out of Player 1 and Player 2\nPlayer 1 Wins\n")
        result2 = pvp(p1Choice,p3Choice)
        if (result2 == 0):
            print("Out of Player 1 and Player 3\nPlayer 1 Wins\n")
        else:
            print("Out of Player 1 and Player 3\nPlayer 3 Wins\n")
    else:
        print("Out of Player 1 and Player 2\nPlayer 2 Wins\n")
        result2 = pvp(p2Choice,p3Choice)
        if (result2 == 0):
            print("Out of Player 2 and Player 3\nPlayer 2 Wins\n")
        else:
            print("Out of Player 2 and Player 3\nPlayer 3 Wins\n")
    print("To continue this game press \'y\' to exit press any character")
    x = input()
    if(x != 'y'):
        break
