#This is a text adventure.
#@author Marius Haueis
#@version 09.04.2021
#

import numpy as np
import random
import time
roomCounter=0
totalRooms = 5
playerAlive = True
enemy =[]
playerStrength = 5
playerHP = 10
playerName = ""



#Introduction
def introduction():
    global playerName
    print("")
    print("Welcome to this Text adventure.")
    playerName = input("Please insert your name: ")
    print("Let's start our journey " + playerName+ ".")
    print("")

#end Text
def endSequenz():
    global playerAlive
    global roomCounter
    if playerAlive:
        print("")
        print("Light!!!")
        time.sleep(1)
        print("")
        print("There is Light")
        print("Hurra")
        time.sleep(1)
        print("You won this game")
        playAgain()
    else:
        print("Shame, shame, shame!")
        playAgain()


def playAgain():
    global playerStrength
    global playerHP
    global playerAlive
    global roomCounter
    time.sleep(1)
    ans = (input("Another round? [y] yes, [n] no: "))
    if ans == "y":
        roomCounter=0
        playerStrength = 5
        playerHP = 10
        playerAlive = True
        playGame()


#Playmaking
def playmaking():
    global totalRooms
    global roomCounter
    global playerAlive
    while (roomCounter < totalRooms) and playerAlive:
        #print room text
        roomPrintText()
        roomCounter +=1
        #summon box or enemy and fight if enemy
        summon()
    else:
        endSequenz()
#rooms
def roomPrintText():
    time.sleep(2)
    adjList = ("dark", "cold", "pestilently", "moisty")
    sizeList = ("small", "reasenable sized", "great", "narrow")
    ran = np.random.randint(0,4)
    print("You've entered a " + adjList[ran] + ", " + sizeList[ran] + " Room.")
        
def summon():
    global roomCounter
    if roomCounter > 1:
        ran = np.random.randint(0,2)
        if ran ==0:
            summonEnemy()          
        else:
            summonBox()
    else:
        summonBox()

#enemys
def summonEnemy():
    global enemy
    ran = np.random.randint(0,3)
    #typ:Attack power
    nameList = [("skelleton",1) , ("witch",3), ("giant",5)]
    #size:HP
    strengthList = [("tiny",8), ("scary",15), ("monstrous",25)]
    enemy = [nameList[ran], strengthList[ran]]
    time.sleep(2)
    print("")
    print("A " + enemy[1][0] +" "+ enemy[0][0]+ " appears")
    takeAction()
    

#boxes
def summonBox():
    global playerHP
    global playerStrength
    print("A box appears.")
    time.sleep(1)
    print("")
    print("Do you want to open this box?")
    bu = input("[o] open, [d] discard: ")
    if bu == "o":
        ran = np.random.randint(0,4)
        if ran == 3:
            print("This box is empty.")
        elif ran == 0:
            print("Power up")
            playerStrength += 2
        elif ran == 1:
            print("Oh no poison")
            playerStrength -=1
        else:
            print("HP. nice")
            playerHP += 3
        showPlayerStats()
    else:
        print("You dismissed the box.")
    time.sleep(2)
    print("")

#The fighting
def takeAction(): 
    global playerAlive   
    global enemy
    global playerHP
    global playerStrength   
    playerStartHealth = playerHP
    enemyAttack = enemy[0][1]
    enemyHP = enemy[1][1]
    print("Enemy Health: " + str(enemyHP))
    print("Enemy Attack power: " + str(enemyAttack))
    while enemyHP > 0 and playerHP > 0:
        print(playerName+" make your move.")
        act = (input("[a] attack, [h] heal, [f] flee, make your move: "))
        if act == "a":
            print("You attacked.")
            enemyHP -= playerStrength
        elif act == "h":
            print("You healed.")
            playerHP += int(playerStartHealth/5)
        elif act == "f":
            if playerHP < int(enemyAttack)*2:
                print("You HP is to low, you cannot flee.")
                continue
            else:
                print("You flee from the fight. Pathetic!")
                break
        print(enemy[1][0] + enemy[0][0]+ " attacks.")
        playerHP -= enemyAttack        
        showPlayerStats()
        print("Enemy health: "+ str(enemyHP))
        time.sleep(2)
        print("")
    if playerHP <= 0:
        print("")
        print("You died!")
        playerAlive = False
    elif enemyHP <= 0:
        print("")
        print("You won this fight.")
        showPlayerStats()
        playerHP = max(playerHP, playerStartHealth)
    print("")


#Prints the player Health and Strength.
def showPlayerStats():
    print("")
    print("Health: ")
    for n in range(playerHP-1):
        print("|", end ="")
    print("")
    print("Strength: ")
    for b in range(playerStrength-1):
        print("|", end ="")
    print("")

def playGame():
    introduction()
    playmaking()
    


playGame()
