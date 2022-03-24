

def robber_encode(word):

    # the list of vowels provided in the exam set
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    # two temporarily variables to store the word and strings
    tempStrArray = []

    # looping through each letter in the provided 'word' parameter
    for w in word:
        # checking if any word is a vowel, if it is - we do nothing other than adding it to the list
        if w in vowels:
            tempWord = w
            tempStrArray.append(tempWord)
        else:
            # if it is not, we add the double letter and o in between
            tempWord = w
            tempWord += 'o'
            tempWord += w
            tempStrArray.append(tempWord)

    wordEncode = ""

    for words in tempStrArray:
        if words == tempStrArray[len(tempStrArray) - 1]:
            wordEncode += words
        else:
            wordEncode += words + "-"

    return wordEncode

print(robber_encode("muggle"))

def robber_decode(wordEncode):

    wordDecode = ""

    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    word = wordEncode.split("-")

    for w in word:
        if w in vowels:
            wordDecode += w
            continue
        size = len(w)
        wordDecode += w[:size - 2]

    return wordDecode

print(robber_decode(robber_encode("muggle")))

def code_shift(code, shift):

    # if code is a negative integer, the program will exit
    if code < 0:
        print("Error: code must be a positive integer.")
        exit(0)

    digits = []
    digitsStr = ""

    # adding 0 as the start element since the length is less than 4
    if len(str(code)) < 4:
        digits.append(0)

    # looping through the integer 'code' and adding individual digits as an int
    for number in str(code):
        digits.append(int(number))

    for digit in digits:
        # checking if the value sum is over 9
        if digit + shift > 9:
            digitsStr += str((digit + shift) - (9 + 1))
        # if not, we just find the sum normally
        else:
            digitsStr += str(digit + shift)

    newCode = int(digitsStr)
    return newCode


print(code_shift(2638, 3))