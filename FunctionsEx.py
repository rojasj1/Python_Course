def say_hello(person1="Mary", person2 = "the director"):
              print("Hello! "+person1+ ", how are you doing? "+person2+ " is waiting for you")

def fahr2celsius(fahr):
              celsius =  (5 * (fahr - 32)) / 9
              return celsius

say_hello()

print ("Celsius: ", round(fahr2celsius(100),2))
print ("Kelvin: ", round(fahr2celsius(100),2)+273.5)
              
