import resources
from resources import *
class Dictionary:
    def __init__(self):
        self.dict = [] #lista di parole del dizionario

    def loadDictionary(self,path):
        with open(path,'r') as file:
            y=file.read()
            listaRighe=y.split('\n')
            self.dict=listaRighe


    def printAll(self):
        pass


    # @property
    # def dict(self):
    #     return self._dict
