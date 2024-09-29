import boto3
import boto3.dynamodb.types
#import json
import decimal
import simplejson as json

def dynamo_to_python(dynamo_object: dict) -> dict:
    deserializer = boto3.dynamodb.types.TypeDeserializer()
    return {
        k: deserializer.deserialize(v) 
        for k, v in dynamo_object.items()
    }  
  
def python_to_dynamo(python_object: dict) -> dict:
    serializer = boto3.dynamodb.types.TypeSerializer()
    return {
        k: serializer.serialize(v)
        for k, v in python_object.items()
    }



dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('guilhermedb')

documento = {
}

# inclui 1

documento['codigo'] = 1
documento['nome'] = "nome 1"
table.put_item(Item=documento)
#print('inclui 1 =', documento)

# inclui 1

documento['codigo'] = 2
documento['nome'] = "nome 2"
table.put_item(Item=documento)
#print('inclui 1 =', documento)

# altera 1

documento['codigo'] = 1
documento['nome'] = 'nome 11'
table.put_item(Item=documento)
#print(documento)

# altera 2

documento['codigo'] = 2
documento['nome'] = 'nome 22'
table.put_item(Item=documento)
#print(documento)

# consulta 1

documentoBusca = {}
documentoBusca['codigo'] = 1
documentoConsultado = table.get_item(Key=documentoBusca)
#print(documentoConsultado)


# consulta 1

documentoBusca['codigo'] = 2
documentoConsultado = table.get_item(Key=documentoBusca)

d = json.dumps(documentoConsultado) # , use_decimal=True

#d = json.dumps(documentoConsultado)


#print(documentoConsultado)

# lista

documentoLista = table.scan(
        TableName = 'guilhermedb'
    )

d = json.dumps(documentoLista) # , use_decimal=True

documentoJSON = python_to_dynamo(documentoLista)
print ('documentoJSON= ', documentoJSON)

documentoJSON = dynamo_to_python(documentoJSON)
print ('documentoJSON= ', documentoJSON)





