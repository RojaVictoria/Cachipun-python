import sys
import random

jugadas = ['piedra', 'papel', 'tijeras']
jugada_usuario = sys.argv[1]
jugada_computador = random.choice(jugadas)

if jugada_usuario == 'piedra' or jugada_usuario == 'papel' or jugada_usuario == 'tijeras':
    print(f'Tú jugaste {jugada_usuario}')
    print(f'El computador jugó {jugada_computador}')
else:
    print(f'Argumento inválido: Debe ser piedra, papel o tijeras')

if jugada_usuario == jugada_computador:
    print('Empataste')
elif jugada_usuario == 'piedra' and jugada_computador == 'tijeras':
    print('Ganaste!!')
elif jugada_usuario == 'papel' and jugada_computador == 'piedra':
    print('Ganaste!!')
elif jugada_usuario == 'tijeras' and jugada_computador == 'papel':
    print('Ganaste!!')
elif jugada_usuario == 'piedra' and jugada_computador == 'papel':
    print('Perdiste :c')
elif jugada_usuario == 'papel' and jugada_computador == 'tijeras':
    print('Perdiste :c')
elif jugada_usuario == 'tijeras' and jugada_computador == 'piedra':
    print('Perdiste :c')