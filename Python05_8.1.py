#!/usr/bin/env python3

import sys

if not len(sys.argv) > 2:
    print('ERRO: Favor especificar uma chave do dicionario e seu respectivo favorito')
    exit(0)
elif len(sys.argv) != 3:
    print('ERRO: Insira somente a sua chave do dicionario e o respectivo favorito')
    exit(0)

c = sys.argv[1]
v = sys.argv[2]

print('Atencao:','"'+v+'"','sera considerado como o novo favorito da chave','"'+c+'"','no dicionario. Caso uma chave de mesmo nome exista, ela sera sobrescrita.')

Fav = {}

Fav['livro'] = 'Fim da picada'
Fav['musica'] = 'Sally - "Wan"'
Fav['planta'] = 'Alamanda blanchetti'
Fav['esporte'] = 'Ciclismo'
Fav['comida'] = 'Bolo'
#Fav['organismo'] = 'Angiosperma'
Fav['organismo'] = 'Gimnosperma'
#print('O organismo favorito for alterado para "Gimnosperma"')

print('As chaves ja registradas sao:')
for op in Fav:
    print(op)

if c not in Fav:
    print('"'+c+'"','foi adicionado como uma nova chave com','"'+v+'"','como seu favorito.')
else:
    print('"'+v+'"','substituiu',Fav[c],'como um(a) novo(a)',c,'favorito(a).')
Fav[c]=v

