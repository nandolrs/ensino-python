import json

def RetornarMaiorV1R1(novosnumeros):
    retornar= novosnumeros[0]

    for numero in novosnumeros:

        if numero > retornar:
            retornar = numero


    return retornar

def lambda_handler(event, context):
    # TODO implement
    
    #import biblioteca
    
    numeros = [10, 10, 20, 20]
    
    maior = RetornarMaiorV1R1(numeros)
    
    print('Resultado: ')
    print (maior)
    
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello Guilherne!')
    }
