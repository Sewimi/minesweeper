import elements





def game():

    board=elements.Board(11,1)
    print(board)
    board.print_board()

    print("Welcome to minesweeper!")
    print("If you want to exit the game, type at any moment 'exit'")
    print("Have fun!")
    
    while True:

        
        
        action=input("reveal(r) or mark(m)?: ")
        if action == "exit":
            break
        if action=="win":
            board.xd()
            lost=0

        row=input("enter row: ")
        if row == "exit":
            break

        col=input("enter col: ")

        if col == "exit":
            break

        row=int(row)
        col=int(col)

        if action=="r":
            lost=board.board[row][col].reveal()
        elif action=="m":
            lost=board.board[row][col].mark()


        if lost == -1:
            print("\nYou lost!\n")
            print(board)
            break

        if board.check_win():
            print("You've won the game!")
            print(board)
            break



        board.print_board()
    
    x=input("play again?(y/n):")
    if x == "y":
        game()



game()