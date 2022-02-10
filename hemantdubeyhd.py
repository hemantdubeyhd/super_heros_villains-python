##############################################################################
#  PSP Assignment 2
##############################################################################
#File : hemantdubeyhd.py
#Author : Hemant Dubey
#Stud ID : 110343214
#Email ID : hemantdubeyhd@gmail.com
#This is my own work as defined by the
#University's Academic Misconduct Policy.
#####################################################


import random   #importing random to use in file when as needed in program

#############################################################################################      
# Definig Function read_file(), takes input as a file to be reead and separates the
# all names and charactiristics to use individually, e.g., name secrect identity, battle data etc.

def readFile(fileToRead):

    character_list = [] # List to store information on heroes and villains (character list)
    
    infile = open(fileToRead, "r") #opening the desired file in redd mode

    line = infile.readline() # Reading first line of file.

   
    while line != '':  # While not end of file reached i.e. empty string not returned from readline method.

        name = line.strip('\n') # Get name

        line = infile.readline()  # Read in next line
        
        secret_id = line.strip('\n') # Get secret_identity

        
        line = infile.readline() # Read in next line
        
        # Followinf spliting lines into no battles, no won, no lost, etc.
        
        info_list = line.split()
        is_hero = info_list[0]
        no_battles = int(info_list[1])
        no_won = int(info_list[2])
        no_lost = int(info_list[3])
        no_drawn = int(info_list[4])
        health = int(info_list[5])        
        
        # Create new list to store individual character information
        new_character = [name, secret_id, is_hero, no_battles, no_won, no_lost, no_drawn, health]
        
        # Add new character to character_list (creating a list of lists)
        character_list.append(new_character)
        
        # Read next line of file.
        line = infile.readline()

    infile.close() #closing the file opened above
    
    return character_list  #returning list of individual character after reading from file

###########################################################################################################################################

# Function display_characters() -
# on the basis of user's choice either Display information of every charaters or only heroes' or only villains'

def displayCharacters(characterList, displayType):
    
    if displayType == 0:                                                    #condition if all characters need to be displayed, 
                                                                            #followinng lines in this if statement defines formate of headings of list displayed
        print("====================================================")
        print("- Character (heroes and villains) Summary          -")
        print("====================================================")
        print("-", end = '')
        print("                               ", end = '')
        print(format("P", '<3s'), end  = '')
        print(format("W", '<3s'), end  = '')
        print(format("L", '<3s'), end  = '')
        print(format("D", '<3s'), end  = '')
        print(format("Health -", '>5s'))
            
        for character in characterList:                                     #printing desired characters, here its displaying all characters
            print("----------------------------------------------------")    #following lines in this for loop diplaying all characters
            print(character[0], end = '')
            space = (30 - len(character[0]))
            for temp in range(space):
                print(" ", end = '')
            print(format(character[3], '3d'), end = '')
            print(format(character[4], '3d'), end = '')
            print(format(character[5], '3d'), end = '')
            print(format(character[6], '3d'), end = '')
            print(format(character[7], '^7d'), end = '')
            print(format("  -", '>2s'))
            
    elif displayType == 1:                                                  #condition to print only heroes
        print("====================================================")
        print("- Character (heroes and villains) Summary          -")
        print("====================================================")
        print("-", end = '')
        print("                               ", end = '')
        print(format("P", '<3s'), end  = '')
        print(format("W", '<3s'), end  = '')
        print(format("L", '<3s'), end  = '')
        print(format("D", '<3s'), end  = '')
        print(format("Health -", '>5s'))
        for character in characterList:
            if character[2].lower() == 'h':                                     # making sure it print only hero
                print("----------------------------------------------------")
                print(character[0], end = '')
                space = (30 - len(character[0]))
                for temp in range(space):
                    print(" ", end = '')
                print(format(character[3], '3d'), end = '')
                print(format(character[4], '3d'), end = '')
                print(format(character[5], '3d'), end = '')
                print(format(character[6], '3d'), end = '')
                print(format(character[7], '^7d'), end = '')
                print(format("  -", '>2s'))
              
    elif displayType == 2:                                                      # making sure it print only villains
        print("====================================================")
        print("- Character (heroes and villains) Summary          -")
        print("====================================================")
        print("-", end = '')
        print("                               ", end = '')
        print(format("P", '<3s'), end  = '')
        print(format("W", '<3s'), end  = '')
        print(format("L", '<3s'), end  = '')
        print(format("D", '<3s'), end  = '')
        print(format("Health -", '>5s'))
        for character in characterList:
            if character[2].lower() == 'v':
                print("----------------------------------------------------")
                print(character[0], end = '')
                space = (30 - len(character[0]))
                for temp in range(space):
                    print(" ", end = '')
                print(format(character[3], '3d'), end = '')
                print(format(character[4], '3d'), end = '')
                print(format(character[5], '3d'), end = '')
                print(format(character[6], '3d'), end = '')
                print(format(character[7], '^7d'), end = '')
                print(format("  -", '>2s'))
    print("----------------------------------------------------")
    print("\n====================================================")
               
#######################################################################################################################################        

# Function write_to_file() - this function updates the file as per last choice enterd by user
def writeToFile(filename, characterList):
    outfile = open(filename, "w") #opening file in write mode, it will always overwrite old file if exist in folder
    #index = 0
   
    for char in characterList: #loop to write whole list in file

        #following three lined defined that in what formte data is stored in desired file

        outfile.write(char[0] + "\n")
        outfile.write(char[1] + "\n")
        outfile.write(str(char[2]) + " " + str(char[3]) + " " + str(char[4]) + " " + str(char[5]) + " " + str(char[6]) + " " + str(char[7])+ "\n")
            
        
    outfile.close() # closing the file
    

#######################################################################################################################################
    #########################################################################



# Function find_character() - place your own comments here...  : )

def findCharacter(characterList, name):
    index = 0                               #variable to step on each record to find if character name exists in file or not
    flag = -1                               # to save place/index at character is stored at, if name is found

    while index < len(characterList):       # To search in whole list
        character = characterList[index]    #storing name in variable
        if name == character[0]:            #if found, then,
            flag = index                    #set save the position of name in list
        index += 1                          #increse index for 1 to keep looking untill found
    return flag                             #return position of name found or return flag as -1 if name does not exist in list

####################################################################################################################
#############################################################################################
       
  
   

#############################################################################################

# Function add_character() - After using findCharacter, this function update file with new character if doenot already exists.

def addCharacter(characterList, name, secret_id, is_hero):      #receiving input as list to update, and data to update
                addCharacter = []                               #creating new list to add new character
                addCharacter.append(newName)                    #Following lines updating all charactiristics/data related to new character to be added
                addCharacter.append(newSecretId)
                addCharacter.append(newHero)
                addCharacter.append(0)
                addCharacter.append(0)
                addCharacter.append(0)
                addCharacter.append(0)
                addCharacter.append(100)
                characterList.append(addCharacter)
                                
                writeToFile("characters.txt", characterList)    # after updating list writing it into file
    
    
               

    
##########################################################################################################################################  

# Function remove_character() -After using findCharacter, this function delete the desired character from file if doenot already exists.
def removeCharacter(characterList, name):                       # receiving input as list of character and character name to remove from list
    newList = []                                                #new list to have all the characters saved except the removed one
    index = 0                                                   # index to use in loop to reach till end of the list
    flag = findCharacter(characterList, name)                   # first checking existence of character
    
    if flag == -1:                                              #if character does not existss
        print("\n", name, "  is not found in characters")
    else:
        while index < len(characterList):                       #loop to check whole lists
            if index != flag:                                   #making sure postion of character to be removed is omitted
                newList.append(characterList[index])            #updating list
            index += 1                                          #increse index for 1 to keep loop running
        print("\nSuccessfully removed ", newName, " from character list.")

        writeToFile("characters.txt", newList)                 # wring updated list to file
        
    
########################################################################################################################################   

# Function display_highest_battles_won(), This function
def displayHighestBattlesWon(characterList):

    index = 1                                   # Index for loop to check every character in whole file/list, and as well using general index for looping
    flag = -1                                   #variable to see if zero battle are fought
    highest = 0                                 # value of Highest battle won by character
    lowest = 0                                  # value of lowest battle fought , if two character won same number of battles
    indexForSameHighest = []                    # Save the index of characters who won same number of battles
    indexLowestFought = 0                       #to save no of lowest battle fought

    #foollwin code store no of battle won by first character in list,
    #and store no of battle fought by first character

    if characterList[0][4] != 0:                #checking if first charater did not fought any battle
        flag = 1                                #flag to check any battle been fought or zero battle are fought
        highest = characterList[0][4]           #defult highest(no of battle won) value if any battle fought by first character in list
        lowest  = characterList[0][3]           #defult highest(no of battle fought) value if any battle fought by first character in list
        indexForSameHighest = 0                 #Saving position of character in list if any battle fought
   
    
    while index < len(characterList):           # this loop checks whole list for higest battle won by any character, an id battle won same the checks for lowest battle fought
        
        if characterList[index][4] > highest:   #if next character has higher no of battle of fought
            flag = 1                            # setting flag since batlles are fought.
            highest = characterList[index][4]   # updatding higest won to new highest won
            indexForSameHighest = index         #saving positons to check later if any characters have sam no of abttle fought
        elif characterList[index][4] == highest :
            if characterList[index][3] < lowest:# conditon to check who fought less battles, in case same no of battle fought
                indexForSameHighest = index -1  #saving postion of lowest battle fough
            else:
                indexForSameHighest = index     #saving positon of lowest battle fought on basis of above if condition
                 
        index += 1                              #increasing index to continue loop till end of list

        
 
    if highest == 0:                            #if zero battle fought
        print("\nall characters have zero battles won")

    if flag == 1:                               # if battles were fought then display the desired output
        print("\nHighest number of battles won => :", characterList[indexForSameHighest][0], " with ", highest, " opponents defeated!")
 
############################################################################################   

# Function do_battle() - place your own comments here...  : )
# Parameters: character_list - list of characters (list of lists).
#             opponent1_pos  - position/index of character in character_list.
#             opponent2_pos  - position/index of character in character_list.

def doBattle (characterList, opponent1Pos, opponent2Pos):
                  

            
            #rounds = 0
            rounds = int(input("\nPlease enter number of battle rounds: "))#rounds of battles to be enter by player

            newNoOfBattleFought = 0 #keeping account of how many battle fought again
            while rounds <= 0 or rounds > 5:# no of rounds can only be min 1 or max 5
                print("Must be between 1-5 inclusive.")
                rounds = int(input("\nPlease enter number of battle rounds: "))
               # print("Must be between 1-5 inclusive.")
            print("\n\n-- Battle --")
            print("\n", characterList[opponent1Pos][0], " versus ", characterList[opponent2Pos][0], " - ", rounds, " rounds \n") 

            while rounds > 0 and (characterList[opponent1Pos][7]> 0 and characterList[opponent2Pos][7] > 0 ) : #battling
                newNoOfBattleFought += 1  # counting battles
                print("\nRound: ", newNoOfBattleFought)
                damage = random.randint(0,50)       #generating random no which will damage the health of charcter
                characterList[opponent1Pos][7] -= damage  #updating damaged health
                print("  > ", characterList[opponent1Pos][0]," - Damage: ", damage, " - Current health: ", characterList[opponent1Pos][7])
                
                damage = random.randint(0,50) #generating random no which will damage the health of charcter
                characterList[opponent2Pos][7] -= damage #updating damaged health
                print("  > ", characterList[opponent2Pos][0]," - Damage: ", damage, " - Current health: ", characterList[opponent2Pos][7])

                if(characterList[opponent1Pos][7] < 0):  # if opponent one character dies, then
                    characterList[opponent1Pos][7] = 0   #udating health as 0
                    print("\n-- End of battle --")
                    print("\n-- ", characterList[opponent1Pos][0], " has died! :(")
                    print("**",characterList[opponent2Pos][0], " wins! **")
                elif(characterList[opponent2Pos][7] < 0): # if opponent two character dies, then
                    characterList[opponent2Pos][7] = 0    #udating health as 0
                    print("\n-- End of battle --")
                    print("\n-- ", characterList[opponent2Pos][0], " has died! :(")
                    print("\n** ",characterList[opponent1Pos][0], " wins! **")
                            
                elif characterList[opponent1Pos][7] == characterList[opponent2Pos][7]: # if health % is same
                    print("\nBattle Drawn")
                    characterList[opponent1Pos][6] += 1
                    characterList[opponent2Pos][6] += 1
                    
                elif characterList[opponent1Pos][7] > characterList[opponent2Pos][7]: # if opponent two character wins
                    characterList[opponent1Pos][4] += 1
                    characterList[opponent2Pos][5] += 1
                    print("\n-- End of battle --")
                    print("\n** ",  characterList[opponent1Pos][0], " wins! **")
                    
                elif characterList[opponent2Pos][7] > characterList[opponent1Pos][7]:  # if opponent two character wins
                    characterList[opponent1Pos][5] += 1
                    characterList[opponent2Pos][4] += 1
                    print("\n-- End of battle --")
                    print("\n** ",  characterList[opponent2Pos][0], " wins! **")
                    input()
                

                    
                rounds -= 1  # keeping account of no of baatles fought
            #print("printing newNoOfBattleFought: ", newNoOfBattleFought)
                
            input()
            characterList[opponent1Pos][3] += newNoOfBattleFought 
            characterList[opponent2Pos][3] += newNoOfBattleFought
            
                    
                
          
            writeToFile("characters.txt", characterList)    #updating new data in file
           
                

####################################################################################################################   

    
# Function sort_by_health() - place your own comments here...  : )
def sortByHealth(characterList):
    newCharacterList = characterList  # saving list so we original list doesnot get modified
   
    #index = 1                         
    maxIndex = len(newCharacterList)
    
    ###Following for loop "SORT" the list in descending order of health, and save it in newCharacterList
    for mainLoop in range(maxIndex):
        for innerLoop in range(mainLoop + 1, maxIndex):
            if newCharacterList[mainLoop][7] < newCharacterList[innerLoop][7]:
                temp=  newCharacterList[mainLoop]
                newCharacterList[mainLoop] = newCharacterList[innerLoop]
                newCharacterList[innerLoop] = temp
            elif newCharacterList[mainLoop][7] == newCharacterList[innerLoop][7]:
                if newCharacterList[mainLoop][3] < newCharacterList[innerLoop][3]:
                    temp=  newCharacterList[mainLoop]
                    newCharacterList[mainLoop] = newCharacterList[innerLoop]
                    newCharacterList[innerLoop] = temp


    displayCharacters(newCharacterList, 0)  # sending new list to display on screen, 0 prompts to display function that whole list need to be prited
          
    
################################################################################################################################
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                #MAIN#
#FOLLOWING IS THE MAIN MENU, IT DISPLAYS LIST OF CHOICES FOR USER TO MANIPULATE, MAINTAIN AND STORE THE DATA OF CHARACTERS(HEROES AND VILLAINS) IN FILE AS PER THEIR CHOICES,
#AND THEN DIPSLAYS DATA FROM FILE /LIST OF CHARACTERS
#PROGRAMM STARTS FROM HERE


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#####################################################################################################################################
#######################################################################################################

print("File : hemantdubeyhd.py")
print("Author : Hemant Dubey")
print("Stud ID : 110343214")
print("Email ID : hemantdubeyhd@gmail.com")
print("This is my own work as defined by the")
print("University's Academic Misconduct Policy.")
print("")
print("")

characterList = []          #Defining list to store character information

characterList = readFile("characters.txt") #calling function readFile() so can use
                                           #information i file as per user's choice

#Displaying list of choice and askinf user to enter their chioice:-
menuChoice = input("\nPleae enter choice\n[list, heroes, villains, search, reset, add, remove, high, battle, health, quit]: ")

if menuChoice == 'quit':    #if player chose to quit in first attempt
    writeToFile("new_characterList.txt", characterList)
    print("\n\n-- Program terminating --\n")
    input()
else:
    while menuChoice != "quit":
        #menuChoice = input("\nPleae enter choice\n[[list, heroes, villains, search, reset, add, remove, high, battle, health, quit]: ")
        menuChoice = menuChoice.lower()  #making input choice general case, independet of case(upper, lower or mixed)
        if menuChoice == 'list' or menuChoice == 'heroes' or menuChoice == 'villains' or menuChoice == 'search' or menuChoice == 'reset' or menuChoice == 'add' or menuChoice == 'remove' or menuChoice == 'high' or menuChoice == 'battle' or menuChoice == 'health' or menuChoice == 'quit':
        
            if menuChoice == 'list':
                displayCharacters(characterList, 0)

            elif menuChoice == 'heroes':
                displayCharacters(characterList, 1)

            elif menuChoice == 'villains':
                displayCharacters(characterList, 2)

            elif menuChoice == 'search':
                name = input("\nPlease enetr the name: ")
                flag = findCharacter(characterList, name) #calling function findCharcter and saving return value to check if character found or not
                if flag == -1:                            #  if character not found
                    print(name, " is not found in character (heroes and villains) list")
              
                else:                                     # if character found in file of characters
                    character = characterList[flag]       # abstarcting characters positing from list of lists
                    print ("\nAll about ", name, " --> ", end = "")
                    if character[2] == 'h':               #if character found is Hero 
                        print("HERO")
                    else:
                        print("VILLAIN")
                    print("\nSecret identity: ", character[1], "\n", "Battles fought: ", character[3], "\n", "  > No won: ", character[4], "\n", "  > No lost: ", character[5], "\n", "  > No drawn: ", character[6], "\n", "\nCurrent health: ", character[7], "%", sep = '')
                    
            elif menuChoice == 'add':
                newName = input("Please enter name: ")
                newSecretId = input("Please enter secret_identity: ")
                newHero = input ("Is this character a hero or a villain [h|v]? ")
                flag = findCharacter(characterList, newName) #calling function findCharcter and saving return value to check if character found or not
                if flag != -1:                               #if character already exists
                    print("\nThe ", newName, " already exists in character list")
                    #input()
                   
                else:                                                               #if character doesnot exist in file, then,
                    addCharacter(characterList, newName, newSecretId, newHero)      # adding it.
                    print("\nSuccessfully added ", newName, " to character list.")
                    #input()
                    
            elif menuChoice == 'remove':
                newName = input("Please enter name: ")

                removeCharacter(characterList, newName)                             #Calling function to remove character on basis of input by player
                                                                                    # And on basis if it exists in file or not
                characterList = readFile("characters.txt")
                

            elif menuChoice == 'high':
                displayHighestBattlesWon(characterList)                             #calling function to display who won max battles,
                                                                                    #on the basis that who fought min battles if any characters won same numbers of battles
                #input()

            elif menuChoice == 'reset':
                name = input("\nPlease enetr the name: ")
                flag = findCharacter(characterList, name)                           #calling function find character, if it exists in file
                if flag == -1:                                                      #if it doesnot exists in file
                    print("\n", name, " is not found in character (heroes and villains) list")
                    #input()
                else:                                                               #if character found in file,
                    characterList[flag][7] = 100                                    #updating/saving: its health must be 100% (or 100 in file)
                    print("\n Successfully updated ", characterList[flag][0],"'s health to 100")
                    #print("characterList[flag]: ", characterList[flag])             #printing to screen the new information
                    writeToFile("characters.txt", characterList)                    #updating new information in file

            elif menuChoice == 'battle':
                charOneIndex = 0                                        #to save 1st opponent's position
                charTwoIndex = 0                                        #to save 2st opponent's position
                found = -1                                              #Flag variable if name found in file, then set flag found 'non -1' number
                while found == -1:                                      #until name is found in file flag found remains -1
                    name = input("\nPlease enter opponent one's name: ")
                    flag = findCharacter(characterList, name)           #searching for name in file
                    if flag == -1:                                      #condition is name doesnot exist in file
                        print(name, " is not found in character (heroes and villains) list - please enter another opponent!")
                        #input()
                    else:
                        charOneIndex = flag                             #saving char 1st's position in file/list
                        found = 1                                       # if name found in file so can finish the looping
                    
                found = -1                                              #resetting flag to search next opponent
                while found == -1:                                      #until name is found in file flag found remains -1
                    name = input("\nPlease enter opponent two's name: ")
                    flag = findCharacter(characterList, name)           #searching for name in file
                    if flag == -1:                                      #condition is name doesnot exist in file
                        print(name, " is not found in character (heroes and villains) list - please enter another opponent!")
                        #input()
                    else:
                        charTwoIndex = flag                             #saving char 2nd's position in file/list
                        found = 1                                       # if name found in file so can finish the looping
                
                doBattle (characterList, charOneIndex, charTwoIndex)    #starting battles, calling function doBattle()

            elif menuChoice == 'health':
                 sortByHealth(characterList)                            #calling function to display character list in deceding order of theit health value(max to min)
                 #input()         
                    
        else:
            print ("\nNot a valid command - please try again.\n\n")
        menuChoice = input("\nPleae enter choice\n[list, heroes, villains, search, reset, add, remove, high, battle, health, quit]: ")
        if menuChoice == 'quit':
                writeToFile("new_characterList.txt", characterList)
                print("\n\n-- Program terminating --\n")
                input()
        


