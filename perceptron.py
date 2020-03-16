import random

class Perceptron:

    def __init__(self, n, w=[1,-1]):
        # n = numero de entradas
        self.n = n
        # w = numero de pesos
        self.w = list()
        self.w.append(1)
        self.eta = 0.2

        for i in range(n) :
            valor = random.randint(0,1) 
            self.w.append(valor)    

    def soma(self, entrada):
        
        soma = self.w[0]

        for idx in range(1, len(self.w)) :

            soma += entrada[idx-1] * self.w[idx]

        return soma

    def y(self, entradas):

        if self.soma(entradas) >= 0 :
            return 1;

        return 0

    def treinar(self, tabela, res_esperado):

        temErro = True
        etapa = 0

        while(temErro and etapa <= 10000):

            temErro = False
            
            for idx in range (0, len(tabela)) :
                
                etapa = etapa + 1

                e = res_esperado[idx] - self.y(tabela[idx])

                if e != 0 :
                    
                    temErro = True  

                    self.w[0] = self.w[0] + self.eta * e

                    for i in range(1,len(self.w)):

                        self.w[i] = self.w[i] + self.eta * e * tabela[idx][i-1]
  

        return False