import random

word_list = ["apple", "banana", "kiwi", "strawberry", "peach"]
print (word_list)

word = random.choice(word_list)
print (word)

print ('Enter a single letter: ')
guess = input()

while True:
    guess = input("Enter a single letter: ")
    if len(guess) == 1:
        print(f'Good guess!')
        break
    if guess.isalpha == True:
        print(f'Good guess!')
        break
    print("Oops! That is not a valid input.\n")
