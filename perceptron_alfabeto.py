from Perceptron import Perceptron

if __name__ == "__main__" :

    percy0 = Perceptron(25)
    percy1 = Perceptron(25)
    percy2 = Perceptron(25)
    percy3 = Perceptron(25)
    percy4 = Perceptron(25)

    pad = [[1, 1, 1, 1, 1,
            1, 0, 0, 0, 1,
            1, 1, 1, 1, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1],
           [0,0,0,0,0]
           [1, 1, 1, 1, 1,
            0, 0, 1, 0, 0,
            0, 0, 1, 0, 0,
            0, 0, 1, 0, 0,
            0, 0, 1, 0, 0]
            ]

    res_esperado = [0,1] 
    print(percy0.w)
            
    percy0.treinar(pad, res_esperado)
    print(percy0.w)

    print("Y: " + str(percy0.y([1, 1, 1, 1, 1,
                                1, 0, 0, 0, 1,
                                1, 1, 1, 1, 1,
                                1, 0, 0, 0, 1,
                                1, 0, 0, 0, 1])))
    print("Y: " + str(percy0.y([1, 1, 1, 1, 1,
                                0, 0, 1, 0, 0,
                                0, 0, 1, 0, 0,
                                0, 0, 1, 0, 0,
                                0, 0, 1, 0, 0])))

#    print("Y: " + str(percy.y([0, 1])))
#    print("Y: " + str(percy.y([1, 0])))
#    print("Y: " + str(percy.y([1, 1])))
