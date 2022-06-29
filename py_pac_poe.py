
welcome_message = '''
----------------------
Let's play Py-Pac-Poe!
----------------------
'''

player = "X"
k = {
    'a1': ' ', 
    'b1': ' ', 
    'c1': ' ', 
    'a2': ' ', 
    'b2': ' ',
    'c2': ' ',
    'a3': ' ',
    'b3': ' ',    
    'c3': ' '
    }



win_opts = [
    ['a1','b1','c1'],
    ['a2','b2','c2'],
    ['a3','b3','c3'],
    ['a1','b2','c3'],
    ['a3','b2','c1'],
    ['a1','a2','a3'],
    ['b1','b2','b3'],
    ['c1','c2','c3'],
]

score = {
    'X': 0,
    'O': 0,
    'Ties': 0 
}

    
    
def start_game():
    global k, player, score
    winner = "none"
    while winner == "none":
        player_opt = input(f"Player's {player} Move (example B2): ").lower()
        if player_opt not in k:
            print("Bogus move! Try again... (example B2)")
        elif k[player_opt] != " ":
            print ("Position is already taken")
        else:
            k[player_opt]=player
            board = f'''
                    A   B   C

                1)  {k["a1"]} | {k["b1"]} | {k['c1']} 
                    -----------
                2)  {k['a2']} | {k['b2']} | {k['c2']} 
                    -----------
                3)  {k['a3']} | {k['b3']} | {k['c3']} 
                
                '''
            print(board)
            for win_opt in win_opts:
                if k[win_opt[0]] == player and k[win_opt[1]] == player and k[win_opt[2]] == player:
                    winner = player
                    score[player] = score[player] + 1
                    print(f'player {player} Wins the game!')
                    print(f'Congrats to Player {player} for winning {score[player]} game(s)!')
                    print ( f'''
                          ---------- SCORE ----------
                           Player X: {score['X']}
                           Player O: {score['O']}
                           Ties: {score['Ties']}
                           ''')
                    for key in k:
                        k[key] = ' '
                elif " " not in k.values():
                    score["Ties"] = score["Ties"] + 1
                    print(f'Another tie!')
                else:
                    continue
            if player == "X":
                player = "O"
            else:
                player = "X" 
        



print (welcome_message)
while True: 
    start = input('Enter "S" to start playing / Enter "Q" to Quit ').lower()
    if start == "s":
        
        start_game()
    elif start == "q":
        print('Bye!')
        break
    else:
        print ('Invalid option')
    

