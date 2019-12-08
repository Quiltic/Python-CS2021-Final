import tkinter as tk

from Swindle import Human, Bot, RunRound
import os

"""
todo:
- Display: shows the numbers on your dice and the number of dice that the opponent has
- MERGE JOSH AND Is FILES
"""



# initialization
root = tk.Tk()
root.title("Swindlestones")

# images initialization
#os.path.join
img_one = tk.PhotoImage(file=".\\faces\\one.gif")
img_two = tk.PhotoImage(file=".\\faces\\two.gif")
img_three = tk.PhotoImage(file=".\\faces\\three.gif")
img_four = tk.PhotoImage(file=".\\faces\\four.gif")
img_five = tk.PhotoImage(file=".\\faces\\five.gif")
img_six = tk.PhotoImage(file=".\\faces\\six.gif")
img_zero = tk.PhotoImage(file=".\\faces\\zero.gif")

dice_img = [img_zero,img_one,img_two,img_three,img_four,img_five,img_six]

# scale that takes in number of dice you're betting 
as_ = tk.Scale(root, from_=1, to=8,orient="horizontal")

# incremental box that takes in what dice face you are betting on
nx = tk.Spinbox(root,from_=1,to=6,width=2)

# list box that works as a log showing all text outputs

lb = tk.Listbox(root,w=50)
lb.insert(tk.END,"Welcome to Swindlestones:", "Rules: You cannot bet a number of dice ", "       less than the current bet.", "You cant bet the dice value less than ", "       the current bet with the same number of dice.", "If you think the total number of dice is", "       LESS than the bet number you can CALL.", "The left input is the face of the die,", "        and the slider is the amount you think there are.")

# Label that displays the dice that the player has and frame that holds the dice images
dv = tk.StringVar()
dv.set("Your Dice: " + str(Human.Dice))
dm = tk.Label(root,textvariable=dv,padx=5,pady=5) # tkinter StringVar

dt = tk.Frame(root)

dm2 = tk.Label(dt,image=img_one)
dm3 = tk.Label(dt,image=img_one)
dm4 = tk.Label(dt,image=img_one)
dm5 = tk.Label(dt,image=img_one)

dm_folder = [dm2,dm3,dm4,dm5]

def updateImgs(indice):
    c = 0
    while c < (len(indice)):
        dm_folder[c].configure(image=dice_img[indice[c]])
        c += 1
    
    while (c<4):
        dm_folder[c].configure(image=img_zero)
        c += 1
    
    dv.set("Your Dice: " + str(Human.Dice))


updateImgs(Human.Dice)

# button that throws a CALL
def callButton():
    quickRound((0,0,True))

    Human.newround()
    updateImgs(Human.Dice)

cb = tk.Button(root, text='CALL', command=callButton)

# button that throws a BET
def betButton():
    #if the bet is possible: (check both numbers)
    if (int(as_.get())>Bot.currentdice+Human.currentdice):
        print("Invalid bet: the total amount of dice is " + Bot.currentdice+Human.currentdice)
    elif (int(nx.get())>6 or int(nx.get())<=0):
        print("Invalid bet: the die face you bet on must be 1-6")
    else:
        print(as_.get(),nx.get())
        quickRound((int(as_.get()),int(nx.get()),False)) # do a round
    updateImgs(Human.Dice)

bb = tk.Button(root, text='BET', command=betButton) # change command

def quickRound(stuffs):
    P = RunRound(stuffs)
    if P == ("Dice",True):
        lb.insert(tk.END,f"You Bet: {stuffs[0]} Dice that are {stuffs[1]}'s")

        B = RunRound(Bot.Ai(Human.currentdice))
        while B == ("Dice",False): # Ai's turn
            B = RunRound(Bot.Ai(Human.currentdice))
        if B[0] == "Call":
            if B == ("Call", True):
                lb.insert(tk.END,f"They CALLED! And where Right! You Lost a Dice!", " ")
            else:
                lb.insert(tk.END,f"They CALLED! And where Wrong! They Lost a Dice!", " ")

            Human.newround()
            #redo the AI turn
            B = RunRound(Bot.Ai(Human.currentdice))
            while B == ("Dice",False): # Ai's turn
                B = RunRound(Bot.Ai(Human.currentdice))

        lb.insert(tk.END,f"The Bot Bet: {Bot.call[0]} Dice that are {Bot.call[1]}'s")

    elif P[0] == "Call":
        if P == ("Call", True):
            lb.insert(tk.END,f"You CALLED! And you where Right! They Lost a Dice!", " ")
        else:
            lb.insert(tk.END,f"You CALLED! And you where Wrong! You Lost a Dice!", " ")

    else:
        lb.insert(tk.END,"That Is INVALID! Try again.")
    


    if (Bot.currentdice == 0):
        lb.insert(tk.END, f"They have 0 Dice left. YOU WON!!")
    elif (Human.currentdice == 0):
        lb.insert(tk.END, f"YOU have 0 Dice left. YOU LOST!!")
    else:
        lb.insert(tk.END, f"They have {Bot.currentdice} Dice left.")
        dv.set("Your Dice: " + str(Human.Dice)) # reset dice
        updateImgs(Human.Dice)


#organizing all of the elements 
lb.pack(side=tk.TOP)
dm.pack()
dt.pack()
dm2.pack(side=tk.LEFT,padx=8)
dm3.pack(side=tk.LEFT,padx=8)
dm4.pack(side=tk.LEFT,padx=8)
dm5.pack(side=tk.LEFT,padx=8)
nx.pack(side=tk.LEFT,padx=8)
as_.pack(side=tk.LEFT,pady=10,padx=8)
bb.pack(side=tk.LEFT,padx=8)
cb.pack(side=tk.LEFT,padx=8)



root.mainloop()