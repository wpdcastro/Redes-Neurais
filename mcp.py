class MCP :
    
    def __init__(self, w, limiar) :
        self.w = w
        self.limiar = limiar
    
    def Y(self, entradas) :
        
        w = list()
        contador = 0
        
        for entrada in entradas :
            
            w.append(entrada * self.w[contador])
            
        if self.soma(w) >= self.limiar :
            return 1

        return 0
    
    def soma(self, w) :
        
        res = sum(w)
        
        return res 
    
if __name__ == "__main__":
    
    main() 
    
    mcp = MCP([0.5,0.5], 0.5)
    
    print("Y: ", mcp.Y([0,0]))
    print("Y: ", mcp.Y([0,1]))
    print("Y: ", mcp.Y([1,0]))
    print("Y: ", mcp.Y([1,1]))