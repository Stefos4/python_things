import chess.pgn
import pickle
import berserk

games = open("C:\\Users\\HP\\Desktop\\programmation\\python\\test_pgns_openning\\eco.pgn")

cont = 1
size = 0;

game = chess.pgn.read_game(games)

while game!=None:
    black = ""
    try:
        black = " - "+game.headers["Black"]
    except:
        pass
    print(game.headers["White"]+black)
    size+=1
    game = chess.pgn.read_game(games)
print(size)
