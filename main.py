from ast import While
import keyboard 
import time
from Field import Field


size=0


def start_Game():
    print("welcome to Mine Sweeper!")
    size=int(input("choose your board size: "))
    board=initialize_board(size)
    game_loop(board,size)




def initialize_board(size):
    board=[]
    for i in range(size):
        for j in range(size):
            board.append(Field([i,j]))


    for i in range(len(board)): 
        surrounding_cells=get_surrounding_cells(board,size,i)


        
        if board[i].is_mine == False:
            count=0
           
            for cell in surrounding_cells:
                if cell.is_mine == True:
                    count+=1
            board[i].content=count
        else:
            board[i].content="*"
                    
            



    
    return board
        

def get_surrounding_cells(board,size,ind):
    surrounding_cells=[]
    
    if ind in range(0,len(board)-size):
        surrounding_cells.append(board[ind+size])
                    

    if ind in range(size,len(board)):
        surrounding_cells.append(board[ind-size])
                    
            
    if ind in range(1,len(board)):
        surrounding_cells.append(board[ind-1])
                    

    if ind in range(0,len(board)-1):                         
        surrounding_cells.append(board[ind+1])
    

 
    return surrounding_cells
                
                        
   



def print_board(board,size):
    for i,field in enumerate(board):
        
        if i%size==0:
            print("\n")
            print("----------")
        if field.revealed == True:
            print(f"{field.content}|",end="")
        else:
             print("?|",end="")

    print("\n\n\n")

    

def get_player_input(size):
    action=""
    row=-1
    column=-1
    while (action != "m" and action !="r") or (row<0 or row>size)or (column<0 or column>size):
        action=input("do you want to mark the cell(m) or reveal it (r)?:")    
        row=int(input("select the row:"))-1
        column=int(input("select the column:"))-1
    return {
        "row":row,
        "column":column,
        "action":action

    }

def check_win():
    pass


def game_loop(board,size):
    while True:
        #don't spam game loop million times a sec
        time.sleep(1)
    
        
        #quitting game
        try:  
            if keyboard.is_pressed('q'):  
                print('You have exited the game')
                break
        except:
            print("an Error Occured")


        #
        print_board(board,size)
        action=get_player_input(size)
        board[size*action["row"]+action["column"]].update_content(action["action"])
        check_win()


        


start_Game()
 