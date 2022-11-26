from ia import Ia

class Nltk:
    
    str
    
    def __init__(self,str = ""):

        self.str = str

    def receive(self,str):

        self.str = str
        self.interpreter()
        self.str += " - tratado"
        return self.send()

    def send(self):
        return self.str

    def interpreter(self):

        self.str += " - interpretado" 

    
    def calc(self):
        print(Ia.say_hello())
        print(Ia.calc())
