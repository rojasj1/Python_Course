f = open("Some_text2.txt","x")
f.write("\n\A Different file altogether")

f = open("Some_text2.txt")
print(f.read())
 
