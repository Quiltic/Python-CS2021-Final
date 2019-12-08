__author__ = "Josh Zack"
__email__ = "zackjm@mail.uc.edu"
#This is based on The game Swindelstones or Lires Dice

import random, os 

def dice(minval,maxval):
    return(random.randrange(minval,maxval+1))


class Player():
    def __init__(self, name,  num_of_dice = 4, max_val_of_dice = 6):
        self.name = name
        self.Dice = [dice(1,max_val_of_dice) for _ in range(num_of_dice)] # current dice
        self.currentdice = num_of_dice # number of dice remaining

        self.max_val_of_dice = max_val_of_dice # this is for later things

        # set up probabilitys with some randomness so you cant fully guess it
        self.prob = self.prob = [dice(0,1) for _ in range(self.max_val_of_dice)]
        for a in self.Dice:
            self.prob[a-1] += 1

        self.call = (0,0,False) # this is this persons call

    def newround(self):
        # new set of dice
        self.Dice = [dice(1,self.max_val_of_dice) for _ in range(self.currentdice)]
        # Update the probabilitys
        self.prob = self.prob = [dice(0,1) for _ in range(self.max_val_of_dice)]
        for a in self.Dice:
            self.prob[a-1] += 1


    # The AI
    def Ai(self,others_dice):
        lengthfull = self.currentdice + others_dice # total number of dice

        # if they say there is more dice then there achualy is
        if Important["Call"][0] > lengthfull:
            self.call = (0,0,True)
            return(self.call)


        if Important["Call"] != (0,0,False):
            # the Probability from 1-max_dice_val
            # add one onto the guessed number for probibility
            self.prob[Important["Call"][1]-1] += 1
                         
        
        prob = [a/lengthfull for a in self.prob] # the ending probabilty in %

        # if the prob of the dice being that is greater than the overall prob then call ?
        if prob[Important["Call"][1]-1] < (Important["Call"][0]/lengthfull):
            self.call = (0,0,True)
            return(self.call)

        # get the best probability/dice val for it
        best = 0 # best prob in %
        location = 0 # Dice val -1
        for a in range(len(prob)):
            if prob[a] > best:
                best = prob[a]
                location = a


        # (number of dice, number on the dice, if the last action was to CALL)
        self.call = (self.prob[location],location+1,False)
        #print(Important["Call"],Checker(self.call, 1, False),"Chacking")
        if self.call == (0,0,False):
            self.call = (dice(1,2), dice(1,self.max_val_of_dice),False)


        return(self.call)

    def killDice(self):
        self.currentdice -= 1


        """
        lengthfull = self.currentdice + others_dice # total number of dice
        if Important['Call'] == (0,0,True):
            return((1,self.Dice[dice(0,self.currentdice-1)],False))
        elif self.currentdice == 1:
            if Important['Call'][0] > 2:
                return((0,0,True))
            else:
                return((Important['Call'][0]+1,self.Dice[0],False))
        """
            
            
    """
    check = rename(ai_dice,num)
    if check >= int(lastcall[1]):
        flop = leterize(num,(int(lastcall[1])+1))
        Game(1,flop,lastcall)
    else:
        if ((int(lastcall[1]) > 3) and (ln >4)):
            ran = random.randrange(1,3)
            if ran < 2:
                flop = leterize(num,(int(lastcall[1])+1))
                Game(1,flop,lastcall)
            else:
                print('Ai: Call!')
                Game(1,"CALL",lastcall)
        elif ((int(lastcall[1]) > 3) and (ln < 4)):
            print('Ai: Call!')
            Game(1,"CALL",lastcall)
        else:
            ran = random.randrange(1,4)
        if ran < 3:
            flop = leterize(num,(int(lastcall[1])+1))
            Game(1,flop,lastcall)
        else:
            print('Ai: Call!')
            Game(1,"CALL",lastcall)

    else:
        if lastcall[0] == 'A':
            simple(ai_dice,lastcall,1,lengthfull)
        elif lastcall[0] == 'B':
            simple(ai_dice,lastcall,2,lengthfull)
        elif lastcall[0] == 'C':
            simple(ai_dice,lastcall,3,lengthfull)
        elif lastcall[0] == 'D':
            simple(ai_dice,lastcall,4,lengthfull)
        else:
            print('Ai: Call!')
            Game(1,"CALL",lastcall)
    """
        




def Checker(new, playerrr, passss = True):
    """
    Makes Sure the new data was legal
    """
    # failsafe
    if (Important["Player"] == playerrr):
        return(True)
    # (# of Dice, # on Dice)
    # both need to be less than the important call inorder to be valid
    if new[0] < Important["Call"][0]:
        print(new[0], Important["Call"][0])
        return(False)
    elif ((new[1] <= Important["Call"][1]) and (new[0] <= Important["Call"][0])):
        print(new, Important["Call"])
        return(False)

    # for the bot
    if passss:
        # change the data
        Important["Call"] = new
        Important["Player"] = playerrr
    
    return(True) # It's valid


def Call():
    """
    Checks to see if the preveous call was True or not

    Returns True if the person who called was right
    Returns False if they where Wrong
    """
    # get the totals for each dice
    totals = [0 for _ in range(Human.max_val_of_dice)]
    for Play in PlayerList:
        for d in Play.Dice:
            totals[d-1] += 1

    print(totals, totals[Important["Call"][1]-1],Important["Call"][1]-1)

    # Reset the round, Needs to be done first
    for Play in PlayerList:
        Play.newround()


    if Important["Call"][0] > totals[Important["Call"][1]-1]:
        print("Correct",PlayerList[Important["Player"]*-1].name)
        PlayerList[Important["Player"]*-1].killDice() # kills dice
        Important["Call"] = (0,0,False) # reset call
        return(True) # sucseeded in the call
    else:
        print("Fail",PlayerList[Important["Player"]].name)
        PlayerList[Important["Player"]].killDice() # kills dice
        Important["Call"] = (0,0,False) # reset call
        return(False) # failed the call
    
  

   
    

def RunRound(new):
    print("Bet: ", new)
    print(Human.Dice, Bot.Dice)
    # 1 is Bot, 0,-1 is Human
    if new[2] == True:
        return(("Call",Call()))
        # Reset the round?
        for Play in PlayerList:
            Play.newround()
    else:
        if Checker(new, Important["Player"]*-1): # new data, the current person is *-1 of the current one because maths
            print("Your Good")
            return(("Dice",True))
        else:
            print("BAD IMPUT!")
            return(("Dice",False))


  


# Call = number of dice, number on the dice, if the last action was to CALL
# Player = the player who made the bet (#)
Important = {"Call": (0,0,False), "Player": -1}

Human = Player("Human")
Bot = Player("Bot")
PlayerList = [Human, Bot, Human] # for later use for easy maths




# for testing realisticly not needed
if  __name__ == "__main__":
    print(Human.Dice)
    print(Bot.Dice, Bot.Ai(Human.currentdice))
    print(Bot.prob)
    

    RunRound(Bot.Ai(Human.currentdice))
    print('\n', Bot.call)
    
    
    print(Human.Dice)
    RunRound((int(input("Number of dice: ")), int(input("Number on the dice: ")), bool(input("CALL!?  (True/False): "))))
    print('\n')


    RunRound(Bot.Ai(Human.currentdice))
    print('\n', Bot.call)

    print(Human.currentdice,Bot.currentdice)


"""

#Dice role
#Ai Uses probability insted of randomness

person_dice = [0,0,0,0]
ai_dice = [0,0,0,0]


def role():
    for a in range(len(person_dice)):
        ran = random.randrange(1,7)
        person_dice[a] = ran
    print(person_dice)


    for a in range(len(ai_dice)):
        ran = random.randrange(1,7)
        ai_dice[a] = ran
    print('The ai has %s dice.' % (len(ai_dice)))

role()

def rename(ai_dice,num):
    token = 0
    for a in ai_dice:
        if a == num:
            token = token + 1
    return token
  

def leterize(num,amount):
    if num == 1:
          num = 'A'
    if num == 2:
          num = 'B'
    if num == 3:
          num = 'C'
    if num == 4:
          num = 'D'
    check = '%s%s' % (num,amount)
    print('Ai: %s' % (check))
    return check
  
def simple(ai_dice,lastcall,num,ln):
    check = rename(ai_dice,num)
    if check >= int(lastcall[1]):
        flop = leterize(num,(int(lastcall[1])+1))
        Game(1,flop,lastcall)
    else:
        if ((int(lastcall[1]) > 3) and (ln >4)):
            ran = random.randrange(1,3)
            if ran < 2:
                flop = leterize(num,(int(lastcall[1])+1))
                Game(1,flop,lastcall)
            else:
                print('Ai: Call!')
                Game(1,"CALL",lastcall)
        elif ((int(lastcall[1]) > 3) and (ln < 4)):
            print('Ai: Call!')
            Game(1,"CALL",lastcall)
        else:
            ran = random.randrange(1,4)
        if ran < 3:
            flop = leterize(num,(int(lastcall[1])+1))
            Game(1,flop,lastcall)
        else:
            print('Ai: Call!')
            Game(1,"CALL",lastcall)


def Ai(ai_dice,person_dice,lastcall):
    length = len(ai_dice)
    lengthfull = length + len(person_dice)
    
    if lastcall == False:
        ran = random.randrange(0,length)
        smallest = leterize(ai_dice[ran],1)
        Game(1,smallest,lastcall)
        '''
        smallest = 500
        for a in ai_dice:
        if a < smallest:
            smallest = a
        smallest = leterize(smallest,1)
        Game(1,smallest,lastcall)
        #'''
    elif length == 1:
        if (int(lastcall[1])+1) >=3:
            print('Ai: Call!')
            Game(1,"CALL",lastcall)
            smallest = ai_dice[0]
            smallest = leterize(smallest,(int(lastcall[1])+1))
            Game(1,smallest,lastcall)
    else:
        if lastcall[0] == 'A':
            simple(ai_dice,lastcall,1,lengthfull)
        elif lastcall[0] == 'B':
            simple(ai_dice,lastcall,2,lengthfull)
        elif lastcall[0] == 'C':
            simple(ai_dice,lastcall,3,lengthfull)
        elif lastcall[0] == 'D':
            simple(ai_dice,lastcall,4,lengthfull)
        else:
            print('Ai: Call!')
            Game(1,"CALL",lastcall)
      
  
  
#Done
def CALL(num,ai_dice,person_dice,player,lastcall):
    list = ['wub','Ai','Person']
    dice = [person_dice,ai_dice,person_dice]
    tally = 0
    for a in ai_dice:
        if a == num:
            tally = tally + 1
    for a in person_dice:
        if a == num:
            tally = tally + 1
  
    if int(lastcall[1]) <= tally:
        print('%s lost this round.' % (list[player])
        del(dice[player][0])
        input()
        os.system('clear')
        role()
    else:
        print('%s won this round.' % (list[player])
        del(dice[player-1][0])
        input()
        os.system('clear')
        role()
    global lastcalled
    lastcalled = False


#Done
lastcalled = False
def Game(player, call, lastcall):
    # A = 1
    # B = 2
    # exc.
    global lastcalled
    if (call == "CALL"):
        if "A" in lastcall:
            CALL(1,ai_dice,person_dice,player,lastcall)
        if "B" in lastcall:
            CALL(2,ai_dice,person_dice,player,lastcall)
        if "C" in lastcall:
            CALL(3,ai_dice,person_dice,player,lastcall)
        if "D" in lastcall:
            CALL(4,ai_dice,person_dice,player,lastcall)
    else:
        lastcalled = call

player = 1
while ((len(ai_dice) != 0) and (len(person_dice) != 0)):
    if player == 1:
        Ai(ai_dice,person_dice,lastcalled)
        player = 2
    else:
        call = str(input("What is your bet?  "))
        Game(2,call,lastcalled)
        player = 1



    
'''    
Game(1,'A6',lastcalled)
Game(2,'Call',lastcalled)
print(person_dice
print(ai_dice
#'''    

"""
