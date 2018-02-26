#Board.py
#Jesse Weaver and Fangge Denge, CS 111, Winter 2016 with Lauren Milne 
#A program that plays Connect 4

import random
from graphics import *

class Board:
    
    # create the seven lists for seven columns on the board
    def __init__(self):
        self.list = []
        for i in range(7):
            self.list.append([])
            for j in range(6):
                self.list[i].append(' ')
                
    # drops marker in the column the user selects
    def drop(self, column, marker, window, color):
        for i in range(7):
            if self.list[column][i] == ' ':
                self.list[column][i] = marker
                
                c1 = Circle(Point((column+1)*100 + 100, 750 - 100*(i+1)), 50)
                c1.setFill(color)
                c1.draw(window)
                return
            
    # if user does not input a valid input, asks for new input from user        
    def pick_new(self, choice):
        number = ['1', '2', '3', '4', '5', '6', '7', '-1']
        if choice in number:
            column = int(choice) -1 
            if self.list[column][5] != ' ' :
                print("That column is full. Please select new column.")
                return True
            else: 
                return False
        elif choice not in number:
            print("Please choose a number 1-7.  Enter -1 to exit.")
            return True

    # checks to see if there are 4 markers in a row of the same color for 
    # horizontal, digonal, and vertical, and if so, prints who wins and ends the game
    def check(self, name):
        
        # checks vertical
        for x in range(7):
            for y in range(3):
                if (self.list[x][y] != ' ' and self.list[x][y+1] != ' ' 
                    and self.list[x][y+2] != ' ' and self.list[x][y+3] != ' '):
                    if (self.list[x][y] == self.list[x][y+1] == 
                        self.list[x][y+2] == self.list[x][y+3]):
                        print(self.list)
                        print(name, 'win')
                        input("press anything to exit")
                        exit()
                            
        # checks horizontal                 
        for x in range(4):
            for y in range(6):
                if (self.list[x][y] != ' ' and self.list[x+1][y] != ' ' 
                    and self.list[x+2][y] != ' ' and self.list[x+3][y] != ' '):
                    if (self.list[x][y] == self.list[x+1][y] == 
                        self.list[x+2][y] == self.list[x+3][y]):
                        print(self.list)
                        print(name, 'win')
                        input("press anything to exit")
                        exit()

        # checks diagonal up to the right
        for x in range(4):
            for y in range(3):
                if (self.list[x][y] != ' ' and self.list[x+1][y+1] != ' ' 
                    and self.list[x+2][y+2] != ' ' and self.list[x+3][y+3] != ' '):
                    if (self.list[x][y] == self.list[x+1][y+1] == 
                        self.list[x+2][y+2] == self.list[x+3][y+3]):
                        print(self.list)
                        print(name, 'win')
                        input("press anything to exit")
                        exit() 
                        
        # checks diagonal down to the right                
        for x in range(4):
            for y in range(3, 6):
                if (self.list[x][y] != ' ' and self.list[x+1][y-1] != ' ' 
                    and self.list[x+2][y-2] != ' ' and self.list[x+3][y-3] != ' '):
                    if (self.list[x][y] == self.list[x+1][y-1] == 
                        self.list[x+2][y-2] == self.list[x+3][y-3]):
                        print(self.list)
                        print(name, 'win')
                        input("press anything to exit")
                        exit()                 
        

    # this function acts as the computer AI and determines where the computer plays  
    def play(self, window, player):

        # drops one more marker veritcally to either win or block the user if 
        # there are three markers in a row that are the same color 
        
        #vertical
        for x in range(7):
            for y in range(3):
                if (self.list[x][y] != ' ' and self.list[x][y+1] != ' ' 
                    and self.list[x][y+2] != ' ' and self.list[x][y+3] == ' '):
                    if self.list[x][y] == self.list[x][y+1] == self.list[x][y+2]:
                        self.list[x][y+3] = 0
                        c2 = Circle(Point((x+1)*100 + 100, 750 - 100*(y+4)), 50)
                        c2.setFill("yellow")
                        c2.draw(window)
                        return
                        
        # drops one more marker horizontally to either win or block the user if 
        # there are three markers in a row that are the same color     
        
        #horizontal 
        for x in range(4):
            for y in range(6):
                if (self.list[x][y] != ' ' and self.list[x+1][y] != ' ' 
                    and self.list[x+2][y] != ' '):
                    if self.list[x][y] == self.list[x+1][y] == self.list[x+2][y]:
                        if self.list[x+3][y] == ' ':
                            if y == 0:
                                self.list[x+3][y] = 0
                                c2 = Circle(Point((x+4)*100 + 100, 750 - 100*(y+1)), 50)
                                c2.setFill("yellow")
                                c2.draw(window)
                                return
                            elif y != 0:
                                if self.list[x+3][y-1] != ' ':
                                    self.list[x+3][y] = 0
                                    c2 = Circle(Point((x+4)*100 + 100, 750 - 100*(y+1)), 50)
                                    c2.setFill("yellow")
                                    c2.draw(window)
                                    return
        
        for x in range(1, 5):
            for y in range(6):
                if (self.list[x][y] != ' ' and self.list[x+1][y] != ' ' 
                    and self.list[x+2][y] != ' '):
                    if self.list[x][y] == self.list[x+1][y] == self.list[x+2][y]:
                        if self.list[x-1][y] == ' ':
                                if y == 0:
                                    self.list[x-1][y] = 0
                                    c2 = Circle(Point(x*100 + 100, 750 - 100*(y+1)), 50)
                                    c2.setFill("yellow")
                                    c2.draw(window)
                                    return
                                if y != 0:
                                    if self.list[x-1][y-1] != ' ':
                                        self.list[x-1][y] = 0
                                        c2 = Circle(Point(x*100 + 100, 750 - 100*(y+1)), 50)
                                        c2.setFill("yellow")
                                        c2.draw(window)
                                        return
        
        # if there are two markers, then a space, and another marker all the 
        # same color in a horizontal row, the computer will drop in the open space

        #horizontal middle
        for x in range(4):
            for y in range(6):
                if (self.list[x][y] != ' ' and self.list[x+1][y] != ' ' 
                    and self.list[x+3][y] != ' '):
                    if self.list[x][y] == self.list[x+1][y] == self.list[x+3][y]:
                        if self.list[x+2][y] == ' ':
                            if y == 0:
                                self.list[x+2][y] = 0
                                c2 = Circle(Point((x+3)*100 + 100, 750 - 100*(y+1)), 50)
                                c2.setFill("yellow")
                                c2.draw(window)
                                return
                            elif y != 0:
                                if self.list[x+2][y-1] != ' ':
                                    self.list[x+2][y] = 0
                                    c2 = Circle(Point((x+3)*100 + 100, 750 - 100*(y+1)), 50)
                                    c2.setFill("yellow")
                                    c2.draw(window)
                                    return
        
        # if there is one marker, then a space, and two other markers all the
        # same color in a horizontal row, the computer will drop in the open space
        
        for x in range(4):
            for y in range(6):
                if (self.list[x][y] != ' ' and self.list[x+2][y] != ' ' 
                    and self.list[x+3][y] != ' '):
                    if self.list[x][y] == self.list[x+2][y] == self.list[x+3][y]:
                        if self.list[x+1][y] == ' ':
                            if y == 0:
                                self.list[x+1][y] = 0
                                c2 = Circle(Point((x+2)*100 + 100, 750 - 100*(y+1)), 50)
                                c2.setFill("yellow")
                                c2.draw(window)
                                return
                            elif y != 0:
                                if self.list[x+1][y-1] != ' ':
                                    self.list[x+1][y] = 0
                                    c2 = Circle(Point((x+2)*100 + 100, 750 - 100*(y+1)), 50)
                                    c2.setFill("yellow")
                                    c2.draw(window)
                                    return
                                
        # drops one more marker to either win or block the user when
        # there are three markers going up diagonally to the right all the same color 
        
        #diagonal up
        for x in range(4):
            for y in range(3):
                if (self.list[x][y] != ' ' and self.list[x+1][y+1] != ' ' 
                    and self.list[x+2][y+2] != ' '):
                    if self.list[x][y] == self.list[x+1][y+1] == self.list[x+2][y+2]:
                        if self.list[x+3][y+3] == ' ':
                            if self.list[x+3][y+2] != ' ':
                                self.list[x+3][y+3] = 0
                                c2 = Circle(Point((x+4)*100 + 100, 750 - 100*(y+4)), 50)
                                c2.setFill("yellow")
                                c2.draw(window)
                                return 
                            
        for x in range(1, 5):
            for y in range(1, 4):
                if (self.list[x][y] != ' ' and self.list[x+1][y+1] != ' ' 
                    and self.list[x+2][y+2] != ' '):
                    if self.list[x][y] == self.list[x+1][y+1] == self.list[x+2][y+2]:
                        if self.list[x-1][y-1] == ' ':
                            if y == 1:
                                if self.list[x-1][y-1] == ' ':
                                    self.list[x-1][y-1] = 0
                                    c2 = Circle(Point(x*100 + 100, 750 - 100*y), 50)
                                    c2.setFill("yellow")
                                    c2.draw(window)
                                    return
                            else:
                                if self.list[x-1][y-2] != ' ':
                                    self.list[x-1][y-1] = 0
                                    c2 = Circle(Point(x*100 + 100, 750 - 100*y), 50)
                                    c2.setFill("yellow")
                                    c2.draw(window)
                                    return
        
        # if there are two markers then a space and another marker all the same color 
        # going up diagonally to the right, the computer will drop in the open space
        
        #diagonal up middle
        for x in range(4):
            for y in range(3):
                if (self.list[x][y] != ' ' and self.list[x+1][y+1] != ' ' 
                    and self.list[x+3][y+3] != ' '):
                    if self.list[x][y] == self.list[x+1][y+1] == self.list[x+3][y+3]:
                        if self.list[x+2][y+2] == ' ':
                            if self.list[x+2][y+1] != ' ':
                                self.list[x+2][y+2] = 0
                                c2 = Circle(Point((x+3)*100 + 100, 750 - 100*(y+3)), 50)
                                c2.setFill("yellow")
                                c2.draw(window)
                                return
                            
        # if there is one marker then a space and two others markers all the same color 
        # going up diagonally to the right, the computer will drop in the open space
        
        for x in range(4):
            for y in range(3):
                if (self.list[x][y] != ' ' and self.list[x+2][y+2] != ' ' 
                    and self.list[x+3][y+3] != ' '):
                    if self.list[x][y] == self.list[x+2][y+2] == self.list[x+3][y+3]:
                        if self.list[x+1][y+1] == ' ':
                            if self.list[x+1][y] != ' ':
                                self.list[x+1][y+1] = 0
                                c2 = Circle(Point((x+2)*100 + 100, 750 - 100*(y+2)), 50)
                                c2.setFill("yellow")
                                c2.draw(window)
                                return

                                
        # drops one more marker diagonally to either win or block the user when
        # there are three markers going down diagonally to the right all the same color
        
        #diagonal down
        for x in range(1, 5):
            for y in range(2, 5):
                if (self.list[x][y] != ' ' and self.list[x+1][y-1] != ' ' 
                    and self.list[x+2][y-2] != ' '):
                    if self.list[x][y] == self.list[x+1][y-1] == self.list[x+2][y-2]:
                        if self.list[x-1][y+1] == ' ':
                            if self.list[x-1][y] != ' ':
                                self.list[x-1][y+1] = 0
                                c2 = Circle(Point(x*100 + 100, 750 - 100*(y+2)), 50)
                                c2.setFill("yellow")
                                c2.draw(window)
                                return
                                 
        for x in range(4):
            for y in range(3, 6):
                if (self.list[x][y] != ' ' and self.list[x+1][y-1] != ' ' 
                    and self.list[x+2][y-2] != ' '):
                    if self.list[x][y] == self.list[x+1][y-1] == self.list[x+2][y-2]:
                        if self.list[x+3][y-3] == ' ':
                            if y == 3:
                                self.list[x+3][y-3] = 0
                                c2 = Circle(Point((x+4)*100 + 100, 750 - 100*(y-2)), 50)
                                c2.setFill("yellow")
                                c2.draw(window)
                                return
                            else:
                                if self.list[x+3][y-4] != ' ':
                                    self.list[x+3][y-3] = 0
                                    c2 = Circle(Point((x+4)*100 + 100, 750 - 100*(y-2)), 50)
                                    c2.setFill("yellow")
                                    c2.draw(window)
                                    return

                                    
        # if there are two markers then a space and another marker all the same color 
        # going down diagonally to the right, the computer will drop in the open space 
        
        #diagonal down middle
        for x in range(4):
            for y in range(3, 6):
                if (self.list[x][y] != ' ' and self.list[x+1][y-1] != ' ' 
                    and self.list[x+3][y-3] != ' '):
                    if self.list[x][y] == self.list[x+1][y-1] == self.list[x+3][y-3]:
                        if self.list[x+2][y-2] == ' ':
                            if self.list[x+2][y-3] != ' ':
                                self.list[x+2][y-2] = 0
                                c2 = Circle(Point((x+3)*100 + 100, 750 - 100*(y-1)), 50)
                                c2.setFill("yellow")
                                c2.draw(window)
                                return
        
        # if there is one marker, then a space and two others markers all the same color 
        # going down diagonally to the right, the computer will drop in the open space 
        
        #diagonal down middle
        for x in range(4):
            for y in range(3, 6):
                if (self.list[x][y] != ' ' and self.list[x+2][y-2] != ' ' 
                    and self.list[x+3][y-3] != ' '):
                    if self.list[x][y] == self.list[x+2][y-2] == self.list[x+3][y-3]:
                        if self.list[x+1][y-1] == ' ':
                            if self.list[x+1][y-2] != ' ':
                                self.list[x+1][y-1] = 0
                                c2 = Circle(Point((x+2)*100 + 100, 750 - 100*y), 50)
                                c2.setFill("yellow")
                                c2.draw(window)
                                return
                            
        # stop when two horizontal markers of the same color are together and there are
        # no markers on either side of them
        
        #stop horizontal two
        for x in range(2, 4):
            for y in range(0, 1):
                if (self.list[x][y] != ' ' and self.list[x+1][y] != ' ' 
                    and self.list[x+2][y] == ' ' and self.list[x-1][y] == ' '):
                    if self.list[x][y] == self.list[x+1][y]:
                        self.list[x+2][y] = 0
                        c2 = Circle(Point((x+3)*100 + 100, 750 - 100*(y+1)), 50)
                        c2.setFill("yellow")
                        c2.draw(window)
                        return
                    
        for x in range(2, 4):
            for y in range(0, 1):
                if self.list[x][y] != ' ' and self.list[x+2][y] != ' ': 
                    if (self.list[x+1][y] == ' ' and self.list[x-1][y] == ' ' 
                        and self.list[x+3][y] == ' '): 
                        if self.list[x][y] == self.list[x+2][y]:
                            if y == 0:
                                self.list[x+1][y] = 0
                                c2 = Circle(Point((x+2)*100 + 100, 750 - 100*(y+1)), 50)
                                c2.setFill("yellow")
                                c2.draw(window)
                                return
                            elif y != 0:
                                if self.list[x+1][y-1] != ' ':
                                    self.list[x+1][y] = 0
                                    c2 = Circle(Point((x+2)*100 + 100, 750 - 100*(y+1)), 50)
                                    c2.setFill("yellow")
                                    c2.draw(window)
                                    return            

        for x in range(2, 4):
            for y in range(1, 6):
                if self.list[x][y] != ' ' and self.list[x+1][y] != ' ':
                    if (self.list[x+2][y] == ' ' and self.list[x-1][y] == ' ' 
                        and self.list[x-1][y-1] != ' ' and self.list[x+2][y-1] != ' '):
                        if self.list[x][y] == self.list[x+1][y]:
                            if y == 1:
                                self.list[x+2][y] = 0
                                c2 = Circle(Point((x+3)*100 + 100, 750 - 100*(y+1)), 50)
                                c2.setFill("yellow")
                                c2.draw(window)
                                return
                            elif y != 1:
                                if self.list[x+2][y-1] != ' ':
                                    self.list[x+2][y] = 0
                                    c2 = Circle(Point((x+3)*100 + 100, 750 - 100*(y+1)), 50)
                                    c2.setFill("yellow")
                                    c2.draw(window)
                                    return


                            
                            
        # if the computer is not forced to play by one of the checks above, the computer will 
        # drop a marker in a random colomn
        column_range1 = 7  
        column_list1 = [0, 1, 2, 3, 4, 5, 6]                     
                    
        # if column generated is already full, it will delete column from the list and 
        # generate another column
        for n in range(7):
            if self.list[n][5] != ' ':
                column_list1.remove(n)
                column_range1 = column_range1 - 1
                
          
        
        origianl_list = True
        # For the column generated from the random list, the computer will check to see if there
        # are three markers in a row to the right or left of that column that are the users, and 
        # if in the row beneath that row of three, there is no marker of either color.  If so, the
        # column generated will be deleted from the list and new random column will be generated. 
        
        #stop dropping for horizontal
        for x in range(4):
            for y in range(1, 6):
                if self.list[x][y] == 1 and self.list[x+1][y] == 1 and self.list[x+2][y] == 1:
                    if self.list[x+3][y-1] == ' ':
                        if (x+3) in column_list1:
                            column_list1.remove(x+3)
                            column_range1 = column_range1 - 1
                            print(column_list1)
                            origianl_list = False
                            
                            
        for x in range(1, 5):
            for y in range(1, 6):
                if self.list[x][y] == 1 and self.list[x+1][y] == 1 and self.list[x+2][y] == 1:
                    if y == 1: 
                            if self.list[x-1][y-1] == ' ':
                                if (x-1) in column_list1:
                                    column_list1.remove(x-1)
                                    column_range1 = column_range1 - 1
                                    print(column_list1)
                                    origianl_list = False
                    elif y != 1:
                        if self.list[x-1][y-1] == ' ' and self.list[x-1][y-2] != ' ':
                            if (x-1) in column_list1:
                                column_list1.remove(x-1)
                                column_range1 = column_range1 - 1
                                print(column_list1)
                                origianl_list = False         
        
        #stop dropping for horizontal middle
        for x in range(4):
            for y in range(1, 6):
                if self.list[x][y] == 1 and self.list[x+2][y] == 1 and self.list[x+3][y] == 1:
                    if y == 1:
                        if self.list[x+1][y-1] == ' ':
                            if (x+1) in column_list1:
                                column_list1.remove(x+1)
                                column_range1 = column_range1 - 1
                                print(column_list1)
                                origianl_list = False
                    elif y != 1:        
                        if self.list[x+1][y-1] == ' ' and self.list[x+1][y-2] != ' ':
                            if (x+1) in column_list1:
                                column_list1.remove(x+1)
                                column_range1 = column_range1 - 1
                                print(column_list1)
                                origianl_list = False  
        
        for x in range(4):
            for y in range(1, 6):
                if self.list[x][y] == 1 and self.list[x+1][y] == 1 and self.list[x+3][y] == 1:
                    if y == 1:
                        if self.list[x+2][y-1] == ' ':
                            if (x+2) in column_list1:
                                column_list1.remove(x+2)
                                column_range1 = column_range1 - 1
                                print(column_list1)
                                origianl_list = False
                    elif y != 1:        
                        if self.list[x+2][y-1] == ' ' and self.list[x+1][y-2] != ' ':
                            if (x+2) in column_list1:
                                column_list1.remove(x+2)
                                column_range1 = column_range1 - 1
                                print(column_list1)
                                origianl_list = False                  
        
                                                               
        # For the column generated from the random list, the computer will check to see if there
        # are three markers in a diagonal line going up to ther right to the right or left of that
        # column that are the users, and if in the row beneath that line of three, there is no 
        # marker of either color.  If so, the column generated will be deleted from the list and
        # new random column will be generated. 
        
        #stop droping for diagonal up
        for x in range(4):
            for y in range(3):
                if self.list[x][y] == 1 and self.list[x+1][y+1] == 1 and self.list[x+2][y+2] == 1:
                    if self.list[x+3][y+2] == ' ' and self.list[x+3][y+1] != ' ':
                        if (x+3) in column_list1:
                            column_list1.remove(x+3)
                            column_range1 = column_range1 - 1
                            print(column_list1)
                            origianl_list = False   
                        
        for x in range(1, 5):
            for y in range(1, 4):
                if self.list[x][y] == 1 and self.list[x+1][y+1] == 1 and self.list[x+2][y+2] == 1:
                    if y == 1:
                        if self.list[x-1][y-1] == ' ':
                            if (x-1) in column_list1:
                                column_list1.remove(x-1)
                                column_range1 = column_range1 - 1
                                print(column_list1)
                                origianl_list = False
                    else: 
                        if self.list[x-1][y-1] == ' ' and self.list[x+3][y-2] != ' ':
                            if (x-1) in column_list1:
                                column_list1.remove(x-1)
                                column_range1 = column_range1 - 1
                                print(column_list1)
                                origianl_list = False
        
        #stop dropping for diagonal up middle
        for x in range(4):
            for y in range(3):
                if self.list[x][y] == 1 and self.list[x+1][y+1] == 1 and self.list[x+3][y+3] == 1:
                    if self.list[x+2][y+1] == ' ' and self.list[x+3][y] != ' ':
                        if (x+2) in column_list1:
                            column_list1.remove(x+2)
                            column_range1 = column_range1 - 1
                            print(column_list1)
                            origianl_list = False
                        
                        
        for x in range(4):
            for y in range(3):
                if self.list[x][y] == 1 and self.list[x+2][y+2] == 1 and self.list[x+3][y+3] == 1:
                    if y == 1:
                        if self.list[x+1][y] == ' ':
                            if (x+1) in column_list1:
                                column_list1.remove(x+1)
                                column_range1 = column_range1 - 1
                                print(column_list1)
                                origianl_list = False
                    else:
                        if self.list[x+1][y] == ' ' and self.list[x+1][y-1] != ' ':
                            if (x+1) in column_list1:
                                column_list1.remove(x+1)
                                column_range1 = column_range1 - 1
                                print(column_list1)
                                origianl_list = False

                                        
        # For the column generated from the random list, the computer will check to see if there
        # are three markers in a diagonal line going down to ther right to the right or left of that
        # column that are the users, and if in the row beneath that line of three, there is no 
        # marker of either color.  If so, the column generated will be deleted from the list and
        # new random column will be generated. 
        
        #stop dropping for diagonal down 
        for x in range(4):
            for y in range(3, 6):
                if self.list[x][y] == 1 and self.list[x+1][y-1] == 1 and self.list[x+2][y-2] == 1:
                    if y == 3:
                        if self.list[x+3][y-3] == ' ':
                            if (x+3) in column_list1:
                                column_list1.remove(x+3)
                                column_range1 = column_range1 - 1
                                print(column_list1)
                                origianl_list = False
                    else:
                        if self.list[x+3][y-3] == ' ' and self.list[x+3][y-4] != ' ':
                            if (x+3) in column_list1:
                                column_list1.remove(x+3)
                                column_range1 = column_range1 - 1
                                print(column_list1)
                                origianl_list = False

                                
        for x in range(1, 5):
            for y in range(2, 5):
                if self.list[x][y] == 1 and self.list[x+1][y-1] == 1 and self.list[x+2][y-2] == 1:
                    if self.list[x-1][y] == ' ' and self.list[x-1][y-1] != ' ':
                        if (x-1) in column_list1:
                            column_list1.remove(x-1)
                            column_range1 = column_range1 - 1
                            print(column_list1)
                            origianl_list = False
                        
        #stop dropping for diagonal down middle  
        
        for x in range(4):
            for y in range(3, 6):
                if self.list[x][y] == 1 and self.list[x+1][y-1] == 1 and self.list[x+3][y-3] == 1:
                    if y == 3:
                        if self.list[x+2][y-3] == ' ':
                            if (x+2) in column_list1:
                                column_list1.remove(x+2)
                                column_range1 = column_range1 - 1
                                print(column_list1)
                                origianl_list = False
                    else:
                        if self.list[x+2][y-3] == ' ' and self.list[x+2][y-4] != ' ':
                            if (x+2) in column_list1:
                                column_list1.remove(x+2)
                                column_range1 = column_range1 - 1
                                print(column_list1)
                                origianl_list = False
        
        for x in range(4):
            for y in range(3, 6):
                if self.list[x][y] == 1 and self.list[x+2][y-2] == 1 and self.list[x+3][y-3] == 1:
                    if self.list[x+2][y-3] == ' ' and self.list[x+2][y-4] != ' ':
                        if (x+2) in column_list1:
                            column_list1.remove(x+2)
                            column_range1 = column_range1 - 1
                            print(column_list1)
                            origianl_list = False
                                
        # if the computer gets through all the checks above, the computer will drop in the randomly
        # selected comlumn 
        
        if len(column_list1) == 0:
            original_list = True
            
        #at the beginning, randomly drop in the middle of the board to increase the possibility of winning
        if player <= 8:
            column_list1 = [2, 3, 4]
            column_range1 = 3
            origianl_list = False
            
        if origianl_list == True:

            column_range = 7  
            column_list = [0, 1, 2, 3, 4, 5, 6]  

        # if column generated is already full, it will delete column from the list and 
        # generate another column
            for n in range(7):
                if self.list[n][5] != ' ':
                    column_list.remove(n)
                    column_range = column_range - 1

            random_column = random.randrange(column_range)   
            column = column_list[random_column]
                
        elif origianl_list == False:
            
            random_column1 = random.randrange(column_range1) 
            column = column_list1[random_column1]
            
            
        for i in range(6):
            if self.list[column][i] == ' ':
                self.list[column][i] = 0
                c3 = Circle(Point((column+1)*100 + 100, 750 - 100*(i+1)), 50)
                c3.setFill("yellow")
                c3.draw(window)
                return
                  