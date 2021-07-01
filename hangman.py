from words import words
import random
word=random.choice(words)
attempts= len(word)
print(f"You have {2*attempts} number of attempts to guess the word.")
print("word=", attempts*"_ ")


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
                
hangman()
            
#while 2*attempts==True:
#    hangman()

        