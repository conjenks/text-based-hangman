from random import randint

print("Welcome to Hangman! Can you guess all of the letters in the word?")

with open('words/animals') as a:  #  create the pool of words to be randomly chosen from, and split it up into categories
    animal_list = a.read().splitlines()
with open ('words/jobs') as b:
    jobs_list = b.read().splitlines()
with open('words/clothes') as c:
    clothes_list = c.read().splitlines()
with open('words/countries') as d:
    countries_list = d.read().splitlines()
with open('words/food_drink') as e:
    food_drink_list = e.read().splitlines()

categories = [animal_list, jobs_list, clothes_list, countries_list, food_drink_list]
category_names = ["Animals", "Jobs", "Clothes", "Countries", "Food & Drink"]  #  create a list of categories and a corresponding
                                                                               #  list of category names

print("Please select a difficulty:")
print("Easy (1)  Medium (2)  Hard (3)")
diff = int(input(""))

assert diff in [1, 2, 3]
print()

difficulties = {1: "Easy", 2: "Medium", 3: "Hard"}
print("Difficulty: %s" %difficulties[diff])


c = randint(0,4)
cat_name = category_names[c]
category = categories[c]

print("Your category is %s." %cat_name)
print("You are allowed to guess SIX wrong letters.")


def select_word(category, diff):  #  easy is less than 6 letters, medium is 6 letters to 8 letters, hard is 9 letters or more
    if diff == 1:
        words = [word for word in category if len(word) < 6]
    elif diff == 2:
        words = [word for word in category if len(word) > 5 and len(word) < 9]
    elif diff == 3:
        words = [word for word in category if len(word) > 8]
    word = words[randint(0,len(words)-1)]
    return word

print()

word = select_word(category, diff)
word = word.upper()

def game(word):
    guesses = 0
    working_word = "-"*len(word)
    guessed_letters = ""
    while guesses < 7:
        print(working_word)
        i = 6 - guesses
        print("You have %s wrong guess(es) left." %i)
        guess = input("Guess a letter: ")
        print()
        guess = guess.upper()
        assert len(guess) == 1
        if guess in word:
            for i, char in enumerate(word):
                if char == guess:
                    working_word = [char for char in working_word] # convert to list to support item assignment
                    working_word[i] = char                           # in next line
                    working_word = ''.join(working_word)
            print("Got one!")
            print(working_word)
        else:
            print("Nope!")
            guesses += 1
        if working_word == word:
            break
        print("______________________________________")
        print()
        guessed_letters = guessed_letters + ("%s " %guess)
        print("The letters you have guessed are:")
        print(guessed_letters)
        print()
    if working_word == word:
        print("You win!")
    else:
        print("You lose!")
        print(word)

game(word)











