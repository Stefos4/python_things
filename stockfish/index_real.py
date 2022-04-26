from stockfish import Stockfish

def game_ended(st,nbr_move):
    if st.get_wdl_stats()==None:
        return True
    elif nbr_move>=120:
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

if __name__ =="__main__":
    
    stockfish = Stockfish("C:\\Users\\HP\\Desktop\\chess\\stockfish_14.1_win_x64_popcnt.exe",
    parameters={"Threads": 4, "Minimum Thinking Time": 5000})
    stockfish.set_fen_position("2kr3r/pbppq3/1p2p3/n1P2ppp/3P4/2P1PNP1/2Q1BPP1/R3K2R w KQ - 0 17")
    stockfish.set_depth(25)
    print("*******Evalutation au début :",aff_ev(stockfish.get_evaluation()))
    print("")

    moves = []

    nbr_mv = 0
    add_mv = True

    while not(game_ended(stockfish,nbr_mv)):

        best_move = stockfish.get_best_move()
        moves.append(best_move)
        stockfish.make_moves_from_current_position([best_move])

        if add_mv:
            nbr_mv+=1
            print("-Nbr_move :",nbr_mv)
            print("Evalutation :",aff_ev(stockfish.get_evaluation()))
            print("")

        add_mv = not(add_mv)

    print(stockfish.get_board_visual())
