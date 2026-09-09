#this is actually challenge 25 but challenge 24 was done inside of 23 because they were related to eachother 
import random
randomNumber = random.randint(1,5)
guess = int(input("Guess a random number 1-5: "))
if (guess == randomNumber):
    print("You guessed correctly!")
else:
    if (guess < randomNumber):
     guess2 = int(input ("The number is higher: "))
    else:
     guess2 = int(input("The number is lower: ")) 
if (guess2 == randomNumber):
   print("You guessed correctly!")
else: 
   if (guess2 < randomNumber): 
     guess3 = int(input("The number is higher: "))
   else: 
      guess3 = int(input("The number is lower: "))
if (guess3 == randomNumber):
   print("You guessed correctly!")
else: 
   if (guess3 < randomNumber):
      print("Your really bad at this...The number was " + randomNumber)
   else: 
      print("Your really bad at this...the number was " + randomNumber)