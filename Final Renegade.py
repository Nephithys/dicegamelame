import os
import random
import time



print("""
                                                                              
                                                                                                       
                                                                                                       
                                                                                                       
                                                                                                       
                                                                                                       
                                                                                                       
                                                                                                       
 888888ba                                                     dP          
 88    `8b                                                    88          
a88aaaa8P' .d8888b. 88d888b. .d8888b. .d8888b. .d8888b. .d888b88 .d8888b. 
 88   `8b. 88ooood8 88'  `88 88ooood8 88'  `88 88'  `88 88'  `88 88ooood8 
  """)


time.sleep(.5)
os.system('cls')
print("""
                                                                             
                                                                                    
                                                                                
                                                                               
                                                                                
                                                                                 
 888888ba                                                     dP          
 88    `8b                                                    88          
a88aaaa8P' .d8888b. 88d888b. .d8888b. .d8888b. .d8888b. .d888b88 .d8888b. 
 88   `8b. 88ooood8 88'  `88 88ooood8 88'  `88 88'  `88 88'  `88 88ooood8 
 88     88 88.  ... 88    88 88.  ... 88.  .88 88.  .88 88.  .88 88.  ... 
 dP     dP `88888P' dP    dP `88888P' `8888P88 `88888P8 `88888P8 `88888P' 
                                           .88                            
                                       d8888P   """)
                                       
time.sleep(.5)
os.system('cls')
print("""                                                                                                                                                              
                                                                                
                                                                               
                                                                                
                                                                                 
 888888ba                                                     dP          
 88    `8b                                                    88          
a88aaaa8P' .d8888b. 88d888b. .d8888b. .d8888b. .d8888b. .d888b88 .d8888b. 
 88   `8b. 88ooood8 88'  `88 88ooood8 88'  `88 88'  `88 88'  `88 88ooood8 
 88     88 88.  ... 88    88 88.  ... 88.  .88 88.  .88 88.  .88 88.  ... 
 dP     dP `88888P' dP    dP `88888P' `8888P88 `88888P8 `88888P8 `88888P' 
                                           .88                            
                                       d8888P   """)
 
time.sleep(.5)
os.system('cls')
 
print("""                                                                                                                                                              
                                                                                
                                                                                                                                                                                                                                             
 888888ba                                                     dP          
 88    `8b                                                    88          
a88aaaa8P' .d8888b. 88d888b. .d8888b. .d8888b. .d8888b. .d888b88 .d8888b. 
 88   `8b. 88ooood8 88'  `88 88ooood8 88'  `88 88'  `88 88'  `88 88ooood8 
 88     88 88.  ... 88    88 88.  ... 88.  .88 88.  .88 88.  .88 88.  ... 
 dP     dP `88888P' dP    dP `88888P' `8888P88 `88888P8 `88888P8 `88888P' 
                                           .88                            
                                       d8888P   """)

time.sleep(.5)
os.system('cls')
                                       
print("""                                                                                                                                                              
 888888ba                                                     dP          
 88    `8b                                                    88          
a88aaaa8P' .d8888b. 88d888b. .d8888b. .d8888b. .d8888b. .d888b88 .d8888b. 
 88   `8b. 88ooood8 88'  `88 88ooood8 88'  `88 88'  `88 88'  `88 88ooood8 
 88     88 88.  ... 88    88 88.  ... 88.  .88 88.  .88 88.  .88 88.  ... 
 dP     dP `88888P' dP    dP `88888P' `8888P88 `88888P8 `88888P8 `88888P' 
                                           .88                            
                                       d8888P   
                                                                           
                                                                           
                   <(^.^)> Press Enter To Start <(^.^)>                                
                                       """)
input("")
os.system('cls')

print("""
Hi, welcome to Renegade, the virtual awful drinking game simulator. 
Feel free to tag along with the virltual players, but just keep in 
mind that Renegade is not responsible for damage to property or 
person Upon discovering that damage or death has occurred, a missing 
person report will be filed within 90 days, or as soon property and 
premises have been thoroughly cleaned and bleached, and the 
carpets have been replaced.

*Hit enter if you stil wish to continue*
""")
input("")

os.system("cls")
list1 = [1,2,3,4,5,6];
list2 = [1,2,3,4,5,6,7,8];
list3 = [1,2,3,4,5,6,7,8,9,10,11,12];

d1 = random.choice(list1)
d2 = random.choice(list2)
d3 = random.choice(list3)

guesses = 0
Guess1 = int(input("Guess a number between 1-6 player 1 "))
Playing = True
while(Playing):
    print("Guess a number between on a 6 sided die")
    Guess1 = int(input("What is your guess player 1? "))
    if (Guess1 > 6 or Guess1 < 1):
        invalid = True
        while(invalid):
            print("Invalid number guess again. Guess a number between 1 - 6")
            Guess1 = int(input("Guess a number between 1-6 player 1 "))
            if (6 >= Guess1 >= 1):
                invalid = False 
    guesses += 1            
    if (Guess1 == d1):
        print("Yay you guessed it.")
        Playing = False
    elif (Guess1 > d1):
        print("Your guess was too high. Guess again :D ")
    else:
        print("Your guess was too low. Try again ._. ")
        
        
print("                                                              ")
print("                                                              ")
print("Press enter to continue")
               
input("")
Playing = True
while(Playing):
    print("Guess a number between on a 6 sided die")
    Guess1 = int(input("What is your guess player 2? "))
    if (Guess1 > 6 or Guess1 < 1):
        invalid = True
        while(invalid):
            print("Invalid number guess again. Guess a number between 1 - 6")
            Guess1 = int(input("Guess a number between 1-6 player 2 "))
            if (6 >= Guess1 >= 1):
                invalid = False 
    guesses += 1            
    if (Guess1 == d1):
        print("Yay you guessed it.")
        Playing = False
    elif (Guess1 > d1):
        print("Your guess was too high. Guess again :D ")
    else:
        print("Your guess was too low. Try again ._. ")
        
print("                                                              ")
print("                                                              ")
print("Press enter to continue")
               
input("")

Playing = True
while(Playing):
    print("Guess a number between on a 8 sided die")
    Guess1 = int(input("What is your guess player 1? "))
    if (Guess1 > 8 or Guess1 < 1):
        invalid = True
        while(invalid):
            print("Invalid number guess again. Guess a number between 1 - 8")
            Guess1 = int(input("Guess a number between 1-8 player 1 "))
            if (8 >= Guess1 >= 1):
                invalid = False 
    guesses += 1            
    if (Guess1 == d2):
        print("Yay you guessed it.")
        Playing = False
    elif (Guess1 > d2):
        print("Your guess was too high. Guess again :D ")
    else:
        print("Your guess was too low. Try again ._. ")
        
print("                                                              ")
print("                                                              ")
print("Press enter to continue")
               
input("")

Playing = True
while(Playing):
    print("Guess a number between on a 8 sided die")
    Guess1 = int(input("What is your guess player 2? "))
    if (Guess1 > 8 or Guess1 < 1):
        invalid = True
        while(invalid):
            print("Invalid number guess again. Guess a number between 1 - 8")
            Guess1 = int(input("Guess a number between 1-8 player 2 "))
            if (8 >= Guess1 >= 1):
                invalid = False 
    guesses += 1            
    if (Guess1 == d2):
        print("Yay you guessed it.")
        Playing = False
    elif (Guess1 > d2):
        print("Your guess was too high. Guess again :D ")
    else:
        print("Your guess was too low. Try again ._. ")
        
print("                                                              ")
print("                                                              ")
print("Press enter to continue")
               
input("")

