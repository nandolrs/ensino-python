#Método do programa

def AbrirArquivo(caminhoeNome): 
    arquivo = open(caminhoeNome, "r")
    conteudo = arquivo.read()
    print(conteudo)




