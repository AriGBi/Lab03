import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        start=time.time()
        txtFin=replaceChars(txtIn).lower()
        MultiDiz=md.MultiDictionary()
        MultiDiz.printDic(language)
        lista=MultiDiz.searchWordDichotomic(txtFin, language)
        stringa=""
        for word in lista:
            if word.corretta is False:
                stringa+=f"{str(word)}\n"
        print("Using contains")
        end=time.time()
        print(stringa)
        print(end-start)



    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars="\\'*{}[]()>#+-.!<$%^;,="
    for c in chars:
        text = text.replace(c, "")
    return text
