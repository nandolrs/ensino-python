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

# Retornar o maior número

def RetornarMaior(n1, n2, n3):
    retornar= None 

    if n1>n2 and n1>n3:
        retornar= n1

    elif n2>n1 and n2>n3:
        retornar= n2 

    elif n3>n1 or n3>n2:
        retornar= n3 

    return retornar

#Retornar qualquer número

def RetornarMaiorV1R1(novosnumeros):
    retornar= novosnumeros[0]

    for numero in novosnumeros:

        if numero > retornar:
            retornar = numero


    return retornar