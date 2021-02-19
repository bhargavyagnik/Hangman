import time
import random
from os import system

def read_words(path):
    '''

    :param path: it would take the path where the file containging the words is. E.g. 'words.txt.' (String)
    :return: The list of words that would be used in the hangman game.
    '''
    try:
        with open(path) as f:
            content=f.read()
            words=content.split('\n')
    except:
        print('Error opening file')
    return words

def random_picker(words):
    '''
    A function that would pick a single word at random
    :param words:  The list of words (List)
    :return: The randomly chosen word as string
    '''
    word='            '
    while(len(word)>10):
        word=random.choice(words)

    return word

def convert_unknown(word, letters_known):
    '''
    A function that would convert a word into underscores for letters that are not guessed
    so suppose word is "Apple" and letters known are 'a','p','l' so this function would return
    string as 'ap_l_'
    :param word:  The word with whom we want to replace underscores (List)
    :param letters_known: The letters that are correctly guessed by the player (List)
    :return: String with underscores and letter.
    '''
    s=''
    temp = letters_known.copy()
    for i in word:
        if i in temp:
            s=s+str(i)
            temp.remove(i)
        else:
            s=s+'_'
    return s

def print_hangman(chances):
    if chances<10:
        print("\t"*5,"-"*10)
    if chances<9:
        print("\t"*5,"     |     ")
    if chances<8:
        print("\t"*5,"     __   ")
        print("\t"*5,"    (  )  ")
        print("\t"*5,"     ``   ")
    if chances < 7:
        print("\t"*5,"      |    ")
    if chances < 6:
        print("\t"*5,"   /|```|\  ")
    if chances < 5:
        print("\t"*5,"    |   |  ")
    if chances < 4:
        print("\t"*5,"    |___|  ")
    if chances < 3:
        print("\t"*5,"     /\   ")
    if chances < 2:
        print("\t"*5,"   /    \  ")
    if chances < 1:
        print("\t"*5,"    Hangman      ")
        print("\t"*5,"    Over      ")





if __name__=='__main__':
    chances= 10
    letters_known = []
    words = read_words('words.txt')
    word = list(str(random_picker(words)).lower())
    print("You have to guess {} letter".format(len(word)))
    while chances>0:
        print(" ".join(convert_unknown(word,letters_known)))
        letter = str(input("Guess a letter: ")).lower()
        if len(letter)==0 or letter.isalpha()==False or len(letter)>1:
            continue
        if letter in word and word.count(letter)>letters_known.count(letter):
            letters_known.append(letter)
        else:
            print("\n\nOOPS!!!!")
            chances=chances-1
            print_hangman(chances)
            print("Chances Left ",chances)
            if chances ==0:
                time.sleep(5)
                exit(0)
                print('Game over no chance left')
                print('The correct word was: {}'.format(''.join(word)))

        if '_' not in convert_unknown(word,letters_known):
            print('Wohoo ! You guessed the correct word {}'.format(''.join(word)))
            time.sleep(5)
            exit(0)

