import boto3

nome_bucket = "nome nome"

def listClient(meu_bucket):
    '''
      Listar objetos no Bucket usando a Client API 
      Tipo de retorno: dicionário. Chamadas de API adicionais podem ser 
      necessárias para obter objetos
    '''
    s3client = boto3.client('s3')
    resposta = s3client.list_objects_v2(Bucket=meu_bucket)
    for conteudo in resposta['Contents']:
        print(conteudo['Key'],conteudo['LastModified'])
    return

listClient(nome_bucket)