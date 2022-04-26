import math
import multiprocessing
import threading
import time


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

words = ["indwi","hepfo","inswa","hanze","kandi","ifuro","ijuru","shima","sokwe","idubu","inkwi","nyika","icupa","umuco","rimwe","ndaje","uruvo","kwiga","kumwa","izuba","imana","nitwa","kanje","wanje","ingwa","hinge","indya","ndeka","ingwe","ntaco","nanje","nyina","nanse","nteka","rwacu","zanje","ndiga","vyawe","kunwa","yanje","gusya","ngaho","kwota","namwe","mfise","ndazi","imbwa","mbega","canke","nivyo","vyose","kwoza","ninde","umuti","ibabi","ibuye","ipera","nyoko","ikaze","ubuki","inama","itabi","amase","ivubi","imari","imiti","isazi","igiti","isake","ijana","izosi","idubu",
"imeza","isoko","ifuro","urugi","ikaye","isuka","inuma","isoya","imibu","isaha","ijoro","icayi","ikoti","izuru","itara","icumu","rwose","icari","iziko","ibati","umubu","ivomo","ivoka","icupa","inoti","akazi","bwiza","ipasi","ihasa","ipine","iwabo","iwacu","iwawe","isato","sinzi","ababa","ababi","ababo","abaca","abaco","abacu","abaha","abahe","abaho","abaja","abaje","abami","abana","abane","abari","abasa","abase","abata","abate","abato","abava","abawe","abaye","abayo","abaza","abaze","abazi","abazo","abeho","abera","abere","henda","jamwo","abeyo","ifoto","abeza","hemwe","ipoto","fyina","bwejo","abiba","abica","abice","twote","abiha","abihe","abika","abira","abiri","abita","abiwe","abizi","aboha","aboma","abona","abone","abora","aboro","abuhe","abura","abure","abuza","abuze","acana","acane","aceze","acika","acike","acira","acire","acita","aciwe","aciye","acura","acure","adaha","adani","aduga","aduge","aduha","aduhe","aduza","aduze","afata","afate","afise","afora","agaba","agabe","agaca","agace","agaco","agafi","agafu","agaha","agana","agasa","agase","agasu","agata","agati","agatu","agaya","agema","agena","agene","agera","agere","ageza","ageze","agica","agiha","agira","agire","agiye","agize","agoye","aguha","aguhe","aguma","agume","agura","agure","aguye","ahaba","ahaca","ahaco","ahaha","ahaja","ahako","ahara","ahari","ahava","ahave","ahawe","ahaye","ahayo","ahaze","aheba","ahebe","ahera","aheta","aheza","aheze","ahiga","ahita","ahiwe","ahiye","ahora","ahowe","ahoze","ahuha","ahuje","ahura","ahure","ahuza","ahuze","ajako","ajamu","ajana","ajane","ajayo","ajeyo","akaba","akabi","akabo","akacu","akaga","akago","akaja","akama","akame","akamo","akana","akano","akara","akari","akate","akato","akava","akawa","akayi","akaza","akaze","akazi","akazu","akehe","akeza","akima","akina","akira","akire","akiri","akiva","akiza","akize","akoba","akoma","akora","akore","akoze","akugi","akuki","akuma","akura","akure","akuwe","akuya","akuye","akuza","akuze","amabi","amafa","amafi","amafu","amagi","amaha","amaho","amaja","amaka","amaki","amama","amamo","amano","amara","amare","amase","amaso","amata","amate","amato","amavi","amaza","amaze","amazi","amazu","amena","amera","amere","amero","ameru","amese","ameza","ameze","amezi","amija","amira","amoko","amota","amoya","amoye","amubi","amuca","amufe","amuha","amuhe","amuta","amuzi","anage","anega","anima","anywa","anywe","apana","araba","arabe","araca","araha","araja","araje","araka","arama","arara","arare","arasa","arava","araza","arazi","arega","areka","areke","arera","areza","ariga","ariha","arihe","ariho","ariko","arima","arime","arimu","arira","arire","ariwa","ariwe","ariwo","ariya","ariye","arize","arizi","aroga","arose","arota","aruca","aruha","arura","aruta","aruwe","asaba","asabe","asama","asare","asasa","asesa","asese","aside","asiga","asize","asoma","asome","asosa","asuka","asuke","ataba","ataha","ataho","ataje","atame","atanu","atari","atate","atatu","atava","ataye","ataza","ataze","atazi","ateba","atebe","atega","atema","ateme","atera","atere","atewe","ateye","ateza","ateze","atiha","atize","atoba","atoca","atoka","atona","atora","atore","atoye","atoze","atuka","atuma","atume","atura","atuzi","avayo","avome","avuga","avuge","avuka","avuye","avuza","avuze","awuha","awuhe","ayacu","ayaga","ayahe","ayari","ayasa","ayava","ayawe","ayera","ayiha","ayihe","ayita","ayiwe","azana","azane","azeza","aziha","azihe","azime","azira","azire","aziye","azize","azoba","azobe","azoca","azoce","azoha","azoja","azota","azova","azoza","azoze","azuka","azura","azuwe","babwo","bagwa","bagwe","bambe","bampa","bamve","bamwe","bamye","bande","bandi","banga","banje","banka","banse","bansi","banta","bantu","banyu","banza","banzi","bapfa","bapfe","barya","barye","baryo","basya","bavyo","bazwi","benda","benga","berwa","besha","bicwa","bicwe","bigwa","bimba","bimwa","bimwe","bimye",
"binca","bindi","bintu","binza","bipfa","bipfe","bipfu","birya","birye","bisha","bishe","biswe","bitwa","bitwe","bizwi","bompi","bonda","bonsa","bonta","bopfa","bosha","boshe","bozwe","bugwa","bukwi","bumba","bumva","bumve","bumwe","bundi","bunge","buntu","bunze","bupfu","burya","buryo","busha","busho","bwaba","bwabe","bwabo","bwaca","bwaco","bwacu","bwaho","bwaje","bwako","bwama","bwame","bwami","bwana","bwari","bwato","bwawa","bwawe","bwawo","bwayo","bwaze","bwazo","bwera","bwica","bwije","bwira","bwire","bwite","bwiwe","bwiye","bwiza","bwoba","bwoca","bwoko","bworo","bwose","bwoya","bwoye","cabwo","cakwe","camwa","camye","canga","canje","canke","canyu","carwo","caryo","catsi","catwo","cavyo","cenda","cezwa","cezwe","cicwa","cigwa","ciswe","citwa","citwe","civye","combo","conze","cumba","cumve","cumye","cunga","dunda","dupfa","dupfe","dutwe","duzwa","egeka","egera","egoda","egome","ekada","emera","emere","emeza","erega","ereka","ereke","erura","fanta","fasha","fatwa","fonda","fukwa","funga","futwa","fuvya","fyeta","fyete","fyine","fyura","gahwa","ganza","gasho","gaswi","gatwe","genda","gende","gipfa","gipfe","gipfu","girwa","girwe","gizwe","gomba","gonda","twize","gubwa","gukwa","gumya","gumye","gupfa","gurwa","gusha","gutwi","akine","gutya","nsabe","ewana","ugeme","gutyo","gwama","iriza","gwara","uyaze","ndase","gwira","nsare","yemye","gwiwe","gwiza","gwize","hagwa","hagwe","hakwa","hamwa","hamwe","handa","hande","handi","hanga","hange","hanje","hantu","hanyu","hanze","hapfa","hapfe","harya","haryo","havyo","hemba","hembe","hesha","heshe","hicwa","hicwe","hinga","hinge","hirwa","hirya","hiswe","hitwa","hitwe","homba","hombe","hompi","honda","honye","hoshi","hukwa","hunga","hunge","huvya","hwata","ibaba","ibabe","ibabi","ibaca","ibaha","ibahe","ibaho","ibaje","ibama","ibane","ibani","ibara","ibata","ibati","ibavu","ibaye","ibaze","ibega","ibeho","ibeko","ibeni","ibera","ibere","ibete","ibeyi","ibeze","ibiba","ibibi","ibica","ibice","ibicu","ibido","ibifi","ibigo","ibihe","ibija","ibika","ibiki","ibiri","ibiro","ibisa","ibise","ubufu","ibisi","ihane","nyiba","ibita","ibiti","nitwe","ibiva","ibivi","nyike","twige","uduki","ibivu","ibiza","ibobo","iboma","ibona","vyoze","bonse","ibone","akubu","amufe","isema","urota","uwota","zande","zipfe","urera","kanda","yande","zanse","tamwo","ibowa","ibuha","ibuka","urote","jamwo","isusa","kuvyo","ibura","kwina","iburi","isope","shure","pompa","ndaho","ibuye","ibuze","icago","icaha","icahi","icana","icara","icari","icasa","icava","icawe","icayi","icayo","icema","icera","iceri","icese","icete","iceyi","icibo","icika","icike","icira","iciro","iciye","iciza","icoba","icobo","icogo","icubi","icuka","icuma","icumi","icumu","icupa","icuya","ideni","idini","idiri","idubu","iduga","iduha","iduhe","iduka","iduza","ifata","ifate","ifazi","ifeke","ifero","ifeza","ifira","ifise","ifuhe","ifuku","ifuni","ifuro","ifuru","ifuti","igaba","igabo","igaha","igana","igapo","igari","igasa","igata","igawa","igayi","igera","igesa","igeza","igeze","igezi","igica","igice","igico","igicu","igifi","igihe","igiki","igira","igire","igisa","igisu","igiti","igito","igiye","igize","igono","igoti","igoye","igufa","igugu","iguhe","iguma","igume","iguye","ihana","ihani","ihari","ihasa","ihawe","iheba","ihema","ihene","ihera","ihere","ihero","iheze","ihiga","ihina","ihire","ihita","ihiye","ihoze","ihuba","ihuna","ihuri","ihuye","ihuza","ijage","ijana","ijayo","ijigo","ijipo","ijoro","ijuru","ikaba","ikaja","ikara","ikaro","ikata","ikava","ikawa","ikaye","ikayi","ikaza","ikaze","ikazi","ikeba","ikete","ikiba","ikibi","ikica","ikida","ikido","ikigo","ikihe","ikija","ikime","ikiri","ikiro","ikivi","ikiya","ikiye","ikiyo","ikiza","ikize","ikizi","ikofe","ikofi","ikoma","ikomu","ikopi","ikora","ikore","ikori","ikosa","ikoti","ikoze","ikuga","ikuma","ikuta","ikuwe","ikuye","ikuza","ikuze","imana","imara","imari","imayi","imaze","imena","imera","imeri","imero","imeya","imeza","imeze","imibu","imice","imico","imina","imira","imisa","imise","imisi","imiti","imizi","imoko","imota","imoto","imuha","imuhe","imuri","imuva","inabi","inaga","inama","inara","inawe","inazi","indwi","indya","inema","ineza","iniro","inivo","inkwi","inota","inoti","inoye","inoze","inshi","inswa","inswi","insya","insyo","inuma","inusu","inywa","inywe","inzya","ipanu","ipasi","ipawa","ipepu","ipera","ipete","ipima","ipine","ipome","ipori","iraba","irabe","iraga","iragi","iraho","iraje","iraka","irama","irame","irare","iraro","irate","iraye","iraza","irazi","ireha","ireka","ireke","irema","irera","iriba","irica","irido","irigi","irihe","iriho","iriko","irima","iripu","iriri","iriro","iriwe","iriya","iriye","irobe","irobo","iroha","irore","irugu","iruka","irura","iruri","iruta","irute","isaba","isage","isaha","isaho","isahu","isake","isano","isare","isari","isase","isaso","isato","isazi","isefu","isega","iseka","isevu","ishwi","isiha","isima","isiya","isogi","isoko","isoni","isoro","isosa","isosi","isowi","isoya","isugi","isuka","isuku","isumo","isumu","isupu","isura","itaba","itabe","itabi","itabu","itaha","itaje","itako","itama","itanu","itara","itari","itatu","itayi","iteba","itege","iteka","iteke","itera","itere","itewe","iteye","iteza","itike","itima","itiro","itiye","itize","itora","itoto","ituba","ituma","itume","iture","ituro","ituta","ituza","ivana","ivano","ivoka","ivomo","ivubi","ivuga","ivuge","ivuka","ivuna","ivutu","ivuye","ivuza","ivuze","iwabo","iwacu","iwawe","iwayo","iwese","iwita","iwiwe","iyaba","iyabo","iyacu","iyamu","iyari","iyata","iyawo","iyera","iyihe","iyiri","iyita","iyiwe","iyoba","iyugi","izamu","izana","izari","izera","izere","izero","izihe","izija","iziko","izina","iziri","izita","iziwe","iziza","izize","izoba","izobe","izoca","izoha","izoja","izosi","izota","izova","izoza","izuba","izuka","izura","izuri","izuru","jambo","janye","jenda","jisho","kabwa","kabwo","kagwa","kagwi","kakwo","kambi","kampe","kamwe","kandi","kanje","kantu","kanwa","kanya","kanyu","kanzu","karya","karyo","katwa","kavyo","kazwi","kenya","kevya","kibwa","kigwa","kigwi","kimwe","kinda","kindi","kinga","kintu","kinya","kinza","kirya","kitwa","kizwa","kobwa","komwa","kondo","kotwa","kubwa","kugwa","kumbe","kumpa","kumwa","kumwe","tunye","abuzi","bimpe","dukwe","gitwe","kunda","kundi","kunja","kunta","kuntu","kunwa","kunya","kurwa","kurya","mbuza","mpora","ngako","kuryo","kwaba","kwabo","kwaco","kwacu","kwaha","kwaho","kwaje","kwaka","kwama","kwana","kwari","kwawe","kwaya","kwayo","kwaza","kwazo","kwega","kwema","kwera","kweri","kweza","kwezi","kwiba","kwica","kwiga","kwiha","kwima","kwira","kwita","kwiwe","kwiza","kwoba","kwoga","kwoma","kwomu","kwona","kwosa","kwose","kwota","kwuma","kwuta","kwuza","mahwa","majwi","mambo","mambu","mango","manza","mapfa","masho","matwi","mbaha","mbaho","mbara","mbavu","mbaye","mbaza","mbeba","mbega","mbeho","mbera","mbere","mbeyo","mbibe","mbiga","mbika","mbisi","mbizi","mboga","mbohe","mbona","mbone","mboyi","mbuga","mbure","mburi","mbuto","mbuze","menya","menye","menyo","mfata","mfate","mfise","mfura","migwi","minwa","minwe","mitsi","mitwe","mivyi","mpaga","mpaka","mpako","mpama","mpari","mpawe","mpaye","mpeba","mpemu","mpene","mpera","mpeta","mpeze","mpima","mpome","mpore","mpuzu","mugwi","mukwa","mukwe","mumpe","mumve","munsi","muntu","munwa","munwe","munyu","munzi","munzu","mupfa","murya","murye","musha","mushu","mutsi","mutwa","mutwe","mutyo","mvane","mveyo","mviro","mvuga","mvuge","mvugo","mvume","mvuna","mvune","mvura","mvuto","mvuye","mvuze","mwaba","mwaje","mwaka","mwama","mwame","mwami","mwana","mwara","mwari","mwaro","mwava","mweho","mwene","mwera","mwese","mwete","mweze","mwezi","mwica","mwice","mwige","mwiha","mwihe","mwiko","mwira","mwita","mwiyu","mwiza","mwize","mwoba","mwobo","mwoca","mworo","mwoza","mwoze","myaka","myiza","myobo","namba","nambu","nampe","namwe","namye","nanga","mbisa","ndima","nyima","apima","twima","rimpe","ngayo","ngiyo","ngure","nkina","nteka","uroze","usaze","nanje","nanka","nanse","napfe","narye","natwe","navyo","nceho","ncika","ncike","ncire","nciye","ncuna","ncuro","ncuti","ndaba","ndabe","ndaha","ndaja","ndaje","ndara","ndaro","ndata","ndava","ndaza","ndazi","ndeka","ndeke","ndema","ndero","ndeza","ndiba","ndica","ndiga","ndiha","ndiho","ndiko","ndimi","ndimo","ndire","ndiwe","ndiye","ndize","ndobo","ndoga","ndome","ndore","ndosa","ndota","ndoto","nduga","nduge","nduza","nduze","nezwa","ngabo","ngaca","ngaha","ngaho","ngana","ngano","ngazi","ngero","ngeso","ngeze","ngira","ngire","ngiro","ngiye","ngize","ngobe","ngogo","ngoma","ngora","ngoro","ngowe","ngozi","ngufi","nguha","nguhe","nguma","ngume","ngura","nguvu","nguze","nguzi","nicwa","nicwe","nimba","ninde","nirye","nishe","nitwa","nivyo","njana","njane","njemu","ivure","ubuzi","imuka","njeyo","nkaba","nkaja","nkako","nkama","nkana","nkava","nkawe","nkaza","nkeka","nkera","nkeya","nkeyi","nkeza","nkiba","nkike","nkino","nkire","nkiri","nkiva","nkiza","nkize","nkoko","nkoma","nkomu","nkona","nkone","nkoni","nkono","nkora","nkore","nkoro","nkota","nkovu","nkoze","nkozi","nkuka","nkumi","nkura","nkure","nkuru","nkuwe","nkuye","nkuzi","nomye","nonke","nonse","nopfa","norya","nosha","nsaba","nsago","nsasa","nsato","nseko","nsesa","nsome","nsuka","nsuke","ntaba","ntabe","ntabo","ntaca","ntaco","ntahe","ntaho","ntaja","ntaje","ntama","ntara","ntare","ntari","ntata","ntate","ntawe","ntayo","ntaza","ntaze","ntazi","ntebe","ntega","nteko","ntera","ntere","ntete","ntewe","nteye","nteze","ntiba","ntibe","ntiri","ntita","ntiwi","ntiza","ntizo","ntoke","ntora","ntore","ntoye","ntoyi","ntoza","ntuba","ntube","ntuhe","ntuje","ntuka","ntuma","ntume","ntumo","ntura","nturi","ntuve","ntuza","ntuze","ntuzi","numpe","numva","numve","numwe","numye","nunge","nunze","nyaco","nyaho","nyama","nyana","nyawe","nyawo","nyayo","nyene","nyina","nyoko","nyoma","nyoni","nyuma","nyuzi","nzana","nzane","nzara","nzeko","nzero","nzeza","nzige","nzima","nzira","nziza","nzoba","nzobe","nzoca","nzoga","nzoha","nzoja","nzoka","nzota","nzovu","nzoya","nzoza","nzoze","nzuzi","omoka","nkuko","onona","oroha","orora","oyaha","oyaye","panga","pfuma","iyuba","pinda","pinga","ikiba","ponda","pwaro","ramba","rembo","bwuma","renga","igori","renza","rerwa","resha","rigwa","rimwe","rimwo","rinda","rinde","rindi","ripfa","rirya","risha","rizwi","ronga","ronka","rugwa","rugwe","rumbu","rumwe","rundi","runtu","rupfu","rurya","rurye","rusha","rushi","rusyo","rutwe","rwaba","rwabo","rwaca","rwaco","rwacu","rwaho","rwako","rwama","rwame","rwamo","rwana","rwari","rwava","rwawe","honja","rwawo","rwaya","rwayo","rwazo","rwego","rweru","rwimo","rwire","rwiri","rwiwe","rwiza","rwoba","rwose","rwuba","rwuma","rwume","ryaba","ryabo","ryaco","ryacu","ryaga","ryaho","ryaje","ryaka","ryama","ryari","ryava","icuba","ryawe","ryawo","nyica","nzica","ryayo","ryazo","ryera","ryica","ryiha","mpeka","ryoha","ryiwe","ryiza","ryoba","ryoca","ncira","icova","nsiga","vyina","nkuyo","ryomu","ryose","sabwe","sanga","senga","senge","senya","shahu","shaka","shano","shavu","shaza","shefu","shehe","shemi","shika","shima","shira","shona","shora","shoza","shura","simba","simbe","sindi","sinje","sinse","sinza","sinze","sinzi","sivyo","sokwe","songa","sonza","sukwa","sutwa","tamba","tanga","tangi","tanya","temba","tenga","terwa","tevya","timba","tinda","tinya","tonda","tonde","tongo","tonya","torwa","tubwa","tugwe","tugwi","tukwa","tundi","tunga","turya","turye","tutsi","twaba","twabo","twaco","twaho","twaje","twama","twame","twara","twari","twawe","twawo","twayo","twazo","tweho","twera","twese","twihe","twita","twiwe","twiza","twoba","twoca","twoge","twoha","twoje","twose","twoye","twoze","iyubu","ubace","ubage","ubaha","ubahe","ubaho","ubaka","ubana","ubane","ubate","ubave","ubaye","nyima","mbisa","apima","ndima","upime","ibora","twiga","yimpe","ubaza","ubaze","ubeho","ubera","ubere","ubeyo","ubeze","ubiba","ubibe","ubice","ubihe","ubika","ubike","ubize","ubizi","ubome","ubona","ubone","uboze","ububi","ubugi","ubuhe","ubuho","ubuja","ubuki","ubuku","ubura","ubure","uburi","uburo","ubusa","ubute","ubuto","ubuva","ubuyi","uceze","ucika","ucike","ucira","ucire","uciye","ucura","ucuze","udaca","udide","udufi","uduga","uduge","uduha","uduhe","uduka","uduta","uduti","uduze","ufata","ufate","ufise","ugaca","ugaha","ugana","ugara","ugaya","ugene","ugere","ugeza","ugeze","ugiha","ugihe","ugira","ugire","ugite","ugiye","ugize","ugona","ugoye","uguca","uguma","ugume","ugumu","ugure","uguta","ugute","uguye","uhabe","uhage","uhare","uhari","uhawe","uhaye","uhaza","uhebe","uhema","uheze","uhita","uhoma","uhuha","uhuje","uhura","uhure","uhuye","ujana","ujane","ujemu","ukaba","ukaja","ukama","ukare","ukase","ukava","ukaza","ukaze","ukica","ukina","ukira","ukire","ukiri","ukize","ukome","ukora","ukore","ukoze","ukuba","ukuja","ukuma","genza","ukura","ukure","irori","abize","nanke","ngaba","ukuri","uhaze","ukiza","kanse","anika","ipano","basha","harye","igore","mwiga","mwoga","nyika","ukuva","ukuwe","ukuza","umara","umare","izane","umaze","ibiyo","umera","umere","umeza","umeze","umira","umire","umiye","umota","umube","umubi","umubu","umuce","umuco","umuda","umufa","umuha","umuhe","umuja","umuji","umuma","umuna","umupo","umusi","umuti","umuto","umuvo","imivo","umuza","umuzi","umuzo","unama","unihe","unoze","unuze","unywa","unywe","upima","uraba","urabe","uraca","uraho","izacu","izisa","uraja","uraje","uraka","urama","urara","urare","urava","uraza","urazi","ureha","ureka","ureke","uriga","urihe","uriho","uriko","urima","urira","urire","urite","uriya","uriye","urize","uroba","uroga","urubu","uruda","urufi","urugi","urugo","uruho","uruhu","urujo","urume","ururo","uruta","njeko","uruti","uruvi","uruvo","uruvu","uruyo","uruzi","usaba","usabe","usase","usibe","usiga","usoma","usome","usosa","usuke","utaba","utaha","utahe","utaje","utako","utama","utari","utaza","utazi","uteba","utege","uteka","uteke","uteko","utema","utera","utere","utewe","uteye","uteza","uteze","utiye","utoba","utora","utore","utugo","utuma","utume","utuzi","uvuga","uvuge","uvume","uvuye","uvuza","uvuze","uwaba","uwabo","uwaka","uwama","uwari","uwava","uwawe","uwera","uwiba","uwica","uwiga","uwima","uwita","uwiwe","uwoba","uwoga","uwuba","uwuca","uwuha","uwuhe","uwuja","uwuje","uwuri","uwusa","uwuza","uwuzi","uyage","uyeze","uyiha","uyihe","uyuhe","uzana","uzane","uzihe","uzima","uzime","uzoba","uzoca","uzoce","uzoha","uzoja","uzoje","uzoza","uzoze","uzuke","uzuza","vanga","vinyu","vugwa","vumwa","vyaba","vyabo","vyaca","vyaco","vyacu","vyago","vyaha","vyahi","vyaho","vyaje","vyaka","vyako","vyama","vyana","vyara","vyari","vyaro","vyasa","vyava","vyawe","vyawo","vyaya","vyayo","vyaza","vyazo","vyera","vyeri","vyeze","vyibe","vyica","vyice","vyiha","vyiwe","vyiza","vyoba","vyobo","vyoca","vyoje","vyosa","vyose","vyoza","vyubi","vyuka","vyuma","vyuza","wabwo","wakwo","wampa","wamye","wanje","wanka","wanke","wanse","wanyu","warwo","waryo","watse","wavyo","wibwe","wimwa","wimye","wishe","witwa","wivye","wompa","wonka","wonke","wonse","wonze","wopfa","wosha","wumva","wumve","wumye","wundi","wunga","wunge","wunze","yabwo","yagwa","yakwa","yambi","yambu","yampa","yamye","yandi","yanje","yanka","yanke","yanse","yanyu","yapfa","yarwo","yarya","yaryo","yatsa","yatse","yavyo","yemwe","yezwa","yicwa","yicwe","yimba","yimbe","yimwa","yimye","yindi","yinga","yishe","yiswe","yitwa","yivye","yogwa","yompa","yompi","yonde","yonka","yonsa","yonse","yonze","yopfa","yorwa","yorya","yosha","yozwe","yumva","yumve","yumye","yunga","yunge","yunze","zabwo","zagwa","zanje","zanyu","zarwo","zaryo","zatse","zatwo","zavyo","zicwa","zicwe","zigwa","zigwe","zimba","zimbe","zimpa","zimpe","zimwa","zimwe","zimya","zimye","zindi","zinga","zinge","zinwe","zirya","zirye","zishe","ziswe","zitwa","zompi","zonda","zonde","zonka","zonke","zonsa","zonse","zonye","zonze","zumva","zumve","zumya","zumye","zunga","zunge","zunza","zunze","sombe","bakwe","koshe","icebe","bukwe","inube","konse","onkwa","itugu","kovya","ihebe","kosha","kotse","shoka","shoke","shuha","impfu","isomo","yonke","bonke","bonze","ihute","kobwe","konwe","mpeke","ronke","wotse","yotse","botse","bweru","cotse","hekwa","nkome","ibuke","izuku","mpeko","nkowe","nzuke","ruswa","sabwa","ahica","ankwa","bwake","bwoze","ibuyi","iduge","inuze","komba","korwa","kunde","kwepa","mbese","mbike","mvako","nkase","nkote","nsoma","ntoya","omeka","omoke","orohe","pfuha","pfuka","songe","sunzu","swata","ubuka","ubuti","uduce","uduse","udute","umuse","uriwe","utoye","utubu","uvuke","agora","agowe","aguwe","akiwe","akote","amake","amana","bibwe","bikwe","bimpe","boste","conde","dutsi","gomwe","gonde","gonga","ibida","ibino","idute","ihone","ihore","ikeze","ikijo","ikina","ikino","ikoye","ikure","imote","indye","irisa","irote","isibe","isiza","isobe","ivoma","kamba","kanga","konzi","kubwo","manzi","mobwa","mpita","mvubu","ndaya","ndira","ndohe","ndose","ndoye","ngara","niswe","nsege","nseke","nsobe","nsore","nsoze","ntoze","ntuke","nunwe","nweko","nzigo","nzura","pfuke","ratwa","ratwe","remba","rihwa","samba","sikwo","somba","somwa","tambe","tesha","torwe","tukwe","turwe","twake","tware","ubufi","ucuke","ufuse","ugoje","ugowe","uhiga","uhira","ukeze","ukowe","ukoye","umubo","umute","uruka","urura","urute","usare","useke","usobe","usose","utima","utira","utowe","utoze","utune","uvure","uzobe","vamwo","vyuke","wezwa","wiswe","wonde","worya","yezwe","yimpe","yokwa","yonye","zotse"]

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

























        
