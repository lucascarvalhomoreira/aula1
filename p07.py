import boto3

nome_bucket = 'meu-bucket-mba-impacta'
regiao_aws = 'us-east-1'

def delete_bucket(nome_bucket):
    '''
    Apaga um bucket removento todos os seus objetos antes.
    '''
    # Crie uma instância do recurso S3
    s3 = boto3.resource('s3',region_name=regiao_aws)
    
    # Apague o bucket
    try:
        bucket = s3.Bucket(nome_bucket)
        bucket.objects.all().delete()
        bucket.delete()
        print(f"Bucket '{nome_bucket}' foi apagado com sucesso!")
    except Exception as e:
        print(f"Erro ao apagar o bucket: {e}")

# Chame a função e passe o nome do bucket que deseja apagar
delete_bucket(nome_bucket)