from Perceptron import Perceptron

if __name__ == "__main__" :

    percy0 = Perceptron(2)
    percy1 = Perceptron(2)

    pad = [
        [0,0],
        [0,1],
        [1,0],
        [1,1],
    ]
    
    res_desejado0 = [0, 1, 1, 1]
    res_desejado1 = [1, 1, 1, 0]

    percy3 = Perceptron(2)

    pad1 = [ [0,1],
        [1,0],
        [1,1],
    ]

    res_desejado3 = [0, 0, 1]

    percy0.treinar(pad, res_desejado0)
    percy1.treinar(pad, res_desejado1)
    percy3.treinar(pad1, res_desejado3)

    entradas = [ [0,0], [0,1], [1,0], [1,1] ]

    for entrada in entradas: 

        x1 = percy0.y(entrada)
        x2 = percy1.y(entrada)
        x3 = percy3.y([x1, x2])

        print('[ x1 = ' + str(x1) + ' , x2 = ' + str(x2) + '] => x3 = ' + str(x3))