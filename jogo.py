import os
# Variáveis
contador_bolsonaro = 0
contador_lula = 0

# Loop
while True:
    print('Opções:')
    print('LULA (L) ou BOLSONARO (B)')
    entrada = input('Qual candidato você irá votar?: ') #Resposta do usuário
    if entrada == 'B':
            for voto_bolosonaro in entrada:
                contador_bolsonaro += 1 # Adicionar um voto a bolsonaro
                os.system('cls')
            print(f'Você votou no Bolsonaro, atualmente ele está com {contador_bolsonaro} votos')
    elif entrada == 'L' :
            for voto_lula in entrada:
                contador_lula += 1 # Adicionar um voto a lula
                os.system('cls')
                print(f'Você votou no Lula, atualmente ele está com {contador_lula} votos')
    else:
         print('Erro desconhecido, tente colocar "B" ou "L" em letra MAIÚSCULA.')
         ...