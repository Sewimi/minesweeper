import random

class Field:

    def __init__(self,pos_x,pos_y,board,value="0") -> None:
        self.hidden=True
        self.value=value #0-empty *-mine
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.board=board
        self.neighbours=self.find_neighbours()

    def find_neighbours(self):
        pot_neighbours=[[self.pos_x+1,self.pos_y],[self.pos_x-1,self.pos_y],[self.pos_x,self.pos_y+1],[self.pos_x,self.pos_y-1],
                        [self.pos_x+1,self.pos_y+1],[self.pos_x+1,self.pos_y-1],[self.pos_x-1,self.pos_y+1],[self.pos_x-1,self.pos_y-1]]
        neighbours=[]
        for n in pot_neighbours:
            for p in n:
                if p<0 or p == self.board.size: 
                    break
            else:
                neighbours.append(n)
        return neighbours
    
    def find_mines(self):
        if self.value == "*":
            return
        
        self.value=int(self.value)
        for row,col in self.neighbours:
            if self.board.board[row][col].value == "*":
                
                self.value+=1

        self.value=f"{self.value}"




    def reveal(self):
        if self.value == "*":
            return -1
        self.hidden=False
        for row,col in self.neighbours:
            neighbour=self.board.board[row][col]
            if neighbour.hidden == True and neighbour.value == "0":
                neighbour.reveal()
            elif neighbour.value != "*" and neighbour.hidden == True:
                neighbour.hidden=False

   

class Board:

    def __init__(self,size,difficulty) -> None:
        self.num_of_mines=(difficulty*size*size)/2
        self.size=size
        self.board=self.generate_board()
         
        for row in self.board:
            for col in row:
                col.find_mines()

    

    def generate_board(self):
        board=[]
        placed_mines=0
        for row in range(self.size):
            board.append([])
            for col in range(self.size):
                # if placed_mines < self.num_of_mines:
                #     board[i].append(random.choice(["0","0","0","0","*"]))
                # else:
                #     board[i].append("0")
                if placed_mines < self.num_of_mines:
                    board[row].append(Field(row,col,self,random.choice(["0","0","0","0","*"])))
                else:
                    board[row].append(Field(row,col,self))



        return board



    def print_board(self):
        x=""
        for row in self.board:
            for col in row:
                if col.hidden==True:
                    x+="?"
                else:
                    x+=col.value
            x+="\n"
        print(x)



    def __str__(self) -> str:
        x=""
        for row in self.board:
            for col in row:
                x+=col.value
            x+="\n"
        return x
       
