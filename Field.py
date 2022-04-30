import random
import math


class Field:

    def __init__(self,pos):
        if(random.randint(0,6)==0):
            self.is_mine=True
        else:
            self.is_mine=False
        self.pos=pos
        self.content=''
        self.revealed=False
        self.marked=False
    
    def update_content(self,action,board):
        if action == "r" and self.revealed==False:
            self.revealed=True
            if(self.is_mine):
                pass
             #we ll handle losing later

            if self.content=="0":
                if(self.is_mine):
                    print("zjebales dejw")
                surrounding_cells=get_surrounding_cells(board, int(math.sqrt(len(board))),self.pos)
                for cell in surrounding_cells:     
                    cell.update_content("r",board)

        if action == "m":
            self.marked=True


    def reveal():
        pass
        



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
                
                        

