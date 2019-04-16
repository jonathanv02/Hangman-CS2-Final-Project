# Hangman-CS2-Final-Project
"""
Name: Jonathan Villanueva
Assignment #: A5-05: Linear & Binary Search
Summary:

HONOR CODE: On my honor, I have neither given nor recieved
any unacknowledged aid on this program
Jonathan Villanueva
"""
from graphics import *
import random
import string

"""
Description:
Parameters:
Return:
Plan:
"""
def draw_window():
    #this is the dimension of the window and making it
    win = GraphWin("Hangman Game", 500, 500)
    win.yUp()	#makes (0,0) at the bottom left
    return win

#def draw_circle(win):

#def draw_line(win):

#def draw_rect():



def open_file():
    open_file = open("words.txt")
    file_list = []
    for line in open_file:
        file_list.append(line)
    return file_list

def random_word(file_list):
    random_word = random.choice(file_list)
    return random_word


def hangman_game(word):
    turns = 6
    guesses = ""
    while turns > 0:
        guess = raw_input("Guess a letter:")                  
        if guess not in word:
            turns -= 1
            print " Your have {} turns left".format(turns)
        else:
            guesses += guess
                
            
    if turns == 0:
        print "You Lose"
    else:
        print " you win with {] turns left".format(turns) 
    print "{}".format(word)



def main():
    #win = draw_window()
    file_list = open_file()
    word = random_word(file_list)
    hangman_game(word)
    #win.getMouse()  #waits for the user to click the screen
    #win.close()	    #closes the window
       
if __name__ == "__main__":
    main()
