#!/usr/bin/env python3

import boto3

regiao = 'us-east-1'  # Região desejada

def listar_buckets(regiao):
    '''
    Lista os buckets de uma dada regiao
    '''
    # Criação da sessão do boto3 na região especificada
    session = boto3.Session(region_name=regiao)
    # Criação do cliente do serviço S3
    s3_client = session.client('s3')
    # Listar os buckets
    response = s3_client.list_buckets()
    # Extrair os nomes dos buckets da resposta
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    # Retornar a lista de buckets
    return buckets
    
buckets = listar_buckets(regiao)

# Imprimir os nomes dos buckets
for bucket in buckets:
    print(bucket)