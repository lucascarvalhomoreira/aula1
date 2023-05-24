import boto3

# Cria uma instância da classe Session
session = boto3.session.Session(
    region_name='us-east-2',
    aws_access_key_id='ACCESS_KEY',
    aws_secret_access_key='SECRET_ACCESS_KEY',
)

# Agora você pode criar clientes ou recursos usando a sessão
s3 = session.client('s3')


