"""
The goal of your quiz is to create a function called posSentCounter that passes in a
string and returns the number of words that show up in the positive sentiments text
file your professor has provided for your project.

Your function should:
1.) Read in the text file Positive Sentiments.
2.) Cycle through the words in the string argument and check if they are in the
    positive sentiment text file.
3.) If they are in the text file, your function should add one to a counter.
4.) Your function should return the count of the positive sentiments.
"""

def posSentCounter(string):
    posSentenceCounter = 0
    negSentenceCounter = 0
    neutSentenceCounter = 0

    sentences = []
    words = []
    # Open and allow use of the Positive Sentiments file.
    filename = 'NegativeSentimentWords.txt'
    f = open(filename, 'r')
    text = f.read()
    # for modifying the positive words file into a list
    negativeList = text.split('\n')
    #negativeList.pop()  # to remove the empty character at the end of the list

    # Open and allow use of the Positive Sentiments file.
    filename1 = 'PositiveSentimentWords.txt'
    f1 = open(filename1, 'r')
    text = f1.read()
    # for modifying the positive words file into a list
    positiveList = text.split('\n')
    #positiveList.pop()  # to remove the empty character at the end of the list

    # remove all punctuations except for end of sentence things.
    string = string.lower()
    string = string.replace(';', ' ')
    string = string.replace(':', ' ')
    string = string.replace('(', ' ')
    string = string.replace(')', ' ')
    string = string.replace('[', ' ')
    string = string.replace(']', ' ')
    string = string.replace("\n", ' ')
    string = string.replace(', ', ' ')
    string = string.replace('"', ' ')
    string = string.replace("'s", ' ')
    string = string.replace("'", ' ')
    string = string.replace("? ", '. ')
    string = string.replace("! ", '. ')
    string = string.replace("... ", '. ')
    string = string.replace("mr.", 'mr')
    string = string.replace("mrs.", 'mrs')
    string = string.replace("ms.", 'ms')
    string = string.replace("dr.", 'dr')
    sentences = string.split(". ")

    for i in range(0, len(sentences)):
        if '' in sentences:
            sentences.remove('')
        if ' ' in sentences:
            sentences.remove(' ')

    for i in range(0, len(sentences)):
        #print(sentences[i])
        words = sentences[i].split(' ')
        posWordCounter = 0
        negWordCounter = 0
        if '' in words:
            words.remove('')
        for element1 in words:
            for element2 in positiveList:
                if element2 == element1:
                    posWordCounter += 1  # if equal then add one to counter.
            for element3 in negativeList:
                if element3 == element1:
                    negWordCounter += 1  # if equal then add one to counter.

        if posWordCounter == negWordCounter:
            neutSentenceCounter += 1
        elif posWordCounter < negWordCounter:
            negSentenceCounter += 1
        elif posWordCounter > negWordCounter:
            posSentenceCounter += 1

    print("Positive Sentences: %i \nNegative Sentences: %i \nNeutral Sentences: %i" % (posSentenceCounter, negSentenceCounter, neutSentenceCounter))
    print("Total Sentences: %i" % (posSentenceCounter+negSentenceCounter+neutSentenceCounter))


def main():

    filename1 = 'The Hound of the Baskervilles.txt'
    f1 = open(filename1, 'r')
    str2 = f1.read()  #The text file for the hound of the baskervilles # EXTRA CREDIT

    posSentCounter(str2)


main()

