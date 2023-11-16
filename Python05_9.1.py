#!/usr/bin/env python3

Fav = {}

Fav['livro'] = 'Fim da picada'
Fav['musica'] = 'Sally - "Wan"'
Fav['planta'] = 'Alamanda blanchetti'
Fav['esporte'] = 'Ciclismo'
Fav['comida'] = 'Bolo'
Fav['organismo'] = 'Gimnosperma'

print('As chaves e seus valores ja registrados sao:')
for op in Fav:
    print(op+':',Fav[op])
