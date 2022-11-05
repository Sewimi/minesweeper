import elements





def game():

    board=elements.Board(11,1)
    print(board)
    board.print_board()

    print("Welcome to minesweeper!")
    print("If you want to exit the game, type at any moment 'exit'")
    print("Have fun!")
    
    while True:
        

        row=input("enter row: ")
        if row == "exit":
            break

        col=input("enter col: ")

        if col == "exit":
            break

        row=int(row)
        col=int(col)

        lost=board.board[row][col].reveal()
        if lost == -1:
            print("\nYou lost!\n")
            print(board)
            break


        board.print_board()
    
    x=input("play again?(y/n):")
    if x == "y":
        game()


game()