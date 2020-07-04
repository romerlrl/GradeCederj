from tkinter import *
import LeArquivo

def maiorPalavra(string):
    string=string.split(' ')
    return len(max(string))*11
class box:
    def __init__(self, item):
        self.info=item
        self.caixaMaior=Label(Janela, bg='red', width=maiorPalavra(self.info.nome), height=2+self.info.nome.count(' '))
        self.caixa=Button(self.caixaMaior, text=self.info.nome.replace(' ', '\n'), command=self.changeColor)
        self.caixaMaior.place(x=20, y=20)
        self.caixa.place(x=2, y=2)
        if self.info.filha:
            self.fonte=3
    def changeColor(self):
        if self.caixaMaior['bg']=='red':
            self.caixaMaior['bg']='green'
        else:
            self.caixaMaior['bg']='red'
            
materias=LeArquivo.AbreArquivo()
Janela=Tk()
Janela.geometry('200x200+300+300')
x=box(materias['EAD05001'])
Janela.mainloop()

        
