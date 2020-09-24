# Import our conversion table first
from conversionTable import conversionTable

# Import the file we are reading. In this case I created a dummy file
file = open("scratch.txt")

# Then we read the file which converts the file into a string
string = file.read()

# We are going to store the compression in this string
bitString = ""

# We are going to iterate over the string, find the character and concatenate it to bitString
i = 0
while i < len(string):
    #Inside the while loop we are going to have to check three cases
    #If the current three characters are inside our compression table
    #If the current three characters aren't, then we need to check the first two characters
    #If neither case applies than we will just have to represent the first character
    #To access the current character you would type: string[i]
    #For the first two, string[i]+string[i+1], same trend for the third
    #To check if a character combination is in the table use the statement: (insert character you are looking for) in conversionTable
    #Make sure to increment i by how many ever characters you were able to represent
    #Also add the binary value to the bitString

print(bitString)



