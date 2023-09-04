#start
import os
lista = [] 
while True:

   
    print('[i] = inserir, [a] = apagar, [l] listar, [p] sair')
    usuario = input('Selecione uma opção: ')

    if usuario == 'i':
        os.system('cls')
        item = input('Item: ')
        lista.append(item)
        print (f'{item} adicionado a lista')
        print(f'Lista atual: {lista}')
        continue
    elif usuario == 'l':
        if len(lista) < 1:
            print('Lista vazia')
        else:
            for indice, nome in enumerate(lista):
                print(indice, nome)
            continue
    elif usuario == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )
        try:
            apagou = int (indice_str) 
            del lista[apagou]
            print('Item excluido com sucesso')
        except ValueError:
            print('Erro, digite um número inteiro.')
        except IndexError:
            print('Este índice não existe')
        except Exception:
            print('Erro desconhecido')
    elif usuario == 'p':
        final = input('Aperte ENTER para sair do programa: ')
        break
    else:
        print('ERRO')
