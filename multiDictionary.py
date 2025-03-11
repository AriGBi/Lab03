import dictionary as d
import richWord as rw
import resources as r
from resources import *

class MultiDictionary:

    def __init__(self):
        self.multiDiz={}


    def printDic(self, language): #uso questa per fare loadDictionary avendo la lingua
        if language == "english":
            dizEng=d.Dictionary()
            dizEng.loadDictionary("resources/English.txt")
            self.multiDiz["english"]=dizEng.dict

        if language == "italian":
            dizIta=d.Dictionary()
            dizIta.loadDictionary("resources/Italian.txt")
            self.multiDiz["italian"]=dizIta.dict

        if language == "spanish":
            dizEsp=d.Dictionary()
            dizEsp.loadDictionary("resources/Spanish.txt")
            self.multiDiz["english"]=dizEsp.dict
        pass

    def searchWordLinear(self, words, language):
        parole=words.split(" ") #lista con tutte le parole
        dizTrovato= self.multiDiz[language]
        lista=[]
        for parola in parole:
            if parola in dizTrovato:
                rich= rw.RichWord(parola)
                rich.corretta=True
                lista.append(rich)

            else:
                rich = rw.RichWord(parola)
                rich.corretta=False
                lista.append(rich)
        return lista

    def searchWordDichotomic(self,words,language):
        parole = words.split(" ")  # lista con tutte le parole
        dizTrovato = self.multiDiz[language]
        lista=[]
        inizio=0
        fine=len(dizTrovato)
        for parola in parole:
            parolaTrovata=False

            while inizio <= fine:
                meta= (inizio + fine)//2
                parola_centrale = dizTrovato[meta]
                if parola_centrale==parola:
                    parolaTrovata=True
                    break

                elif parola_centrale<parola:
                    inizio=meta+1

                else:
                    fine=meta-1

            rich = rw.RichWord(parola)
            rich.corretta = parolaTrovata
            lista.append(rich)
        return lista





