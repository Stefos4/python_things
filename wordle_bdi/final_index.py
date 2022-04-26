from Wordle import Wordle
from WordleDir import WordleDir
import random
import kirundi
import english
import time
import os

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

def play_ijambo(words):
    reste = words
    last_word = "ibera"

    for _ in range(0,5):

        wd = Wordle(reste)
        
        infos = [int(nbr) for nbr in list(input("Entrez les infos pour '"+last_word+"' : "))]
        reste = wd.getReste(infos=infos,mot=last_word)

        print(" -Nombre de reste sur",len(wd.words),"mots :",len(reste),"mots")
        print(" -Entropy :",wd.calculateI(len(reste)/len(wd.words)))
        
        wd = Wordle(reste)
        print(" Recherche dans",len(reste),"mots..")
        last_word = wd.start(display_pourc=False)[0]

        print("")
        print("Essayez celui ci :",last_word)

def getMoyenne(wd):

    moy = 0
    n = 0

    for lg in words:

        n+=1

        moot = words[random.randint(0,len(words)-1)]
        moot = lg
        print("Find",moot)
        etap = wd.foundMot(moot)
        moy+=len(etap)
        
        clear()

        print(etap)
        print("Nouvelle moyenne :",moy/n)
        print("nbr :",n)
        print("")

clear = lambda: os.system('cls')

words = kirundi.mots


if __name__== "__main__":

    #words = words[:500]

    words = traitementOfWords(words);

    print("Long :",len(words),"mots")

    wd = WordleDir(words)
    wd.bestword = "ibera"
    wd.generateAllInfos()
    time_av = time.time()
    #print(wd.start())
    print("Temps :",str(time.time()-time_av))

    #play_ijambo(words)

    getMoyenne(wd)