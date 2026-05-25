# name = input('what is your name?: ')
# while name.isdigit:
#  print('you entered an invalid letter')
    # name = input('what is your name?: ')
# print(f"welcome {name}")
# for x in range(1, 11):
    # print(x)
# from curses.ascii import isdigit

# principle = 0
# rate = 0
# time = 0

# while principle <= 0:
   # principle = float(input('Enter the principle amount (1-10): '))
   # if principle <= 0:
  #       print('invalid number, kindly input try again ')
# while rate <= 0:
  #  rate = float(input('Enter the rate (1-10): '))
 #   if principle <= 0:
#      print('invalid number, kindly input try again ')
# while time <= 0:
    # time = int(input('Enter the given years (1-10): '))
    # if principle <= 0:
        # print('invalid number, kindly input try again ')
# total = principle * pow((1 + rate / 100), time)
# print(f'balance after {time} years/s: ${total:.2f} ')
# for x in range(1, 21):
    # if x == 17:
       # break/continue (break to break out of the loop while continue to skip the certain number eg, x == 17, skip 17)
  #  else:
   #     print(x)
#import time
#my_time = int(input('enter the time in seconds'))
#for x in reversed(range(0, my_time)):
   # print(x)
  #  time.sleep(1)

# print("time's up")
# name = input('What is your name?: ')

# while name.isdigit():
#  print("enter a valid name")
    #   name = input('What is your name?: ')
#while age == '' :
#  age = int(input('How old are you?: '))
    #   if age <= 17 or age >= 50:
#    print("ypu must be up tp the required age")
        #        print("ypu must be up tp the required age")

#  relationship_status = input('What is your relationship_status ?: ')
# while relationship_status == '' :
#     print("This section can`t be blank")
    #     relationship_status  = input('What is your relationship_status ?: ')
# country = input('Enter country/region: ')
# while country == '' :
#     print("input a valid country")
    #     country = input('Enter country/region: ')


# print(f"hello {name}, welcome to enterprises")
# print(f"you are {age} years old")
# print(f"you are {relationship_status}, and you are from {country} ")
# print("your information has been reviewed successfully, you are qualified to use our website")

# my_time = int(input(""Enter the time in seconds: "))

# for x in range(my_time, 0, -1):
    # seconds = x % 60
   # minutes = int(x / 60) % 60
  #  hours = int(x / 3600)
 #   print(f"{hours:02}:{minutes:02}:{seconds}")
#    time.sleep(1)
#for x in range(3):
 #   for y in range(1, 10):
  #      print(y, end="")
   # print()
# temp = int(input("Enter the temperature: "))
# is_raining = False
# if temp > 35 or temp < is_raining:
  #  print("The outdoor event is cancelled.")
# else:
  #  print("the outdoor event is still scheduled")
# name = input("What is your name. (do not include spaces): ")
# name.len()
# while name.count(" ") > 0:
  #  print("Your name can't have spaces ")
   # name = input("What is your name: ")
# print(name)
#num_of_students = {
#    "bola": 75,
#    "ade": 46,
#    "ada": 58,
#    "rita": 37,
#    "ope": 78,
#    "sey": 93
#}
#by = "Passed"
#fx = "Failed"
#key = num_of_students.keys()
#value = num_of_students.values()
#for key, value in num_of_students.items():
#    if value >= 50:
#        print(f" {key}:{by}")
#    else:
#        print(f" {key}:{fx}")
# variables: string, this is a series of text withing a double or singe quote.
# name = ope

# print(name)

# integers: this are whole numbers
#age = 18

#print(age)

# float: this are decimals
#gpa = 3.78

#print(gpa)

# boolean = this function is either true or false
#is_student = True

#print(is_student)

#typecasting is the process of converting a variable to another data type. eg:
#name = "ope"
#age = 18
#gpa = 3.78
#is_student = True

#gpa = int(gpa)

#print(gpa)

#name = bool(name)
#print(name)
# for the string and bool, the bool will always show false when an empty string is there and true when a string is there

# input(): this is a function that allows the user to enter data. eg
#name = input("What is your name?: ")
#age = int(input("how old are you?: "))
#age += 1
#print(f"Hello {name}")
#print("Happy birthday")
#print(f"you are {age} years old!!")

# calculating the area of a rectangle, eg.
# formual is A=WL
#length = float(input("Enter the length: "))
#width = float(input("Enter the width: "))
#area = length * width

#print(f"your area is {area}")

# Shopping cart program
#item = input("what item would you like to buy?: ")
#quantity = int(input("How many would you like to buy?: "))
#price = float(input("enter the amount: "))
#total = quantity * price

#print(f"you have bought {quantity} {item}s")
#print(f"your total is {total}")

#madlibs game
# a word game where you create a strory by filling in blanks with random words

#adejective1 = input("Enter an adjective. (description): ")
#noun1 = input("Enter a noun. (name, place or thing): ")
#adejective2 = input("Enter an adjective. (description): ")
#verb1 = input("Enter a verb ending with 'ing': ")
#adejective3 = input("Enter an adjective. (description): ")


#print(f" Today i went to a {adejective1} zoo")
#print(f"in an exhibit i saw a {noun1}")
#print(f"{noun1} was {adejective2} and {verb1}")
#print(f"i was {adejective3}")

#operator = input("Enter an operator (+, -, *, /): ")
#num1 = float(input("Enter the 1st number: "))
#num2 = float(input("Enter the 2nd number: "))

#if operator == "+":
#    result = num1 + num2
#    print(result)
#elif operator == "-":
#    result = num1 - num2
#    print(result)
#elif operator == "*":
#    result = num1 * num2
#    print(result)
#elif operator == "/":
#    result = num1 / num2
#    print(result)
#else:
#    print(f"{operator} is not a valid operator")


#name = input("Enter your name: ")
#con = name.isalpha()
#if con:
#    print(f"welcome {name}")
#else:
#    print(f"your {name} contains numbers or space, kindly try again")
# Math (arithemetic operators)
#friends = 58
# addition
#friends += 1
# subtraction
#friends -= 1
#multiplication
#friends *= 2
#division
#friends /= 2
# raise to power
#friends **= 2

#print(friends)

# modulous (this will givue you any remainder)
#friends = 10
#remainder = friends % 3

#print(remainder)

#x = 3.14
#y = 4
#z = 5

#result = round(x)
#result =abs(y)
#result = pow(y, 3)
#result = max(x, y, z)
#result = min(x, y, z)



#print(result)

#import math
#print(math.pi)
#print(math.e)
#x = 9.1
#result = math.sqrt(x)
#result = math.ceil(x)
#result = math.floor(x)

#print(result)

#calculating the circumfrence of a circle
#(c = 2 math.pi r)
#import math
#radius = float(input("Enter the radius: "))
#cir = 2 * math.pi * radius

#print(f"Your circumfrence is {round(cir, 2)}")

#teseting python quiz game
#questions = ("How many elements are in the periodical table?: ",
#            "Which animals lays the largest egg?: ",
#            "What is the most abudant gas in the earth's atmosphere?: ",
#            "How many bones are in the human body?: ",
#            "which planet in the solar system is the hottest?: ")
#options = (("A. 116", "B.117", "C.118", "D.119"),
#           ("A. Whale", "B. crocodile", "C. Elephant", "D. Ostrich"),
#           ("A. Nitrogen", "B. Oxygen", "C. Carbon-dioxide", "D. Hydrogen"),
#           ("A. 206", "B. 207", "C. 208", "D. 209"),
#           ("A. Mecury", "B. Venus", "c. Earth", "D. Mars"))

#answers = ("C", "D", "A", "A", "B")
#guesses = []
#score = 0
#question_num = 0

#for question in questions:
#    print("---------------")
#    print(question)
#    for option in options[question_num]:
#        print(option)
#    guess = input("Enter (A, B, C, D): ").upper()
#    guesses.append(guess)
#    if guess == answers[question_num]:
#        score += 1
#        print("CORRECT!!!")
#    else:
#        print("INCORRECT!!!")
#        print(f"answer {answers[question_num]} is the correct answer")

#    question_num += 1

#print("---------------")
#print("-----RESULT----")
#print("---------------")

#print("answers:", end="")
#for answer in answers:
#    print(answer, end=" ")
#print()


# print("guesses:", end="")
# for guess in guesses:
#    print(guess, end=" ")
# print()
# score = (score / len(questions) * 100)
# print(f"Your score is: {score}% ")
# import time
# print("set a count down timer")


# def count(start, end):
#    for x in range(start, end+1):
#        print(x)
#        time.sleep(1)
#    print("Done!")
# count(start = int(input("start time: ")),end = int(input("end time: ")))
#  print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518" )
#import random
# ● ┌ ─ ┐ │ └ ┘

#dice_art = {
#    1: ("┌─────────┐",
#        "│         │",
#        "│    ●    │",
#        "│         │",
#        "└─────────┘"),
#    2: ("┌─────────┐",
#        "│  ●      │",
#        "│         │",
#        "│      ●  │",
#        "└─────────┘"),
#    3: ("┌─────────┐",
#        "│  ●      │",
#        "│    ●    │",
#        "│      ●  │",
#        "└─────────┘"),
#    4: ("┌─────────┐",
#        "│  ●   ●  │",
#        "│         │",
#        "│  ●   ●  │",
#        "└─────────┘"),
#    5: ("┌─────────┐",
#        "│  ●   ●  │",
#        "│    ●    │",
#        "│  ●   ●  │",
#        "└─────────┘"),
#    6: ("┌─────────┐",
#        "│  ●   ●  │",
#        "│  ●   ●  │",
#        "│  ●   ●  │",
#        "└─────────┘"),
#}

#dice = []
#total = 0
#num_dice = int(input("How many dice?: "))

#for die in range(num_dice):
#    dice.append(random.randint(1,6))

#for line in range(5):
#    for die in dice:
#        print(dice_art.get(die)[line], end="")
#    print()

#for die in dice:
#    total += die
#print(f"total: {total}")


# principle = 0
#rate = 0
#time = 0

# while True:
# principle = float(input(enter the principle amount: ))
 #   if principle <= 0:
#        print("you can`t enter a number less than zero")
#    else:
 #       break
#while True:
    #rate = float(input("enter the intrest rate: "))
    #if rate <= 0:
    #    print("you can`t enter a number less than zero")
   # else:
  #      break
# while True:
    # time = int(input("enter the time in years: "))
    #    print("you can`t enter a number less than zero")
   # else:
  #      break

# total = principle * pow((1 + rate / 100), time)
#print(f"Balance after {time} years/s: ${total:.2f}")

# for f in range(1, 11):
#    if f == 5:
##       break
#   print(f)
# first_name = input(first name)
#last_name = input( ""enter your last name (surname): ")
# while len(first_name) >= 10 or not first_name.isalpha():
   # print(" invalid name")
  #  first_name = input("Reenter your first name: ")


# while len(last_name) >= 10 or not last_name.isalpha():
   # print(" invalid name")
  #  last_name = input("enter your last name (surname): ")


# print(f"welcome {last_name} {first_name}")
# credit_card = "123-456-789"

# import time

# my_time =  int(input(""enter the time in seconds: "))

# for x in range(my_time, 0, -1):
#    seconds = x % 60
  #  minutes = int(x / 60) % 60
 #   hours = int(x / 3600)
   # print(f"{hours:02}:{minutes:02}:{seconds:02} ")
  #  time.sleep(1)
#import time
#import datetime
#import pygame
#def set_alarm(alarm_time):
#    print(f"alarm set for {alarm_time}")
#    sound_file = "my_music.mp3"
#    is_running = True

#    while is_running:
#        current_time = datetime.datetime.now().strftime("%H:%M:%S")
#        print(current_time)
#        if current_time == alarm_time:
#            print("Wake up!")

#            pygame.mixer.init()
#            pygame.mixer.music.load(sound_file)
#            pygame.mixer.music.play()

#            while pygame.mixer.music.get_busy():
#                time.sleep(1)
#            is_running = False

#        time.sleep(1)

#if __name__ == "__main__":
#    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
#    set_alarm(alarm_time)
#def favourite_food(food):
#    print(f"Your favourite food is {food}")

#def main():
#    print("This is script1")
#    favourite_food("pizza")
#    print("Goodbye!")

#if __name__ == '__main__':
#    main()

#def favourite_drink(drink):
#    print(f"you favourite drink is {drink}")

#def main():
#    print("This is script2")
#    favourite_food("sushi")
#    favourite_drink("coffee")
#    print("Goodbye")

#if __name__ == '__main__':
#    main()