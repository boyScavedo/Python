# Strings are immutable
a = "jeevan!!!!!!!"
print(len(a))  # Gives the length of the string
print(a.upper())  # Changes the text into UPPERCASE
print(a.lower())  # Changes the text into lowercase
print(a.rstrip("!"))  # Removes the given characters at the end of the string.
print(a.replace("!!!!!!!", " adhikari"))  # Replaces the given string into some other string
print(a.split("ev"))  # Splits the string into list with the given seperator
print(a.capitalize())  # Capitalizes the first letter
print(len(a.center(50)))  # Create whitespaces at the start and end of the string to make it the given length.
print(a.count("!"))  # Counts the amount of occurrence of the given string
print(a.endswith("!!!!!!!"))  # Checks if the string ends with the given string
print(a.endswith("n", 0, 6))  # Checks if the string is the end in the given slice of string
print(a.find("v"))  # Finds the index of the string giver, prints -1  if not found
print(a.isalnum())  # Checks if the text is alphanumerical
print(a.isalpha())  # Checks if the text is alphabetical
print(a.islower())  # Checks if the text is lowercase
print(a.isupper())  # Checks if the text is uppercase
print(a.isprintable())  # Checks if the text is printable
print(a.isspace())  # Checks if the text has whitespace
print(a.istitle())  # Checks if the text is capitalized
print(a.startswith("J"))  # Checks if the text starts with given string
print(a.swapcase())  # Converts lower to UPPER and UPPER to lower
print(a.title())  # Converts every first character of each word into UPPERCASE