class MCP :
    
    def __init__(self, limiar) :
        self.limiar = limiar
    
    def Y(self, pesos, entradas) :
                
        w = list()

        for entrada in entradas :
            for peso in pesos:
                w.append(entrada * peso)
            
        if self.soma(w) >= self.limiar :
            return 1

        return 0
    
    def soma(self, w) :
        
        res = sum(w)
        
        return res 
    
if __name__ == "__main__":

    mcp = MCP(0.5)
    pesos = []
    pesos.insert(0, [-0.46, -0.07, 0.94])
    pesos.insert(1, [0.10, 0.94, 0.46])
    pesos.insert(2, [0.78, -0.22, 0.58])

    y1 = mcp.Y(pesos[0], [0, 0])
    y2 = mcp.Y(pesos[1], [0, 0])
    o1 = mcp.Y(pesos[2], [y1, y2])
    # o2 = mcp.Y(pesos[3], [y1, y2])
