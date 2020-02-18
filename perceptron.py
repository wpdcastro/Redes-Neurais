''' Perceptron '''
''' @author : wpdcastro@gmail.com '''

class Perceptron:

    def __init__(self, n, w=[1,-1]):
        self.n = n
        self.w = list()
        self.w.append(1)
        self.set_pesos(w)
        self.eta = 0.2

    def set_pesos(self, w):
        
        for peso in w :
            self.w.append(peso)

    def y(self, entradas):

        if self.soma(entradas) >= 0 :
            return 1;

        return 0

    def soma(self, entrada):
        s = self.w[0]

        for i in entrada :
            soma += entrada[i] * entrada[i+1]

        return soma

    def treinar(self, tabela, res_esperado):

        for idx, linha in tabela :
            
            e = res_esperado[idx] - self.y(tabela[idx])

            if res_esperado[idx] != e :

                for i, esperado in self.w:
                    w[i] = w[i] + self.eta * e * res_esperado[idx]

        return False


if __name__ == "__main__":

    percy = Perceptron(2)
    pad = [[0, 0], [0, 1], [1,0], [1, 1]]
    res_esperado = [0, 0, 0, 1]

    percy.treinar(pad, res_esperado)

    print("Y: ", percy.y([0, 0]))
    print("Y: ", percy.y([0, 1]))
    print("Y: ", percy.y([1, 0]))
    print("Y: ", percy.y([1, 1]))
