introstring=input("enter string :")
#print(introstring)
charCount=0
wordCount=1
for char in introstring:
    charCount=charCount+1
    #print(charCount)
    if (char == " "):
        wordCount=wordCount+1
print("number of words in the string:")
print(wordCount)
print("number of characters in the string:")
print(charCount)