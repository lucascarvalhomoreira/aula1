import boto3

nome_bucket = "nome nome"

def listResource(meu_bucket):
    '''
      Listar objetos no balde usando a Client API
      Recursos representam uma interface orientada a objetos para AWS. 
      Eles fornecem uma abstração de nível superior do que as chamadas 
      brutas de baixo nível feitas por clientes de serviço
    '''
    s3resource = boto3.resource('s3')
    bucket = s3resource.Bucket(meu_bucket)
    for objeto in bucket.objects.all():
        print(objeto.key, objeto.last_modified)
    return 

listResource(nome_bucket)