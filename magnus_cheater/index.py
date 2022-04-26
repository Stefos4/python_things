import chess.pgn
import pickle
import berserk


def save_table(tb,link):
    with open(link,"wb") as file:
        pickle.dump(tb,file)
        
def load_table(link):
    with open(link,"rb") as file:
        table = pickle.load(file)
        return table

def checkIfPlayerIsCheaterNow(pseudo,client):
    resp = client.users.get_public_data(pseudo)
    try:
        cheat = resp["tosViolation"]
        if cheat==True:
            print("****** - "+pseudo+" is a cheater!!! - ******")
            return True
    except:
        print(pseudo+" is not a cheater")
        return False
    

#games = open("C:\\Users\\HP\\Desktop\\chess\\magnus_cheater\\lichess_DrNykterstein_2022-02-20.pgn")
games = []
#game = chess.pgn.read_game(games)
#print(game.headers["White"])

MAGNUS_PSEUDO = "DrNykterstein"

oponents = []
all_names = []

cont = 1
i=1

while cont==1 and i<0:
    
    game = chess.pgn.read_game(games)
    
    if game==None:
        
        cont = 0
        
    else:
        
        new_name = game.headers["White"]

        if(game.headers["White"]==MAGNUS_PSEUDO):
            new_name = game.headers["Black"]

        if not(new_name in all_names):
            all_names.append(new_name)
    
    print(i)
    i+=1

lnk = "C:\\Users\\HP\\Desktop\\chess\\magnus_cheater\\list_cheater";
#save_table(all_names,lnk)
all_names = load_table(lnk)
all_cheater = []

print(all_names)
"""token = "lip_HfTQrYNvMvmtE2pfcjjn"

session = berserk.TokenSession(token)
client = berserk.Client(session=session)

print("Taille :",len(all_names))
print("")

for i in range(1,len(all_names)+1):

    ps = all_names[i-1]
    
    print(str(i)+"-checking",ps+"...")
    result = checkIfPlayerIsCheaterNow(ps,client)
    if result==True:
        all_cheater.append([ps,i-1])
    print("")

"""

