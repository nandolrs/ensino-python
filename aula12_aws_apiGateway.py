#import biblioteca
import json

def RetornarMaiorV1R1(novosnumeros):
    retornar= novosnumeros[0]

    for numero in novosnumeros:

        if numero > retornar:
            retornar = numero


    return retornar

def lambda_handler(event, context):

    try:
        httpMethod= event['requestContext']['http']['method']

        numeros = [50, 10, 20, 20]

        if httpMethod == 'POST':
        # body
            httpBodyJson = event['body']
            httpBody = json.loads(httpBodyJson) 
            numeros= httpBody['numeros']


        maior = RetornarMaiorV1R1(numeros)

        print (maior)

        retorno= {

            'retorno': maior
        }

        return retorno

    except Exception as e:
        print(f"Ocorreu um erro{e}")
        raise e
    
#lambda_handler(None, None)