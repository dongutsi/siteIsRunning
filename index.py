#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
/*----------------------------------------------------------------------*\
 * Copyright (C) 2014  Danilo da Silva Maciel
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
\*----------------------------------------------------------------------*/
"""
import requests

#função para impimir = na tela
def traste(n):
    t = ''
    for i in range(0,n):
        t += '='
    print t+'\n'

# inicio
# verifica o tipo de protocolo utizado http ou https
traste(30)
opcao = input("Tipo do site \n1 - http\n2 - https")
if opcao == 1:
    site = 'http://'
elif opcao == 2:
    site = 'https://'
else:
    print 'Opcao invalida'
    exit()

opcao = raw_input("Digite o site ")
traste(30)

site += opcao

print 'Site a ser pesquisado \n '+site
traste(30)
opcao = input('1 - Continuar \n2 - Cancelar')
traste(30)

if opcao == 1:
    traste(30)
    print 'Analisando, por favor aguarde...'
    #tenta realizar a conexão com o servidor
    try:
        #res irá conter os dados da requisição
        res = requests.get(site)
        print res.status_code
        #verifica o status de retorno da requisição, se for 200 existe e pode continuar com a lógica
        if res.status_code == 200:
            print 'O endereço existe'
            traste(30)
        elif res.status_code == 400:
            print 'O endereço não está funcionando'
            traste(30)
        elif res.status_code == 403:
            print 'Acesso proibido'
            traste(30)
        elif res.status_code == 404:
            print 'A página não existe'
            traste(30)
        elif res.status_code == 500:
            print 'Erro interno no servidor'
            traste(30)
        else:
            print 'Erro interno no servidor'
            traste(30)
    #se não existir o servidor
    except:
        traste(30)
        print 'Servidor não encontrado'
        traste(30)
elif opcao == 2:
    print 'Bye...\n'
