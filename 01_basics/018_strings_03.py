topic ="String Methods. Strings are immutable."
sample = "!!!!!!%%%%%%!!!!!!!$$$$$$$^^^^^^^^@!!!!!!!*******!!!!!!!&&&&&&&&!!!!!!!"
low_case_sent = "the quick Brown fOx"
# Strings are immutable. i.e. String Methods another copy. Do not make changes in the Original.

print(topic)
print(topic.upper()) # Converts all characters to Upper Case
print(topic.lower()) # Converts all the characters to the Lower Case.
print(sample.rstrip("!")) # Remove one trail of the match from right.
print(sample.lstrip("!")) # Remove one trail for one match from left.
print(topic.replace("Methods", "Data")) # Replaces each same word or sentences with the other.
print(topic.split(" ")) # The thing used inside quotes is used to separate and consider as different elements. It is used to make lists.
print(low_case_sent.capitalize()) # Sentence Capitalization.
print(topic.center(50)) # Add the specified nos. of spaces to the front to keep sentence in the middle.
print(topic.count("e")) # Check for the exact count of the word/characters match.
print(topic.startswith("String")) # Checks if the variable value starts with the match or not.
print(topic.endswith("immutable.")) # Checks if the variable value ends with the match or not.
print(topic.endswith("met", 4,18)) # Checks if the variable value contain the match between the given indexes.
print(topic.find("met")) # Finds the match and then returns the indexes. Returns -1 if not found.
print(topic.isalnum()) # Check if it only contains alpha numeric values. Returns False if contains punctuations and signs.
print(topic.isalpha()) # Check if it only contains alpha values. Returns False if contains numbers, punctuations and signs.
print(topic.isnumeric()) # Check if it only contains numeric values. Returns False if contains numbers, punctuations and signs.
print(topic.islower()) # Check if it only contains text in lower case.
print(topic.isupper()) # Check if it only contains text in upper case.
print(topic.isprintable()) # Check if string are printable or not. If not, return False. Non printable values like \n.
print(topic.isspace()) # Check if string contains whitespaces or not. The space may be of Space bar or Tab.
print(topic.title()) # Capitalized the string's each word.
print(topic.istitle()) # Check if string's each word is capitalized or not.
print(topic.swapcase()) # Converts Lower Case to Upper Case and Upper Case to Lower Case.

