import json

def change_name():
    newName = input("What do you want to change your name to?   ")
    answers['name'] = newName
def change_age():
    newAge = input("What do you want to change your age to? ")
    answers['age'] = newAge
def change_hometown():
    newHometown = input("What do you want to change your hometown to?   ")
    answers['hometown'] = newHometown

def change_birthday():
    newBirthday = input("What do you want to change your birthday to?   ")
    answers['DOB'] = newBirthday

def change_pet():
    newPet = input("What do you want to change your pet to? ")
    answers['pet'] = newPet

def change_color():
    newColor = input("What do you want to change your color to? ")
    answers['color'] = newColor

def change_siblings():
    newSiblings = input("What do you want to change your siblings to?   ")
    answers['siblings'] = newSiblings

def change_genre():
    newGenre = input("What do you want to change your genre to?   ")
    answers['genre'] = newGenre

def change_artist():
    newArtist = input("What do you want to change your music artist to?   ")
    answers['artist'] = newArtist

def printAllLists():
    categories_list = []
    names = []
    for s in range(len(list_of_answers)):
        names.append(list_of_answers[s]["name"])
    categories_list.append(names)

    ages = []
    for s in range(len(list_of_answers)):
        ages.append(list_of_answers[s]["age"])
    categories_list.append(ages)

    hometowns = []
    for s in range(len(list_of_answers)):
        hometowns.append(list_of_answers[s]["hometown"])
    categories_list.append(hometowns)

    birthdays = []
    for s in range(len(list_of_answers)):
        birthdays.append(list_of_answers[s]["DOB"])
    categories_list.append(birthdays)

    pets = []
    for s in range(len(list_of_answers)):
        pets.append(list_of_answers[s]["pet"])
    categories_list.append(pets)

    colors = []
    for s in range(len(list_of_answers)):
        colors.append(list_of_answers[s]["color"])
    categories_list.append(hometowns)

    siblingsCounts = []
    for s in range(len(list_of_answers)):
        siblingsCounts.append(list_of_answers[s]["siblings"])
    categories_list.append(siblingsCounts)

    genres = []
    for s in range(len(list_of_answers)):
        genres.append(list_of_answers[s]["genre"])
    categories_list.append(genres)

    artists = []
    for s in range(len(list_of_answers)):
        artists.append(list_of_answers[s]["artist"])
    categories_list.append(artists)

    print("List of all different category lists of user inputs: ")
    print(categories_list)


survey = [
    "What is your name?",
    "How old are you?",
    "What is your hometown?",
    "What is your date of birth? (DD/MM/YYYY)",
    "What's your favorite pet?",
    "What's your favorite color",
    "How many siblings do you have",
    "What is your favorite movie genre",
    "Who is your favorite music artist"]
keys = ["name", "age", "hometown", "DOB", "pet","color","siblings", "genre", "artist" ]

# Create a list that will store each person's individual survey responses.
list_of_answers = []

done = "NO"
while done == "NO":

    # Create the dictionary to store the responses.
    answers = {}
    print("New entry! Please answer the questions below.")

    # Iterate over the list of survey questions and take in user responses.
    for x in range(len(survey)):
        response = input(survey[x] +":     ")
        answers[keys[x]] = response

    list_of_answers.append(answers)

    answer = "yes"
    while answer != "no":
        answer = input("Do you want to change any of your answers   ").lower()
        if answer == "yes":
            answer2 = input("What do you want to change? (name, age, hometown, birthday, pet, color, siblings, genre, artist)    ").lower()
            if answer2 == 'name':
                change_name()
            elif answer2 == 'age':
                change_age()
            elif answer2 == 'hometown':
                change_hometown()
            elif answer2 == 'birthday':
                change_birthday()
            elif answer2 == 'pet':
                change_pet()
            elif answer2 == 'color':
                change_color()
            elif answer2 == 'siblings':
                change_siblings()
            elif answer2 == "genre":
                change_genre()
            else:
                change_artist()


    done = input("Are you done collecting information? Type YES or NO.     ").upper()


# Print the list of dictionaries.
print(list_of_answers)
printAllLists()

# Example of how to iterate over the list of dictionaries and pull out particular pieces of information.


with open('allanswers.json', 'r') as f:
    lines = f.read()
    info = json.loads(lines)
    list_of_answers.extend(info)
    f.close()


# Reopen the file in write mode and write each entry in json format.
f = open("allanswers.json", "w")
f.write('[\n')
index = 0
for answer in list_of_answers:
    if (index < len(list_of_answers)-1):
        f.write('\t')
        json.dump(answer,f)
        f.write(',\n')
    else:
        f.write('\t')
        json.dump(answer,f)
        f.write('\n')
    index += 1

f.write(']')
f.close()
