
from conversion_table import conversionTable

file = open('./testing/bits_to_text.txt')

bitString = file.read()

# Create an empty string to store our final output
string = ""

# Set pointer to index 0
i = 0
while(i < len(bitString)):
    # Checking if the character is short
    if(bitString[i] == '0'):
        # Store the short bit character in a variable
        lookup_value = bitString[i]+bitString[i+1]+bitString[i+2]+bitString[i+3]
        # Find the resulting key for the bit value
        for key, value in conversionTable.items():
            if(value == lookup_value):
                string += key
        # Move the pointer over by the length of the variable, short -> 4 bits
        i += 4
    # If it isn't a short character, than it must be a long character
    else:
        # Access the first seven bits
        lookup_value = bitString[i]+bitString[i+1]+bitString[i+2]+bitString[i+3]+bitString[i+4]+bitString[i+5]+bitString[i+6]
        for key, value in conversionTable.items():
            if(value == lookup_value):
                string += key
        # Move the pointer over by the length of the character, long -> 7 bits
        i += 7
# Prints out the final string output
print(string)


