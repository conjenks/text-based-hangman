__author__ = 'Connor'
from random import randint

print("Welcome to Hangman! Can you guess all of the letters in the word?")

with open('animals') as a:  #  create the pool of words to be randomly chosen from, and split it up into categories
    animal_list = a.read().splitlines()
with open ('jobs') as b:
    jobs_list = b.read().splitlines()
with open('clothes') as c:
    clothes_list = c.read().splitlines()
with open('countries') as d:
    countries_list = d.read().splitlines()
with open('food_drink') as e:
    food_drink_list = e.read().splitlines()

categories = [animal_list, jobs_list, clothes_list, countries_list, food_drink_list]
category_names = ["Animals", "Jobs", "Clothes", "Countries", "Food & Drink"]  #  create a list of categories and a corresponding
                                                                                #  list of category names

print("Please select a difficulty:")  # difficulty selection
print("Easy (1)  Medium (2)  Hard (3)")
diff = int(input(""))

assert diff in [1, 2, 3]  # check to see the difficulty input is valid
print()

difficulties = {1: "Easy", 2: "Medium", 3: "Hard"}  #  print the difficulty
print("Difficulty: %s" %difficulties[diff])

categ = randint(0,4)
cat_name = category_names[categ]  #  create the category name string variable
categ = categories[categ]  #  select the category

print("Your category is %s." %cat_name)  #  print the category
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

word = select_word(categ, diff)  #  choose the word

def game(word):
    guesses = 0
    working_word = "-"*len(word)
    print(working_word)

game(word)











