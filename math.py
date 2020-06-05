print("Calculating the area and circumfrence")
       
import math
radius = float(input("Please enter the radius of the circle: "))

area = math.pi * (radius ** 2) 
circumfrence = 2 * math.pi * radius

print("The area of the circle is : " ,round(area,2))
print("The circumfrence of the circle is : " ,round(circumfrence,2))     
