#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'life'
import requests

def traste(n):
    t = ''
    for i in range(0,n):
        t += '='
    print t+'\n'

opcao = input("Tipo do site \n1 - http\n2 - https\n")

if opcao == 1:
    site = 'http://'
elif opcao == 2:
    site = 'https://'
else:
    print 'Opcao invalida'
    exit()

opcao = raw_input("Digite o site \n")


site += opcao

print 'Site a ser pesquisado'
traste(30)
print site
traste(30)
opcao = input('1 - Continuar \n2 - Cancelar')

if opcao == 1:
    print 'Analisando, por favor aguarde...'
    #tenta realizar a conexão com o servidor
    try:
        #res irá conter os dados da requisição
        res = requests.get(site)

        #verifica o status de retorno da requisição, se for 200 existe e pode continuar com a lógica
        if(res.status_code == 200):
            traste(30)
            print 'O site está funcionando'
            traste(30)
        else:
            traste(30)
            print 'O site não está funcionando'
            traste(30)
    #se não existir o servidor
    except:
        traste(30)
        print 'Servidor não encontrado'
        traste(30)
elif opcao == 2:
    print 'Bye...\n'