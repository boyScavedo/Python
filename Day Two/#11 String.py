name = "Jeevan"
friend = "Rohit"
another_friend = "Bogies"
apple = '''He said,
Hi Jeevan
hey I'm good
\"I want to eat an apple\"'''

print("Yo,", name)
# print(apple)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
# print(name[6])  # Throws an error since there is nothing in index 6
print("\nThis is a buffer text before the loop \n")
for character in apple:
    print(character)
