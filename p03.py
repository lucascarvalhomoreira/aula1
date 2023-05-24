#!/usr/bin/env python3

import boto3

nome_bucket = 'meu-bucket-mba-impacta'
regiao_aws = 'us-east-1'

def criar_bucket(nome_bucket,regiao):
    '''
    Cria um bucket na regiao indica.
    '''
    # Crie uma instância do recurso S3
    s3 = boto3.resource('s3',region_name=regiao_aws)
    regiao = {'LocationConstraint': regiao}
    # Crie o bucket
    bucket = s3.create_bucket(
            Bucket=nome_bucket,
            ACL='private'
        )
    print(f"Bucket {nome_bucket} criado com sucesso!")

# Chame a função e passe o nome desejado para o bucket
criar_bucket(nome_bucket,regiao_aws)