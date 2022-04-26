import math


class WordleDir:
    
    def __init__(self,words):

        self.words = words
        self.bestword = ""
        self.all_infos = []

        self.number = 0
        self.prec = -1

        self.data = [];
    
    def __generate_infos(self,tested_wd,wd_to_find):
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

    def __word_is_in(self,infos,tested_wd,act_wd):

        yelw_ltr = []
        yelw_ltr_ap = []

        the_ltr = []
        ltr_ap = []

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
                        
                    if tested_wd[ltr_id]==act_wd[ltr_id]:
                        return False
            elif ltr_infos == 1:

                if not(ltr in the_ltr):
                    the_ltr.append(ltr)
                    ltr_ap.append(1)
                else:
                    id_ltr = the_ltr.index(ltr)
                    ltr_ap[id_ltr]+=1
                
                if not(ltr in yelw_ltr):
                    yelw_ltr.append(ltr)
                    yelw_ltr_ap.append(1)
                else:
                    idx = yelw_ltr.index(ltr)
                    yelw_ltr_ap[idx]+=1

                if ltr in act_wd:
                    if ltr == act_wd[ltr_id]:
                        return False
                else:
                    return False
            elif ltr_infos == 2:
                if act_wd[ltr_id]!=ltr:
                    return False

                if not(ltr in the_ltr):
                    the_ltr.append(ltr)
                    ltr_ap.append(1)
                else:
                    id_ltr = the_ltr.index(ltr)
                    ltr_ap[id_ltr]+=1

        for ltr_yl_id in range(0,len(yelw_ltr)):
            if act_wd.count(yelw_ltr[ltr_yl_id])<yelw_ltr_ap[ltr_yl_id]:
                return False

        for ltr_ap_id in range(0,len(the_ltr)):
            if act_wd.count(the_ltr[ltr_ap_id])<ltr_ap[ltr_ap_id]:
                return False
            elif act_wd.count(the_ltr[ltr_ap_id])>ltr_ap[ltr_ap_id]:
                for i in range(0,len(infos)):
                    if infos[i]==0 and tested_wd[i]==the_ltr[ltr_ap_id]:
                        return False

        return True

    def calculateI(self,x):
        return  (-1)*math.log10(x)/math.log10(2)

    def generateAllInfos(self):

        for wd in self.words:
            for wd2 in self.words:
                infos = self.__generate_infos(wd2,wd)

                if not infos in self.all_infos:
                    self.all_infos.append(infos)

    def __calculateEnthropie(self,word,all_infos):

        all_infos_used = len(all_infos)
        
        enthropie = 0;

        for select_infos in all_infos:
            reste = 0
            for wd in self.words:
                if self.__word_is_in(select_infos,word,wd):
                    reste+=1
            if reste!=0:
                qt_reste = reste/len(self.words)
                i = self.calculateI(qt_reste)*qt_reste;
                enthropie+=i
            else:
                all_infos_used-=1

        return (enthropie)

    def process_wd(self,tab,affich):

        for wd_ in tab:

            act_entr = self.__calculateEnthropie(wd_,self.all_infos);
            
            self.data.append([wd_,act_entr])

            if affich:

                prc_act = self.__pourcentage(self.number,len(self.words));

                if prc_act!=self.prec:
                    self.prec = prc_act
                    print("Pourcentage :",str(prc_act)+"%")
                
                self.number+=1
    
    def __pourcentage(self,vl_act,tot):
        return int(100*vl_act/tot);

    def __getHighest(self,data_):

        hg = [-1,-1];

        for dt in data_:
            if dt[1]>hg[1]:
                hg = dt;
    
        return hg

    def getReste(self,tab = False,infos = None,mot = None):
        reste = []
        tab_wk = self.words
        
        if tab!=False:
            tab_wk=tab

        for wd in tab_wk:
            if self.__word_is_in(infos,mot,wd):
                reste.append(wd)
        return reste

    def start(self,display_pourc = True,precision=False):

        self.number = 0
        self.prec = -1

        if len(self.all_infos)==0 or precision:
            self.generateAllInfos()
        
        self.process_wd(self.words,display_pourc)

        return self.__getHighest(self.data)

    def foundMot(self,mot):
        all_words_prob = self.words
        words_used = []

        words_used.append(self.bestword)

        while len(words_used)<10 and mot!=words_used[-1]:

            """print("Already used :",len(words_used),"mot(s)")
            print("Mots restant :",len(all_words_prob),"mots")"""

            les_infos_act = self.__generate_infos(words_used[-1],mot)
            all_words_prob = self.getReste(all_words_prob,les_infos_act,words_used[-1])

            wd = WordleDir(all_words_prob)
            wd.all_infos = self.all_infos
            mot_act = wd.start(display_pourc=False)[0]

           #print(words_used)

            words_used.append(mot_act)

        return words_used
