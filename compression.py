# Import our conversion table first
from conversion_table import conversionTable

# Import the file we are reading. In this case I created a dummy file
file = open("./testing/text_to_bits.txt")

# Then we read the file which converts the file into a string
string = file.read()

# We are going to store the compression in this string
bitString = ""

# We are going to iterate over the string, find the character and concatenate it to bitString
i = 0
while i < len(string):
    #Check to see if there is three characters or more and see if the current three character combination is in the conversionTable
    if(len(string) - i > 2 and string[i]+string[i+1]+string[i+2] in conversionTable):
        #If true, add the binary compression to the bitString and increment by 3
        bitString += conversionTable[string[i]+string[i+1]+string[i+2]]
        i += 3
    #Check if there is two characters and if the current two letter combination is in the conversionTable
    elif(len(string) - i > 1 and string[i]+string[i+1] in conversionTable):
        bitString += conversionTable[string[i]+string[i+1]]
        i += 2
    #If all else fails, just use the single character binary compression
    else:
        bitString += conversionTable[string[i]]
        i += 1

print(str(len(bitString))+'.'+bitString)



