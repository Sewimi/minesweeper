from ast import While
import keyboard 
import time
import Field
import Display
# import pygame

# pygame.init()

console_mode = True


# background_colour = (255,255,255)
# (width, height) = (300, 200)
# screen = pygame.display.set_mode((width, height))




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
            board.append(Field.Field((i*size)+j))


    for i in range(len(board)): 
        surrounding_cells=Field.get_surrounding_cells(board,size,i)


        
        if board[i].is_mine == False:
            count=0
           
            for cell in surrounding_cells:
                if cell.is_mine == True:
                    count+=1
            board[i].content=f"{count}"
        else:
            board[i].content="*"
                    
            



    
    return board
        

   



def print_board(board,size):
    for i,field in enumerate(board):
        
        if i%size==0:
            print("\n")
            for i in range(size):
                print("--",end="")
            print("")
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

def check_win_lose(board,size):
    for field in board:

        #Checking if game is lost
        if field.revealed == True and field.is_mine == True:
            print_board(board,size)
            print("You Have Lost")
            return True

        #Cheking if game has been won
        


def game_loop(board,size):
    if console_mode:
        while True:
            #don't spam game loop million times a sec
            time.sleep(0.1)
        
            
            #quitting game
            try:  
                if keyboard.is_pressed('q'):  
                    print('You have exited the game')
                    break
            except:
                print("an Error Occured")


            print_board(board,size)
            action=get_player_input(size)


            board[size*action["row"]+action["column"]].update_content(action["action"],board)

            if(check_win_lose(board,size)):
                restart=input("Do you want to restart the game? (y/n): ")
                if restart == "y":
                    start_Game()
                else:
                    print("Goodbye!")
                    break
    else:
        while True:
            #don't spam game loop million times a sec
            time.sleep(0.1)
            pygame.display.flip()
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break


            action=get_player_input(size)


            board[size*action["row"]+action["column"]].update_content(action["action"],board)

            if(check_win_lose(board,size)):
                restart=input("Do you want to restart the game? (y/n): ")
                if restart == "y":
                    start_Game()
                else:
                    print("Goodbye!")
                    break


        


start_Game()
 