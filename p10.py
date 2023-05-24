import boto3

# Crie uma instância da classe Session e especifique o perfil desejado
session = boto3.session.Session(
    profile_name='default',
    region_name='us-east-2',
)

# Agora você pode criar clientes ou recursos usando a sessão
s3 = session.client('s3')


