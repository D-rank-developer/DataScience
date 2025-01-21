#today is about python aritmatic operation and assignment
#day 3.2 using modulo % for odd and even numbers
# number = int(input("type in your number: "))

# if (number % 2 == 0):
#     print("this number is an even number")
# else:
#     print("this numer is an odd number")
# height = float(input("Enter the height in m:"))
# weight = float(input("enter your weight in kg:"))

# bmi= round(weight/(height**2))
# print(bmi)

# if bmi<18.5:
#     print("You are underweight")
# elif bmi>18.5 and bmi<25:
#     print("you are normal")
    
# elif bmi>25 and bmi<30:
#     print("you are overweight")
    
# elif bmi>30 and bmi<35:
#     print("you are obese")
# else:
#     print("you are clinically obese")

# year= int(input("which of the year you wanna check? "))

# if year%4==0 and year%100==0 and year%400==0:
#     print("the year is a leap year")
# else:
#     print(" the year is not a leap year")

#multiple if statements.
# print("Welcome to python pizza delivery")
# size= input("what size of pizza do you want? S, M or L ")
# add_pepperoni = input("Do you want Pepperoni? Y or N" )
# extra_cheese = input("Do you want extra cheese? Y or N")

# bill=0

# if size=="S":
#     bill += 15
# elif size=="M":
#     bill+= 20
# elif size =="L":
#     bill +=25
# if add_pepperoni=="Y":
#     if size == "S":
#         bill +=2
#     else:
#         bill+=3

# if extra_cheese == "Y":
#     bill +=1
    
# print(bill) 

print("Welcome to the love calculator")
name1 = input("what is your name?\n")
name2= input("what is their name\n")

combined_string= name1 + name2
lower_case_string= combined_string.lower()

t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")

true = t + r + u + e

l=lower_case_string.count("l")
o=lower_case_string.count("o")
v=lower_case_string.count("v")
e=lower_case_string.count("e")

love= l + o + v + e

love_score =int(str(true) + str(love))

if love_score<10 or love_score>90:
    print(f"your love score is{love_score}, you go like coke and mentos")
    
elif(love_score>=40) and (love_score<50):
    print(f"your score is {love_score}, you guys are alright together")
else:
    print(f"your score is {love_score}")

   
            
            

    
    

    
    
    
