print("Understanding for-loops")


blog_posts = ["","The 10 coolest math functions in Python", "","How to Make HTTP requests in Python","A tutorial about data types"]

for post in blog_posts:
    if post == "":
       continue
    else:
        print(post)

print('------------------------------------------------------------------')       
myString = "This is a String"

for char in myString:
      print(char)
      
print('------------------------------------------------------------------')

for x in range(0,10):
      print(x)
      
print('------------------------------------------------------------------')

person={'Name':'Nicole Suarez', 'Age':27,'Gender':'Female'}

for key in person:
  print(key,":",person[key])

print('------------------------------------------------------------------')

blog_posts = {"Python":["The 10 coolest math functions in Python","How to Make HTTP requests in Python","A tutorial about data types"],"Javascript": ["Namespaces in javascript", "New Functions in javascript"]}

for catagory in blog_posts:
  print("Posts about",catagory)
  for post in blog_posts[catagory]:
      print(post)          
                




