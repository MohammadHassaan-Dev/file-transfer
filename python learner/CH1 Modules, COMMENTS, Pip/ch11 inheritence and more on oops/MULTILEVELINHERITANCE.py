class dada:
    dada = 1

    
class papa(dada):
    papa = 2

class beta(papa):
    beta = 3

o = beta()
print(o.dada, o.papa, o.beta)

