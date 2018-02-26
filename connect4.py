#connect4.py
#Jesse Weaver and Fangge Denge, CS 111, Winter 2016 with Lauren Milne 
#A program that runs Connect 4

from graphics import *
from Board import *

# define function for user to play with computer
def with_computer(window):
    
    board = Board()
    print("Player is red, Computer is Yellow")
    print("\n")
    
    player = 0
    while player != '':
           
        if player % 2 == 0:
            choice = input("Player, Which column do you want to drop in? ")
            
            while board.pick_new(choice) == True:
                choice = input("Player, Which column do you want to drop in? ")
            column = int(choice) - 1
            
            if choice == '-1':
                exit()
       
            board.drop(column, 1, window, "red")       
            name = "Player"
            board.check(name)
            player = player + 1 
            
        elif player % 2 != 0:
            board.play(window, player) 
            
            name0 = "Computer"
            board.check(name0)
            player = player + 1 
            print(board.list) 
            
            if player == 42:
                print("No one win")
                input("press anything to exit")
                exit()

                
# define function for user to play with another user
def two_players(window):
    
    name1 = "Player 1"
    name2 = "Player 2"
    board = Board() 
    player = 0
    print("Player 1 is red, Player 2 is yellow.")
    print("\n")
    
    while player != '':
           
        if player % 2 == 0:
            choice = input("Player 1, Which column do you want to drop in? ")
            
            while board.pick_new(choice) == True:
                choice = input("Player 1, Which column do you want to drop in? ")
            column = int(choice) - 1 
            
            if choice == '-1':
                exit()

            board.drop(column, 1, window, "red")             
            board.check(name1)
            player = player + 1 
            print(board.list)
        
        elif player % 2 != 0:
            choice = input("Player 2, Which column do you want to drop in? ")
            
            while board.pick_new(choice) == True:
                choice = input("Player 2, Which column do you want to drop in? ")
            column = int(choice) - 1 
            
            if choice == '-1':
                exit()
            
            board.drop(column, 2, window, "yellow")
            board.check(name2)
            player = player + 1
                
            print(board.list)
            
                        
            if player == 42:
                print("No one win")
                input("press anything to exit")
                exit()

# asks for user input on if they would like to play agianst the computer or another user
def choose_game(window):
    
    mode = input("What mode do you want to play? a for two players, b to play with computer.\n (Press -1 to exit to quit anytime during the game)")
    run = False
    while run == False:
        if mode == 'a':
            two_players(window)
        elif mode == 'b':
            with_computer(window)
        elif mode == "-1":
            exit()
        else:
            print("Please enter only a or b.")
            mode = input("What mode do you want to play? (a - two players, b - with computer) ")
            run == False

# creates grpahic window and board and runs the mode choose by the user 
def main():

    window = GraphWin("Connect4", 1000, 800)
    r = Rectangle(Point(150, 700), Point(850, 100))
    r.draw(window)
    brightBlue = color_rgb(0,200,250)
    r.setFill(brightBlue)
    
    n = 1
    a = 200
    b = 750 
    
    for x in range(7):
        number = Text(Point(a, b), n)
        n = n + 1 
        a = a + 100
        number.draw(window)
    
    
    x = 200
    y = 150
    
    for j in range(7):
        for i in range(6):
            c0 = Circle(Point(x, y), 50)
            c0.setFill("white")
            c0.draw(window)
            
            if y < 650:
                x = x
                y = y + 100
            elif y == 650:
                x = x + 100
                y = 150  
     
    print("Welcome to Connect 4! The goal of the game is to get four markers in a row, ")
    print("either vertically, horizontally, or diagonally. Each marker will drop to ")   
    print("the bottom of the column and each player can only drop one marker per turn. ")
    print("Once a player gets four in a row or the board is full, the game is over. ")
    print("\n")

    choose_game(window)
    
    
if __name__ == "__main__":
    main()
