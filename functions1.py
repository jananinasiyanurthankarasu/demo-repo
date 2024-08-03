phrase="Giraffe Academy"
#convert to upper and check whether it is upper or not - combining 2 functions
print(phrase.upper().isupper())
#To find out length of the string
print(len(phrase))
#To find out location of the string
print(phrase[0])
print(phrase[4])
#passing a parameter
print(phrase.index("G"))
print(phrase.index("a"))
#passing parameter - using more that 1 character - It will give the start of the string
print(phrase.index("Acad"))
#using replace function
print(phrase.replace("Giraffe" , "Elephant"))