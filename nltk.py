class Nltk:
    
    str

    def receive(self,str):

        self.str = str
        self.str = self.interpreter()

        self.str = self.str + " - tratado"
        return self.str


    def interpreter(self):
        self.str += " - interpretado" 
        return self.str

nltk = Nltk() 
print(nltk.receive('teste'))
        