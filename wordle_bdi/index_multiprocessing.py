import math
import multiprocessing
import threading
import time
import kirundi


def generate_infos(tested_wd,wd_to_find):
    tab = [0,0,0,0,0]
    founded_ltr = []
    id_fd_ltr = []
    
    for ltr_id in range(0,len(tested_wd)):

        if tested_wd[ltr_id]==wd_to_find[ltr_id]:

            tab[ltr_id] = 2
            founded_ltr.append(tested_wd[ltr_id])
            id_fd_ltr.append(ltr_id)

    for ltr_id in range(0,len(tested_wd)):
        if not(ltr_id in id_fd_ltr):
            ltr = tested_wd[ltr_id]
            if ltr in wd_to_find:
                if not(wd_to_find.count(ltr) == founded_ltr.count(ltr)):
                    nbr_ltr_act = wd_to_find.count(ltr)

                    wrong_placed = 0
                    
                    nbr_times_wr_pl = 0
                    for vl_id in range(0,len(tab)):
                        #print((tab[vl_id]==1 or tab[vl_id]==2))
                        if ((tab[vl_id]==1 or tab[vl_id]==2) and tested_wd[vl_id]==ltr):
                            nbr_times_wr_pl+=1
                            
                    #print(nbr_times_wr_pl,":",ltr,":",ltr_id)

                    if nbr_times_wr_pl<nbr_ltr_act:
                        wrong_placed = 1
                        
                    tab[ltr_id] = wrong_placed

    return tab
            

def word_is_in(infos,tested_wd,act_wd):
    words_not_in = []
    words_in_not_in_that_pos = []
    for ltr_id in range(0,len(tested_wd)):
        ltr_infos = infos[ltr_id]
        ltr = tested_wd[ltr_id]
        if ltr_infos == 0:
            if ltr in act_wd:
                is_in = False

                for vl_id in range(0,len(infos)):
                    act_inf = infos[vl_id]
                    if (infos[vl_id]==1 or infos[vl_id]==2) and ltr==tested_wd[vl_id]:
                        is_in = True
                        break
                
                if not is_in:
                    return False
        elif ltr_infos == 1:
            if ltr in act_wd:
                if ltr == act_wd[ltr_id]:
                    return False
            else:
                return False

    return True

def calculateI(x):
    return  (-1)*math.log10(x)/math.log10(2)

number_ = multiprocessing.Value('i');
number_.value=0

prec_ = multiprocessing.Value('i')
prec_.value = -1


def calculateProb(infos,all_wd,sel):
    nbr_ap=0

    for wd1 in all_wd:
        if generate_infos(wd1,sel)==infos:
            nbr_ap+=1
    
    return nbr_ap/len(all_wd)

def generateAllInfos(all_wd):

    all_infos = []

    for wd in all_wd:
        for wd2 in all_wd:
            infos = generate_infos(wd2,wd)

            if not infos in all_infos:
                all_infos.append(infos)
    
    return all_infos

def calculateEnthropie(word,all_wd):

    all_infos = []
    enthropie = 0;

    for selected in all_wd:
        
        if selected!=word:
            les_infos = generate_infos(word,selected)
            reste = 0
            for wd in all_wd:
                if word_is_in(les_infos,word,wd):
                    reste+=1;

            #print(selected,word,reste,les_infos)
            #time.sleep(0.5)

            #probabilite = calculateProb(les_infos,all_wd,selected)
            qt_reste = reste/len(all_wd)
            i = calculateI(qt_reste) * (1/len(all_wd));

            enthropie+=i

    """lk.acquire()
    data.append([word,enthropie])
    number+=1
    prc_act = pourcentage(nbr,len(words));
    if prc_act!=prec:
        prec = prc_act
        print("Pourcentage :",str(prc_act)+"%",end="\r")

    lk.release()"""

    return enthropie


def calculateEnthropieTwoSteps(word,all_wd):

    all_infos = []
    enthropie = 0;

    for selected in all_wd:
        
        if selected!=word:
            les_infos = generate_infos(word,selected)
            reste = []
            for wd in all_wd:
                if word_is_in(les_infos,word,wd):
                    reste.append(wd)

            for wd2 in reste:
                act_ent = calculateEnthropie(wd2,reste)

            #print(selected,word,reste,les_infos)
            #time.sleep(0.5)

            #probabilite = calculateProb(les_infos,all_wd,selected)
            qt_reste = len(reste)/len(all_wd)
            i = calculateI(qt_reste) * (1/len(all_wd));

            enthropie+=i


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

def pourcentage(vl_act,tot):
    return int(100*vl_act/tot);

def getEntr(data_,nom):
    for dt_id in range(0,len(data_)):
        if data_[dt_id][0]==nom:
            print(data_[dt_id])
            break

def getHighest(data_):

    hg = [-1,-1];

    for dt in data_:
        if dt[1]>hg[1]:
            hg = dt;
    
    print(hg);

words = kirundi.mots



def process_wd(tab,lk,data,number,prec,all_vl):

    for wd_ in tab:

        act_entr = calculateEnthropie(wd_,all_vl);

        lk.acquire()
        
        data.append([wd_,act_entr])
        prc_act = pourcentage(number.value,len(all_vl));

        if prc_act!=prec.value:
            prec.value = prc_act
            #print("vl :",number.value)
            print("Pourcentage :",str(prc_act)+"%")
        
        number.value+=1

        lk.release()


if __name__== "__main__":

    words = words[:400]

    words = traitementOfWords(words);

    #words = ["tarie","paris","parie","tapis","gosse","tarif","mamie"]

    print("long",len(words))
    

    manager = multiprocessing.Manager()
    data = manager.list();

    lock = multiprocessing.Lock();

    size = int(len(words)/3)

    limits = [size,size*2,len(words)]

    #print(limits)
        
    t1 = multiprocessing.Process(target=process_wd,args=(words[:limits[0]],lock,data,number_,prec_,words,));
    t2 = multiprocessing.Process(target=process_wd,args=(words[limits[0]:limits[1]],lock,data,number_,prec_,words,));
    t3 = multiprocessing.Process(target=process_wd,args=(words[limits[1]:limits[2]],lock,data,number_,prec_,words,));
    
    t1.start();
    t2.start();
    t3.start();

    t1.join()
    t2.join()
    t3.join()


    # #print(highest)

    getHighest(data)

    #infosss = generateAllInfos(words)
    #print(len(infosss))

























        
