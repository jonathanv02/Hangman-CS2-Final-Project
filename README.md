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

def draw_circle(win):

def draw_line(win):

def draw_rect():

def hangman_game(win, word):
    turns = 6
    guess_letter = raw_input("What letter would you like to guess:")
    while turns != 0:
        if guess_letter in word:
            if guess_letter == word[]
        
        else:
            #puts letter to the wrong guess list and draws a body part
            turns -= 1
        





def main():
    win = draw_window()



    win.getMouse()  #waits for the user to click the screen
    win.close()	    #closes the window
       
if __name__ == "__main__":
    main()

