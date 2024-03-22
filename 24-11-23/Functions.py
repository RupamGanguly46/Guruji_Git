def tictactoe():
    #Creating board
    game=[1,2,3,4,5,6,7,8,9]

    #Choosing sign
    player1=input("Circle(O) or Cross(X)?")
    if player1=="O":
        player2="X"
    else:
        player2="O"

    win1=[player1,player1,player1]
    win2=[player2,player2,player2]

    #Game
    while True:
        #filling moves
        pos=int(input(f"Player 1 enter your position \n{game}\t"))
        game[pos-1]=player1
        
        pos=int(input(f"Player 2 enter your position \n{game}\t"))
        game[pos-1]=player2

        #extracting portions of board
        row1=game[0:2]
        row2=game[3:6]
        row3=game[6:9]
        col1=[game[i] for i in [0, 3, 6]]
        col2=[game[i] for i in [1, 4, 7]]
        col3=[game[i] for i in [2, 5, 8]]
        diag1=[[game[i] for i in [0, 4, 8]]]
        diag2=[[game[i] for i in [2, 4, 6]]]

        #All ways of winning at one place
        combinations=[row1,row2,row3,col1,col2,col3,diag1,diag2]

        #Check if won
        if win1 in combinations:
            print(f"PLAYER 1 WINS!\n{game}")
            break
        elif win2 in combinations:
            print(f"PLAYER2 WINS!!\n{game}")
            break
        
        # if (i for i in range(0,9)) not in game:
        #     print("Board filled, Draw")
        #     break
        
        #checking if board is filled
        over=0
        for i in range(9):
            if i in game:
                break
        else:
            print("Board filled, Draw")
            over=1
        if(over):
            break
        
        

tictactoe()