def save_history(text):
    with open('score.txt','a') as f:
        f.write(text + '\n')


def read_history():
    with open('score.txt','r') as f:
        content = f.readlines()
        player_wins = [line for line in content if "Player won" in line]
        computer_wins = [line for line in content if "Computer won" in line]
        draw = [line for line in content if "draw" in line]
        print(f""" 
            Game stats
            ------------------
            Player wins: {len(player_wins)}
            Computer wins: {len(computer_wins)}
            Draws: {len(draw)}
""")