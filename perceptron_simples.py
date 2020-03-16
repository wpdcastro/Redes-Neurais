from Perceptron import Perceptron

if __name__ == "__main__":

    percy = Perceptron(2)

    pad = [
        [0,0],
        [0,1],
        [1,0],
        [1,1],
    ]

    res_desejado = [0, 0, 0, 1]

    print(percy.w)
            
    percy.treinar(pad, res_desejado)

    print(percy.w)

    print("Y: " + str(percy.y([0, 0])))
    print("Y: " + str(percy.y([0, 1])))
    print("Y: " + str(percy.y([1, 0])))
    print("Y: " + str(percy.y([1, 1])))