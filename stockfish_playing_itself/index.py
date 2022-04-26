from stockfish import Stockfish
import time

def game_ended(st):
    if st.get_wdl_stats()==None:
        return True
    else:
        return False

def aff_ev(evaluation):
    if evaluation["type"]=="cp":
        try:
            evaluation["value"]/=100
        except KeyError:
            pass
    return evaluation

def getPourc(nbr_mv,max_nbr):
    return int((nbr_mv/max_nbr)*100)

stockfish = Stockfish("C:\\Users\\HP\\Desktop\\chess\\stockfish_14.1_win_x64_popcnt\\stockfish_14.1_win_x64_popcnt.exe",parameters={"Threads": 4, "Minimum Thinking Time": 5000})
stockfish_2 = Stockfish("C:\\Users\\HP\\Desktop\\chess\\stockfish_14.1_win_x64_popcnt\\stockfish_14.1_win_x64_popcnt.exe",parameters={"Threads": 4, "Minimum Thinking Time": 5000})


moves = [];

weak_elo = 2100
strong_depth = 25;

stockfish.set_elo_rating(weak_elo);
stockfish_2.set_depth(strong_depth)

#mv = stockfish.get_best_move();

#print(mv);

turn = True

last_Prc = -1

while not(game_ended(stockfish)):
    
    player = "Weak"

    prc_act = getPourc(len(moves),120)

    words_print = stockfish.get_board_visual();

    if(prc_act!=last_Prc):
        print("Pourcentage : "+str(prc_act)+"%")
        last_Prc = prc_act

    #print(words_print,end="\r")

    if(len(moves)!=0):
        stockfish.set_position(moves)
        stockfish_2.set_position(moves)

    if turn:
        moves.append(stockfish.get_best_move())
    else:
        moves.append(stockfish_2.get_best_move())
        player = "Strong"

    #print(stockfish.get_board_visual(),end="\r")

    #moves.append(stockfish.get_best_move())

    turn = not(turn)

    #print("Turn :",player)

    #print(aff_ev(stockfish.get_evaluation()))

print(stockfish.get_board_visual())

print(moves)

