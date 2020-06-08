print("Experimenting with modules")

import time as t
import matplotlib.pyplot as plt

times = []
mistakes = 0

print("This program is designed to help you type faster.You will have too type the word 'communication' as fast as you can for 5 times")
input("Press enter to continue.")

while len(times) < 5:
              start= t.time()
              word = input("Type the word: ")
              end = t.time()
              time_elapsed = end - start

              times.append(time_elapsed)

              if (word.lower() != "communication"):
                            mistakes += 1

print("You made "+str(mistakes)  + " mistake(s).")
print("Now let's see your evolution")
t.sleep(3)

x = [1,2,3,4,5]
y = times
plt.plot(x,y)

legend = ["1","2","3","4","5"]
plt.xticks(x,legend)
plt.ylabel('Time in seconds')
plt.xlabel('Attempts')
plt.title('Your typing evolution')


plt.show()

