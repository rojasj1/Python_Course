print("A program that prints random colors")

import random

colors= ["red","green","blue","black","white","orange"]

while True:
     color = colors[random.randint(0,len(colors)-1)]
     guess = input("Im thinking about a color. Guess which is it?: ")

     while True:
         if (color==guess.lower()):
             break
         else:
           guess = input("Nope.Try Again!: ")

     print("Correct! The color I was thinking about was: ",color)


     play_again = input("Lets play again? Type 'no' to quit.")

     if play_again.lower() == 'no':
        break

print("It was fun! thanks for playing!")
