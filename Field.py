import random


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
    
    def update_content(self,action):
        if action == "r":
            self.revealed=True
        if action == "m":
            self.marked=True


    def reveal():
        pass
        




