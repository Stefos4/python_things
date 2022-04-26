"""from selenium import webdriver

#link = "C:\\Users\\HP\\Desktop\\programmation\\stuff\\edgedriver_win64"
#link = "C:/Users/HP/Desktop/programmation/stuff/edgedriver_win64"
link = "C:\\Users\\HP\\Desktop\\programmation\\stuff\\edgedriver_win64\\msedgedriver.exe"
browser = webdriver.Edge(link)"""

from Wordle import Wordle
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
import kirundi

def getCasePath(l,c):
    return '/html/body/div/div/div[2]/div['+str(l)+']/div['+str(c)+']'

def getCasePathBtn(ltr):
    return "//button[text()='"+ltr+"']"

def getCaseColor(l,c,bw):

    class_vls = ["w-14 h-14 border-solid border-2 flex items-center justify-center mx-0.5 text-4xl font-bold rounded dark:text-white absent shadowed bg-slate-400 dark:bg-slate-700 text-white border-slate-400 dark:border-slate-700",
                 "w-14 h-14 border-solid border-2 flex items-center justify-center mx-0.5 text-4xl font-bold rounded dark:text-white present shadowed bg-yellow-500 text-white border-yellow-500",
                 "w-14 h-14 border-solid border-2 flex items-center justify-center mx-0.5 text-4xl font-bold rounded dark:text-white correct shadowed bg-green-500 text-white border-green-500"]
    
    path = getCasePath(l,c)
    el = bw.find_element(by=By.XPATH, value=path)
    class_vl = el.get_attribute("class")

    return class_vls.index(class_vl)

def writeWd(wd,bw):
    for ltr in wd:
        pt = getCasePathBtn(ltr.upper())
        btn = browser.find_element(by=By.XPATH, value=pt)
        btn.click()

def getInfos(bw,ligne):
    infos = []
    for i in range(1,6):
        cl = getCaseColor(ligne,i,bw)
        infos.append(cl)
    return infos

def hitEnter(bw):
    pt = getCasePathBtn("KWEMEZA")
    btn = bw.find_element(by=By.XPATH, value=pt)
    btn.click()

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

if __name__=="__main__":
    words = traitementOfWords(words);

    link = "C:\\Users\\HP\\Desktop\\programmation\\stuff\\edgedriver_win64\\msedgedriver.exe"
    ser = Service(link)
    op = webdriver.EdgeOptions()

    browser = webdriver.Edge(service=ser, options=op)

    browser.get("https://www.ijambo.app")
    browser.maximize_window()

    croix_path = '/html/body/div[2]/div/div/div/div[2]/div[1]'
    croix = browser.find_element(by=By.XPATH, value=croix_path)
    croix.click()


    act_word = "ibera"
    reste = words

    writeWd(act_word,browser)
    hitEnter(browser)

    for i in range(2,7):
        time.sleep(2)
        les_infos = getInfos(browser,i-1)
        #print(les_infos)
        if les_infos.count(2)<5:
            wd = Wordle(reste)
            reste = wd.getReste(infos=les_infos,mot=act_word)
            wd = Wordle(reste)
            act_word = wd.start(display_pourc=False)[0]
        
            writeWd(act_word,browser)
            hitEnter(browser)
        else:
            break





