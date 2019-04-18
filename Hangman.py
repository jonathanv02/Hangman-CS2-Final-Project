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

def draw_circle(center, radius, color, win):
    circle = Circle(center, radius)
    circle.draw(win)

def draw_line(P1, P2, win):
    line = Line(P1, P2)
    line.draw(win)

def draw_rect(x1, y1, x2, y2, win):
    rect = Rectangle(Point(x1, y1), Point(x2, y2))
    rect.draw(win)


def open_file():
    open_file = open("words.txt")
    file_list = []
    for line in open_file:
        file_list.append(line)
    return file_list

def random_word(file_list):
    random_word = random.choice(file_list)
    return random_word


def draw_structure(win):
    w = win.getwidth()
    h = win.getHeight()
    



def hangman_game(word):
    turns = 6
    guesses = ""
    word_len = len(word)-1
    print " The word is {} letters long".format(word_len)
    while len(guesses) != len(word):
        guess = raw_input("Guess a letter:")                  
        if guess not in word:
            turns -= 1
            print "Your have {} turns left".format(turns)
        else:
            guesses += guess
            ch_loc = word[guess]
            print "You guessed a letter in letter {} of the word".format(ch_loc)
                
    print guesses
    print len(guesses)
    print len(word)
    if len(guesses) == len(word):
       print " you win with {} turns left".format(turns)
    elif turns == 0:
        print "You Lose"
        print "{}".format(word)


def main():
    #win = draw_window()
    file_list = open_file()
    word = "work"
    hangman_game(word)
    #win.getMouse()  #waits for the user to click the screen
    #win.close()	    #closes the window
       
if __name__ == "__main__":
    main()
    
