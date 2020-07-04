class Disciplina:
    def __init__(self, dicio):
        self.nome=dicio['nome']
        self.ch=dicio['ch']
        self.uni=dicio['uni']
        self.cod=dicio['cod']
        self.pre=self.liga(dicio['pre'])
        self.filha=set()
        
            
    def liga(self, listaPre):
        self.pre=[]
        if listaPre[0]:
            for x in listaPre:
                self.pre.append(colecao[x])
                colecao[x].filha.add(self)
        else:
            self.pre.append(None)
        return self.pre
        
            
    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.__str__()

def printf(string):
    print(string, end='')

def lf(string, num):
    return str(string).rjust(num)


def pd():
    print('cod'+ lf('nome', 40)+ lf('lista', 40)+ '                 ', 'ch'+ '   u')
    for z in arquivo.items():
        x=z[0]
        y=z[1]
        printf(x)
        printf(lf(y['nome'], 45))
        printf(lf(y['pre'], 40))
        printf(lf(y['ch'], 10))
        printf('   ')
        printf(y['uni'])
        print()


def AbreArquivo():
    listaLinha=["cod", "nome", "ch", "pre", "semestre", "uni", "sig"]
    with open('gradeporextenso.txt','r', encoding='utf-8') as entrada:
        for linha in entrada:
            dicioLinha=dict()
            linha=linha.strip().split('¬')
            
            #Itera sobre o listaLinha montando o dicionário
            for key, value in zip(listaLinha, linha):
                if key in {'ch', 'semestre', 'uni'}: value=int(value)
                dicioLinha[key]=value

            #Cria o abreviatua
            if dicioLinha['sig']=='*':
                dicioLinha['sig']=dicioLinha['nome']
            
            abreviatura[dicioLinha['sig']]=dicioLinha['cod']

            #Uniformiza a lista de prerequistos
            if dicioLinha['pre'] == 'não tem':
                dicioLinha['pre']=[None]
            else:
                dicioLinha['pre']=dicioLinha['pre'].split('|')
                dicioLinha['pre']=[abreviatura[x] for x in dicioLinha['pre']]
            arquivo[dicioLinha['cod']]=dicioLinha
            colecao[dicioLinha['cod']]=Disciplina(dicioLinha)

            
    return colecao


arquivo=dict()
colecao=dict()
abreviatura=dict()

AbreArquivo()
#d()

#MC=arquivo['EAD05008'];Mo=Disciplina(MC)
#FAC=arquivo['EAD05004']; F=Disciplina(FAC)
