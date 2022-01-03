"""
Write two functions that perform a 'Caesar Cipher' on a string.
A string and an integer are entered into the function called encryption(S, n)
The string that is entered into the function must contain lowercase letters or spaces.
The integer can be negative or positive. encryption(S, n) will shift every character in
the string over to the right by the amount of n. If n is a negative value then the cipher
will shift characters to the left. The shifting is done in a circular fashion. a -> z and
then the rest of the alphabet. Then a new string is printed out. Also the cipher key is
attached at the end of the new string. This allows for decoding the encrypted file with
a little more ease.
"""

def encryption(S, n):
    T = ""                      # T is the given variable for the scrambled string
    m = n % 26                  # this is if n is greater than 26 it will obtain the remainder
                                # and then shift by that many characters.
                                # m is used since the original number must be printed in the new string
    for element in S:           # this for loop helps make the new string or T
        if ord(element) + m > 122:              # ord is used to obtain the ASCII values for each character
            T = T + chr(ord(element) + m - 26)           # chr is used to convert back from the ASCII value
        elif (ord(element) <= 122) & (ord(element) >= 97):    # these checks are done with the ASCII values
            T = T + chr(ord(element) + m)
        elif element == " ":
            T = T + " "
    print("%s%i" % (T, n))               # this prints out the new string and the key for the cipher


"""
decryption(W) is used to take in a scrambled string that contains a cipher key at the end and then revert 
it back to the original phrase. It also works for both positive and negative values. It uses two for loops:
one to find the value of the cipher and then another to unscramble the string. Various types of casting was 
used to check vor various things. ord() was primarily used to convert characters and numbers into their ASCII
values. If the characters were found to be integers in the string then they would be cast into an integer.
str() was used to find the amount of digits were in the number value of n. This allowed for an efficient manner
of making and printing out the original phrase.  
"""

def decryption(W):
    a = ""                       # a is used as a place holder. It is to hold the numbers as they are in string.
    for i in range(0, len(W)):
        if ((ord(W[i]) <= 57) & (ord(W[i]) >= 48)) or ord(W[i]) == 45:          # obtains the number value of n.
            a = a + W[i]                                                        # this pieces the digits together.

    n = int(a)                                           # the digits are then cast to integer values
    m = n % 26                                           # m is then given the value of the remainder n % 26
    word = ""                                            # word is used to form the original string

    for element in W:
        if element == ' ':                               # finds spaces in W and then adds that to word
            word = word + ' '
        elif ord(element) - m < 97:                      # converts to ASCII then allows for circular un-shifting.
            word = word + chr(ord(element) - m + 26)
        elif (ord(element) <= 122) & (ord(element) >= 97):
            word = word + chr(ord(element) - m)     # converts to ASCII for checks then back to char and makes word

    r = len(str(n))         # this converts the number into a string and finds the amount of digits.
    word2 = word[:-r]       # forms the original message and removes the number from the end of the string.
    print("%s" % word2)     # prints the original string.


"""
The next few lines prompt the user to enter a string and a number to scramble the code. 
Then encryption will take them in an input and then provide the message. 
Since the decryption function is made to decrypt any string with this type of cipher, 
the user is prompted to enter in a string that he/she would like to decrypt. 
Finally decryption will run and it will print out the original string. 
"""
S = input("Enter a message in all lowercase letters: ")
n = int(input("Enter a number used to scramble the given message: "))
encryption(S, n)

W = input("Enter an encrypted string and a number at the end used to decrypt the message: ")
decryption(W)

