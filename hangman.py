import os, random

def word_pool():
    categories = []
    os.chdir('words')
    for file in os.listdir('.'):
        with open(file) as f:
            category = []
            words = f.read().splitlines()
            for word in words:
                category.append(word)
            categories.append(category)
    return categories

def select_category():
    categories = word_pool()
    category_names = ["Animals", "Clothes", "Countries", "Food & Drink", "Jobs"]
    i = random.randint(0,4)
    category = categories[i]
    cat_name = category_names[i]
    return category, cat_name

def select_difficulty():
    difficulties = {
        1:"Easy",
        2:"Medium",
        3:"Hard"
    }
    while True:
        try:
            diff = int(input(""))
            if diff in [1, 2, 3]:
                diff_string = difficulties[diff]
                return diff, diff_string
        except:
            continue

def select_word(category, diff):  #Easy is less than 6 letters; medium is 6 letters to 8 letters; hard is 9 letters or more.
    if diff == 1:
        choices = [word for word in category if len(word) < 6]
    elif diff == 2:
        choices = [word for word in category if len(word) > 5 and len(word) < 9]
    elif diff == 3:
        choices = [word for word in category if len(word) > 8]
    word = random.choice(choices).upper()
    return word

def get_guess():
    while True:
        guess = input("\n")
        guess = guess.upper()
        if guess in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return guess
        else:
            print("That is not a valid guess. Please choose again.")
            continue

def check_guess(guess, guessed_letters):
    if guess in guessed_letters:
        return False
    else:
        guessed_letters = guessed_letters + "%s " %guess
        return guessed_letters

def update_word(word, working_word, guess):
    for i, char in enumerate(word):
        if char == guess:
            working_word = [char for char in working_word] #Convert to list to support item assignment
            working_word[i] = char                         #in next line
            working_word = ''.join(working_word)
    return working_word

def game(word):
    guesses_left = 6
    guessed_letters = ""
    working_word = "-"*len(word)
    print(working_word)
    while guesses_left > 0:
        print("Guess a letter:")
        guess = get_guess()
        if check_guess(guess, guessed_letters) == False:
            print("You already guessed that!")
            continue
        else:
            guessed_letters = check_guess(guess, guessed_letters)
        if guess not in word:
            print("Wrong!")
            guesses_left -= 1
            print("You have %s wrong guess(es) left." %guesses_left)
            if guesses_left == 0:
                break
        else:
            print("Got one!")
            working_word = update_word(word, working_word, guess)
            if working_word == word:
                break
        print(working_word)
        print("So far, you have guessed: \n", guessed_letters)
    return working_word

def main():
    print("Welcome to Hangman! Can you guess all of the letters in the word? \n")
    category, cat_name = select_category()
    print("Your category is %s. \n" %cat_name)
    print("Please select a difficulty:")
    print("Easy (1)  Medium (2)  Hard (3)")
    diff, diff_string = select_difficulty()
    print("Difficulty: %s \n" %diff_string)
    word = select_word(category, diff)
    final_word = game(word)
    if final_word == word:
        print(final_word)
        print("You won!")
    else:
        print("You lose!")
        print("The word was %s." %word)
    print()
    input("Press Enter to exit.")

if __name__ == '__main__':
    main()











