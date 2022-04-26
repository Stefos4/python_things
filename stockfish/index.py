from stockfish import Stockfish
import time

def getWords(sec):
    if sec>=60:
        min_ = int(sec/60)
        sec_ = sec - min_*60
        print("-Temps :",min_,"minutes",sec_,"secondes")
    else:
        print("-Temps :",sec,"secondes")

stockfish = Stockfish("C:\\Users\\HP\\Desktop\\chess\\stockfish_14.1_win_x64_popcnt\\stockfish_14.1_win_x64_popcnt.exe",parameters={"Threads": 4, "Minimum Thinking Time": 5000})
stockfish.set_fen_position("rn2k1nr/p1p2p2/Pp6/7p/6pP/5bP1/5P1K/3q4 w kq - 0 25")
stockfish.set_depth(30)
print(stockfish.get_board_visual())


time_av = time.time()

print("-best move :",stockfish.get_best_move())
stockfish.make_moves_from_current_position([stockfish.get_best_move()])
print(stockfish.get_board_visual())
print("-best move :",stockfish.get_best_move())
evaluation = stockfish.get_evaluation()
if evaluation["type"]=="cp":
    try:
        evaluation["value"]/=100
    except KeyError:
        pass

time_apr = time.time()
getWords(time_apr-time_av)

print(evaluation)
print(stockfish.get_wdl_stats())
print("")
