import random
import os

game_over=False
incorrect_guesses_left=7

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''

    f=open(os.path.dirname(os.path.realpath(__file__))+'/words.txt','r')
    # credit https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
    words_list = f.readlines()
    f.close()

    words_list=words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    guessed=True
    for letter in list(secret_word):
        if letter not in letters_guessed:
            guessed=False
    return guessed

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    temp_word=""
    for letter in list(secret_word):
        if letter in letters_guessed:
            temp_word=temp_word+letter
        else:
            temp_word=temp_word+"_"
    return temp_word

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    if guess in list(secret_word):
        return True
    else:
        return False

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    print("Welcome to Spaceman!")
    print("Spaceman is a guessing game. There is a mystery word which you will try to guess one letter at a time. A placeholder is initially shown, with the number of blanks corresponding to the number of letters in the word. If the letter is in the mystery word, the position(s) of the letter(s) are revealed in the placeholders. Guess the word before you run out of guesses!")
    print("You win if you can guess the mystery word before the spaceman is drawn. The spaceman is made up of seven parts, and each part is drawn for each incorrect guess. If all seven parts get drawn before you guess the word, then you lose.")
    print("Your word contains "+str(len(secret_word))+" letters.")
    # Inspired by Spaceman Project Spec from Make School
    begin_game=input("Ready? Press enter to begin the game.")
    guess_number=0
    letters_guessed=[]
    global game_over
    not_yet_guessed=list("abcdefghijklmnopqrstuvwxyz")
    while game_over==False:
        print("-------------------------")
        guess_number=guess_number+1
        guess=input("Guess "+str(guess_number)+": ")
        if not len(list(guess))==1:
            print("You can only enter one letter.")
            guess_number=guess_number-1
        else:
            if guess in letters_guessed:
                print("You already guessed that letter.")
                guess_number=guess_number-1
            else:
                if is_guess_in_word(guess, secret_word)==True:
                    print("YES! \""+guess+"\" is in the word.")
                    letters_guessed.append(guess)
                    not_yet_guessed.remove(guess)
                    if is_word_guessed(secret_word,letters_guessed)==True:
                        print("...YOU GOT IT! The word is "+secret_word+".")
                        game_over=True
                    else:
                        print("Here's what the word looks like now: "+get_guessed_word(secret_word,letters_guessed))
                        not_yet_guessed_string=""
                        for letter in not_yet_guessed:
                            not_yet_guessed_string=not_yet_guessed_string+letter
                        print("These letters haven't been guessed yet: "+not_yet_guessed_string)



    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost

#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)