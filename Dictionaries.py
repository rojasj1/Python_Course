print("A little demonstration on using dictionaries")

person= {"name":"John Doe","gender":"male","age":29,"address": "1234 SuperMario Dr","phone": 18004356642}

user_input = input("What would you like to know about this person?: ").lower()

print(person.get(user_input,"data not found"))
