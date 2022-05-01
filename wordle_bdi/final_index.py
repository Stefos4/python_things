from Wordle import Wordle
from WordleDir import WordleDir
import random
import pickle
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

def getMoyenne(wd,verbose=True):

    moy_table = []

    moy = 0
    n = 0

    for lg in words:

        n+=1

        moot = lg
        if verbose:
            print("Find",moot)
        
        etap = wd.foundMot(moot)
        moy+=len(etap)

        moy_table.append(moy/n)

        #clear()

        if verbose:
            print(etap)
            print("Nouvelle moyenne :",moy/n)
            print("nbr :",n)
            print("")
    
    return moy_table

def saveMoyenne(link,data_moy):
    with open(link,"wb") as data_file:
        pickle.dump(data_moy,data_file)

def loadMoyenne(folder,name):
    with open(folder+"\\"+name,"rb") as data:
        return pickle.load(data)

def generateAndSaveMoy(wordle,name,path):
    wordle.bestword = name
    abs_path = path+wd.bestword
    saveMoyenne(abs_path,getMoyenne(wordle,verbose=False))

clear = lambda: os.system('cls')

words = kirundi.mots


if __name__== "__main__":

    #words = words[:300]

    link = "C:\\Users\\HP\\Desktop\\programmation\\python\\wordle_bdi\\moy_saves\\"

    words = traitementOfWords(words);

    print("Long :",len(words),"mots")

    wd = WordleDir(words)

    wd.bestword = "umubu"

    wd.generateAllInfos()


    #print(wd.start())
    #play_ijambo(words)

    words2 = words.copy()
    random.shuffle(words2)

    """table_alr = ["umubu"]

    for wd_mt in table_alr:
        generateAndSaveMoy(wd,wd_mt,link)

    for wd_mt in words2:
        if not(wd_mt in table_alr):
            print("-Ok",wd_mt)
            generateAndSaveMoy(wd,wd_mt,link)"""

    print(getMoyenne(wd,verbose=True))

    #print(loadMoyenne(link,wd.bestword))