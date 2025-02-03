# #random code generator
#import random

# random_interger = random.randint(1,10)
# print(random_interger)

# randomFloat= random.random()*5
# print(randomFloat)

# love_score = random.randint(1,100)
# print(f"your love score is {love_score}")

# probability= random.randint(0,1)
# if probability==1:
#     print("heads")
# else:
#     print("tails")

# states_of_america =["Delaware", "Pennslyvania"]
# print(states_of_america[-1])
# states_of_america[1]="Detaware"
# print(states_of_america)
# states_of_america.append("california")
# print(states_of_america)
# states_of_america.extend(["chirpo", "vavincan"])
# print(states_of_america)#check for documentation
#code challenge
# import random
# name_string= input("Give me everybodys names, seperated by a comma.")
# names=name_string.split(",")##it turns to a list
# print(random.choice(names))
# num_names= len(names)
# random_names= random.randint(0, num_names-1)
# random_choice=names[random_names]
#print(random_choice)
#we will be working with the nested list, take note of the index error
#list within a list has [[]] for indications
#treasure map
# 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# horizontal= int(position[0])
# vertical= int(position[1])

# map[vertical-1][horizontal-1]="X"
#index manipulation
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
#print(f"{row1}\n{row2}\n{row3}")

#RockPaperScissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images=[rock, paper, scissors]
userchoice= int(input("what do you choose? type 0 for rock, 1 for paper or 2 for scissors.\n"))
print(game_images[userchoice])
computerchoice= random.randint(0,2)
print("the computer chose:")
print(game_images[computerchoice])

if userchoice>=3 or userchoice<0:
    print("You have an invalid number, you lose!")

elif userchoice==0 and computerchoice ==2:
    print("You win!")
elif userchoice==2 and computerchoice==0:
    print("You lose!")
elif userchoice < computerchoice:
    print("You lose!")
elif userchoice > computerchoice:
    print("You Win!")
elif userchoice==computerchoice:
    print("its a draw")

