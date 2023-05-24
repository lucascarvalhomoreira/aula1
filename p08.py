import boto3

aws_session = boto3.session.Session()

# Lista os recursos disponiveis
print("------------------------")
print(aws_session.get_available_resources())
print("------------------------")
# Lista os servicos disponiveis
print(aws_session.get_available_services())
print("------------------------")