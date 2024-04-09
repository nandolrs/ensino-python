#Método do programa

def AbrirArquivo(caminhoeNome): 
    arquivo = open(caminhoeNome, "r")
    conteudo = arquivo.read()
    print(conteudo)

#Função

def RetornarTerminar(terminar):
    retornar= None
    if terminar==1:
        print("Terminei")
        retornar= "Terminei"

    elif terminar==1 or terminar==2:
        print("Terminei 1,2")
        retornar= "Terminei 1,2"

    elif terminar>4:
        print("Maior que 4")
        retornar= "Maior que 4"
    
    else:
        print("Não terminei")
        retornar= "Não Terminei"

    
    return retornar