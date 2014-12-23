#!/usr/bin/env python
# -*- coding: utf-8 -*-
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