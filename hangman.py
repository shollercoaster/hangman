import random

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open("words.txt", 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def hangman():
    for j in range (0, 2*attempts):
        guess=input("enter the alphabet you wish to guess: ")
        for i in word:
            if i==guess:
                print("you guessed correctly.")
                for iter in word[:]:
                    if iter==i:
                        print(i)
                    else:
                        print("_ ")
            else:
                pass
                print("incorrect guess! You're already losing hehe.")
                hangman()
                
word = random.choice(load_words())
attempts= len(word)
print(f"You have {2*attempts} number of attempts to guess the word.")
print("word=", attempts*"_ ")
hangman()