from milestone_2.py import word
from milestone_2.py import guess

check_guess = (guess)
guess.lower()

while True:
    word = random.choice(word_list)
    if guess.lower() in (word):
       print (f"Good guess! {guess} is in the word.")
    elif (guess) not in (word):
       print (f"Sorry, {guess} is not in the word. Try again.")
    break

ask_for_input = (guess)

while True:
    guess = input("Enter a single letter: ")
    if guess.isalpha():
        print(f'Good guess!')
        break
    print("Invalid letter. Please enter a single alphabetical character.\n")
    check_guess()
