from Perceptron import Perceptron

if __name__ == "__main__":

    percy0 = Perceptron(25)

    pad = [[1, 1, 1, 1, 1,
            1, 0, 0, 0, 1,
            1, 1, 1, 1, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1],
           [1, 1, 1, 1, 1,
            0, 0, 1, 0, 0,
            0, 0, 1, 0, 0,
            0, 0, 1, 0, 0,
            0, 0, 1, 0, 0]
            ]

    res_esperado = [0,1] 

    resposta = { 0 : 'Letra A', 1 : 'Letra T'}
            
    percy0.treinar(pad, res_esperado)

    res0 = percy0.y([1, 1, 1, 1, 1,
                     1, 0, 0, 0, 1,
                     1, 1, 1, 1, 1,
                     1, 0, 0, 0, 1,
                     1, 0, 0, 0, 1])

    res1 = percy0.y([1, 1, 1, 1, 1,
                     0, 0, 1, 0, 0,
                     0, 0, 1, 0, 0,
                     0, 0, 1, 0, 0,
                     0, 0, 1, 0, 0])

    print("Y: " + resposta[res0])
    print("Y: " + resposta[res1])


