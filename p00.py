#!/usr/bin/env python3

import boto3

# Criação do cliente do serviço S3
s3_client = boto3.client('s3')
# Listar os buckets
resposta = s3_client.list_buckets()
# Extrair os nomes dos buckets da resposta
buckets = [bucket['Name'] for bucket in resposta['Buckets']]

# Imprimir os nomes dos buckets
for bucket in buckets:
    print(bucket)