#Day2 deals with data types, numbers, operations, type conversions and f-strings
# print("hello"[0])
#the above code line is called subscripting.
#replacing the commas in numbers with underscores
#remember floating point numbers
#also boolean(true or false)
#len() cannot work with intergers remember that
# you can only concat strings and not intergers
# sup= type("chamberlain")
# print(sup)
#thrs also type conversion or typ[e casting]
#first excecise for day 2
# two_digit_number = input("type two digit number ")
# first_number= two_digit_number[0]
# second_number= two_digit_number[1]

# sum= int(first_number) + int(second_number)
# print(sum)
#there is another thing i learnt
# print(2**9)#means 2 to the power of 9
#all these can be arranged using PEMDAS

#

# height = input("enter the height in m: ")
# weight = input("enter the weight in kg: ")

# BMI = int(weight)/float(height)**2


# print(float(BMI))

#print(round(2.666668,2))
#take note of the count use +=, -=, *=
#fstrings, incoperTE different datatypes
# score=100
# height=1.8
# isWnning= True
# #f-string
# print(f"your inormation is {score}, {height} and {isWnning}")
# age= input("What is your current age?: ")
#maximum age to leave is 90
# num_of_years_left= 90-int(age)
# num_of_days= num_of_years_left*365
# num_of_weeks= num_of_years_left*52
# num_of_months = num_of_years_left*12

# print(f"You have {num_of_days} days, {num_of_weeks} weeks and {num_of_months} months left")
print("Welcome to the tip calculator")
total= input("What was the total bill? $")
total=float(total)
tip= input("What Percentage tip do you want to give? 10, 12 or 15 ")
tip= float(tip)
if (tip<10):
    input("input tip tip 10 percent and above")
else: 
     tip
     
totalwithtip= total* (1+tip/100)
      
        
    
split= input("How many people to split the bill? ")
split = int(split)
pay=round(totalwithtip/split,2)

print(f"Each person should pay: ${pay}")

