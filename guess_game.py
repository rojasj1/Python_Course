print("Understand while loops though a guess game")
import random

number = random.randint(0,10)
guess = int(input("I'm thinking about a number Between 0 and 10. Can you guess it?: "))

while True:
      if guess == number:    
         break
      else:
         guess = int( input("Nope! Please try again: "))

print("Correct! I was thinking about the number : ",number)


