import boto3

nome_bucket = 'jpap-novo-teste-20232'
regiao_aws = 'us-east-1'

def delete_bucket(bucket_name):
    # Crie uma instância do recurso S3
    s3 = boto3.resource('s3',region_name=regiao_aws)
    
    # Apague o bucket
    try:
        bucket = s3.Bucket(bucket_name)
        bucket.delete()
        print(f"Bucket '{bucket_name}' foi apagado com sucesso!")
    except Exception as e:
        print(f"Erro ao apagar o bucket: {e}")

# Chame a função e passe o nome do bucket que deseja apagar
delete_bucket(nome_bucket)