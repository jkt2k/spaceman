import random
import os
game_over=False

def load_word():
    f=open(os.path.dirname(os.path.realpath(__file__))+'/words.txt','r')
    #credit https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
    words_list = f.readlines()
    f.close()
    words_list=words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    guessed=True
    for letter in list(secret_word):
        if letter not in letters_guessed:
            guessed=False
    return guessed

def get_guessed_word(secret_word, letters_guessed):
    temp_word=""
    for letter in list(secret_word):
        if letter in letters_guessed:
            temp_word=temp_word+letter
        else:
            temp_word=temp_word+"_"
    return temp_word

def is_guess_in_word(guess, secret_word):
    word_letters=list(secret_word)
    for i in word_letters:
        if guess in list(secret_word):
            return True
    return False

def spaceman(secret_word):
    print("Welcome to Spaceman!")
    print("Spaceman is a guessing game. There is a mystery word which you will try to guess one letter at a time. A placeholder is initially shown, with the number of blanks corresponding to the number of letters in the word. If the letter is in the mystery word, the position(s) of the letter(s) are revealed in the placeholders. Guess the word before you run out of guesses!")
    print("You win if you can guess the mystery word before the spaceman is drawn. The spaceman is made up of seven parts, and each part is drawn for each incorrect guess. If all seven parts get drawn before you guess the word, then you lose.")
    print("Your word contains "+str(len(secret_word))+" letters.")
    #inspired by Spaceman Project Spec from Make School
    begin_game=input("Ready? Press enter to begin the game.")
    guess_number=0
    letters_guessed=[]
    valid_letters_ascii=list(range(65,91))+list(range(97,123)) #acii ranges for all uppercase and lowercase letters
    global game_over
    incorrect_guesses_left=7
    not_yet_guessed=list("abcdefghijklmnopqrstuvwxyz")
    while game_over==False: #perma loop until game is over
        print("-------------------------")
        guess_number=guess_number+1
        print("Here's what the word looks like so far: "+get_guessed_word(secret_word, letters_guessed))
        not_yet_guessed_string=""
        for letter in not_yet_guessed:
            not_yet_guessed_string=not_yet_guessed_string+letter
        print("These letters haven't been guessed yet: "+not_yet_guessed_string)
        guess=input("Guess "+str(guess_number)+": ")
        if not len(list(guess))==1: #input can only be 1 character
            check_for_word=""
            for letter in guess:
                check_for_word=check_for_word+letter.lower()
            if check_for_word==secret_word: #...unless they guess the word itself
                game_over=True
                print("[!!!!!] YOU WIN!!! You figured out what the word is.")
            else:
                print("You can only enter one character.")
                guess_number=guess_number-1
        elif ord(guess) not in valid_letters_ascii:
            print("Please enter a valid character.")
        else:
            real_guess=guess.lower()
            if real_guess in letters_guessed: #check if letter has already been guessed
                print("You already guessed that letter.")
                guess_number=guess_number-1
            else:
                if is_guess_in_word(real_guess, secret_word)==True: #found new letter in word? do this
                    print("[!] YES! \""+real_guess.upper()+"\" is in the word.")
                    letters_guessed.append(real_guess)
                    not_yet_guessed.remove(real_guess)
                    if is_word_guessed(secret_word,letters_guessed)==True:
                        print("[!!!] ...YOU GOT IT! The word is "+secret_word+".")
                        game_over=True
                    else:
                        print("LETTER UNCOVERED: "+get_guessed_word(secret_word,letters_guessed))
                else: #letter not in word
                    print("[!] WRONG! \""+real_guess.upper()+"\" is NOT in the word.")
                    incorrect_guesses_left=incorrect_guesses_left-1
                    letters_guessed.append(real_guess)
                    not_yet_guessed.remove(real_guess)
                    if incorrect_guesses_left==0:
                        game_over=True
                        print("[!] YOU LOSE!")
                        print("The word was \""+secret_word+".\"")
                    else:
                        print("You have "+str(incorrect_guesses_left)+" guesses left.")

secret_word = load_word()
spaceman(secret_word)