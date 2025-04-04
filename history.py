def save_history(text):
    with open('score.txt','a') as f:
        f.write(text + '\n')


def read_history():
    with open('score.txt','r') as f:
        content = f.read()
        print(" Game History:\n" + content if content else "No history yet.")