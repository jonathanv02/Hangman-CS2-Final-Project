    
"""
Name: Jonathan Villanueva
Assignment #: A5-05: Linear & Binary Search
Summary: Hangman game using a graphics window

HONOR CODE: On my honor, I have neither given nor recieved
any unacknowledged aid on this program
Jonathan Villanueva
"""
from graphics import *
import random
import string

"""
Description: opens the graphics window
Parameters:none
Return:
    win: graphics window to be used in other methods
Plan: will give the graphics a certain dimension and open it
"""
def draw_window():
    #this is the dimension of the window and making it
    win = GraphWin("Hangman Game", 500, 500)
    win.yUp()	#makes (0,0) at the bottom left
    return win
"""
Description: draws a circle in a given location
Parameters:
    center: center point of the circle
    radius: length of the radius of the circle
    win: the garphics window
Return:
    circle: cirlce that will be drawn
Plan: will give a center point, radius, and draw it
"""
def draw_circle(center, radius,win):
    circle = Circle(center, radius)
    circle.draw(win)
    return circle

"""
Description: draws lines in a given place
Parameters:
    x1: first x- coord of the end of the line
    y1: first y- coord of the end of the line
    x2: second x- coord of the end of the line
    y2: second y- coord of the end of the line
    color: color given 
    win: the graphics window
Return:
    line: the line that is drawn
Plan: Will add points for the ends of the lines, color it, and draw it.
"""
def draw_line(x1, y1, x2, y2, color, win):
    line = Line(Point(x1, y1), Point(x2, y2))
    line.setFill(color)
    line.draw(win)
    return line

"""
Description: adds text into the graphics window
Parameters:
    x: x coordinate
    y: y coordinate
    string: text that will be draw
    color: color for the string
    win: the graphics window
Return: nothing
Plan: have a point for the text, color it, size it, and draw it.
"""
def text( x, y, string, color, win):
    text = Text(Point(x, y), string)
    text.setFill(color)
    text.setSize(36)
    text.draw(win)

"""
Description: opens the file of the list of words
Parameters: none
Return:
    file_list: list of words 
Plan: will open the text file and append each item into an empty list
"""
def open_file():
    open_file = open("words.txt")
    file_list = []
    for line in open_file:
        file_list.append(line)
    return file_list

"""
Description:
Parameters:
Return:
Plan:
"""
def random_word(file_list):
    random_word = random.choice(file_list)
    return random_word

"""
Description: draws the structure where the man will be 
Parameters:
    win: the graphics window
Return: nothing
Plan: will use lines to idraw the structure 
"""
def draw_structure(win):
    w = win.getWidth()
    h = win.getHeight()
    draw_line(w/4, h/4, w/4, h/4*3, "black", win)
    draw_line(w/4, h/4*3, w/4*2, h/ 4*3, "black", win)

"""
Description: makes a list of shape comands for the mans body
Parameters:
    win: graphics window
Return:
    body: list of body part shapes
Plan: Will add the dimensions is the methods and place them in a list
"""
def man(win):
    w = win.getWidth()
    h = win.getHeight()
    body = draw_circle(Point(w/4*2,h/4*3-25), 25, win),\
           draw_line( w/4*2, h/4*3-50, w/4*2, h/2, "blue", win),\
           draw_line( w/4*2, h/4*3-60, w/4+ w/8, h/2+30, "blue", win),\
           draw_line( w/4*2, h/4*3-60, w/2+w/8, h/2+30, "blue", win),\
           draw_line( w/4*2, h/2, w/4+w/8, h/2-40, "brown", win),\
           draw_line( w/4*2, h/2, w/2+w/8, h/2-40, "brown", win)
    return body

"""
Description: Plays the game of Hangman
Parameters:
    word: random word from a list
    win: graphics window
Return: nothing
Plan: Having a while loop until the amount of turns are zero, it will check
through each letter in the word and check if the letter guessed is in the word.
If it is not in the word, it will print "-", or else, the letter. When the
guessed word is wrong, it will add a body part to the man. 
"""
def hangman_game(word, win):
    w = win.getWidth()
    h = win.getHeight()
    index_count = 0
    body = man(win)

    # undraws the list of body parts from the window
    for item in body:
        item.undraw()
    guesses = ''
    turns = 6
    while turns > 0:         
        wrong = 0             
        for ch in word:      
            if ch in guesses:    
                print ch,    
            else:
                print "_",     
                wrong += 1  
        if wrong == 0:
            print
            text( w/2, h/2, "You won", "green", win)
            text( w/2, h/4, "You Guessed: {}".format(word), "green", win)
            #breaks out of script
            break
        print
        guess = raw_input("guess a letter:") 
        guesses += guess                    
        if guess not in word:  
            turns -= 1        
            print "Wrong"    
            print "You have", + turns, 'more guesses'

            # draws the item in the list of body parts and adds 1 to index count
            body[index_count].draw(win)
            index_count += 1
            if turns == 0:           
                text( w/2, h/2,"You Lose", "red", win)
                text( w/2, h/4, "The word was: {}".format(word), "red", win)
                draw_line(w/10, h-h/10, w-w/10, h/10, "red", win)
                draw_line(w-w/10, h-h/10, w/10, h/10, "red", win)

"""
Description: calls all the methods neede to do the game
Parameters: none
Return: nothing
Plan: Will place the methods that will need to be called 
"""
def main():
    win = draw_window()
    file_list = open_file()
    word = random_word(file_list)
    draw_structure(win)
    hangman_game(word, win)
    win.getMouse()  #waits for the user to click the screen
    win.close()	    #closes the window

       
if __name__ == "__main__":
    main()
    
