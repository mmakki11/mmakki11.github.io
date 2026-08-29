# Source: index.html link "Caesar Cipher example" (pythontutor.com)
#Predict what will be printed:

for c in range(65,90):
    print(chr(c))
    
message = "I love Python"
newMessage = ""
for c in message:
    print(ord(c))   #Print the Unicode of each number
    print(chr(ord(c)+1))    #Print the next character
    newMessage = newMessage + chr(ord(c)+1) #add to the new message
print("The coded message is", newMessage)

word = "zebra"
codedWord = ""
for ch in word:
    offset = ord(ch) - ord('a') + 1 #how many letters past 'a'
    wrap = offset % 26  #if larger than 26, wrap back to 0
    newChar = chr(ord('a') + wrap)  #compute the new letter
    print(wrap, chr(ord('a') + wrap))    #print the wrap & new letter
    codedWord = codedWord + newChar #add the newChar to the coded word
    
print("The coded word (with wrap) is", codedWord)
