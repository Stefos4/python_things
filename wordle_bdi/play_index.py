from Wordle import Wordle
from WordleDir import WordleDir
import kirundi


def play_ijambo(words):
    reste = words
    last_word = "abira"

    for _ in range(0,10):

        wd = WordleDir(reste)
        
        infos = [int(nbr) for nbr in list(input("Entrez les infos pour '"+last_word+"' : "))]
        
        if infos.count(2)==5:
            break

        reste = wd.getReste(infos=infos,mot=last_word)

        # print(" -Nombre de reste sur",len(wd.words),"mots :",len(reste),"mots")
        
        if len(reste)!=0:
            wd = WordleDir(reste)
            print(" Recherche dans",len(reste),"mots..")
            last_word = wd.start(display_pourc=False)[0]

            print("")
            print("Essayez celui ci :",last_word)
        else:
            print("Oups, nous n'avons pas pu trouver ce mot")
            break

def traitementOfWords(tb):
    act_wd = tb
    i = 0
    while i<len(act_wd):
        
        vl = act_wd[i]

        if act_wd.count(vl)>1:
            while act_wd.count(vl)>1:
                act_wd.pop(act_wd.index(vl))
            i = -1
        
        if len(vl)!=5:
            act_wd.pop(act_wd.index(vl))
            print(len(vl),'"'+vl+'"')


            i = -1
        
        i+=1
    
    return act_wd

words = kirundi.mots

if __name__== "__main__":

    words = kirundi.mots
    words = traitementOfWords(words);

    play_ijambo(words)