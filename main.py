game = True
while game:
    print("Welcome to Rock, Paper & Scissors")
    rounds = int(input("How many rounds would you like to have? :"))
    p1_wins = 0
    p2_wins = 0
    while rounds!=0:
        player_1 = input("player 1 : ")
        player_2 = input("player 2 : ")
        choice = ["rock","paper","scissors"]
        if (player_1.lower() == choice[0]) and (player_2.lower() == choice[2]):
            p1_wins+=1
            print("player_1 beats player_2")
        
        elif (player_1.lower() == choice[1]) and (player_2.lower() == choice[0]):
            p1_wins+=1
            print("player_1 beats player_2")
        
        elif (player_1.lower() == choice[2]) and (player_2.lower() == choice[1]):
            p1_wins+=1
            print("player_1 beats player_2")
        
        elif player_1.lower() == player_2.lower():
            print("its a draw")
        else:
            p2_wins+=1
            print("player_2 beats player_1")
        
        rounds-=1
    
    print(p1_wins,p2_wins)    
    if p1_wins > p2_wins:
        print("Winner is Player 1")
    else:
        print("Winner is Player 2")
    
    
    
    ans = input("Would you like to play again? y/n :")
    if ans.lower() == "n":
        game = False
    else:
        continue