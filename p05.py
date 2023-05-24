import boto3

nome_bucket = 'jpap-novo-teste-20232'
regiao_aws = 'us-east-1'

def criar_bucke(bucket_name,region_name=regiao_aws):
    # Crie uma instância do cliente S3
    s3 = boto3.client('s3')
    
    # Crie o bucket
    try:
        response = s3.create_bucket(
            Bucket=bucket_name,
            ACL='private'
        )
        print(f"Bucket '{bucket_name}' criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar o bucket: {e}")

# Chame a função e passe o nome desejado para o bucket
criar_bucke(nome_bucket)