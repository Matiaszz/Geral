import os

maquina = 'REFRIGERANTE', 'PIPOCA', 'SALGADINHO', 'SNACK'

for item in enumerate (maquina):
 print(item)

usuario = input('Digite o número correspondente ao que você quer comprar: ')



if usuario == '0':
   dinheiro = print('Insira o valor em dinheiro para resgatar seu item (3 R$): ')
   os.system('cls')
   # Ainda não estou no nível de criar um sistema inteiro para verificar cada nota
   if dinheiro: # for menor que 3
         print('REFRIGERANTE: Erro, valor insuficiente')
   elif dinheiro: # for maior que 3
         print('REFRIGERANTE: Pedido confirmado, aqui está seu troco e seu pedido.')
   else: # for 3
         print('REFRIGERANTE: Pedido confirmado')



if usuario == '1':
   dinheiro = print('Insira o valor em dinheiro para resgatar seu item (3 R$): ')
   os.system('cls')
   # Ainda não estou no nível de criar um sistema inteiro para verificar cada nota
   if dinheiro: # for menor que 3
         print('PIPOCA: Erro, valor insuficiente')
   elif dinheiro: # for maior que 3
         print('PIPOCA: Pedido confirmado, aqui está seu troco e seu pedido.')
   else: # for 3
         print('PIPOCA: Pedido confirmado')



if usuario == '2':
   dinheiro = print('Insira o valor em dinheiro para resgatar seu item (3 R$): ')
   os.system('cls')
   # Ainda não estou no nível de criar um sistema inteiro para verificar cada nota
   if dinheiro: # for menor que 3
         print('SALGADINHO: Erro, valor insuficiente')
   elif dinheiro: # for maior que 3
         print('SALGADINHO: Pedido confirmado, aqui está seu troco e seu pedido.')
   else: # for 3
         print('SALGADINHO: Pedido confirmado')



if usuario == '3':
   dinheiro = print('Insira o valor em dinheiro para resgatar seu item (3 R$): ')
   os.system('cls')
   # Ainda não estou no nível de criar um sistema inteiro para verificar cada nota
   if dinheiro: # for menor que 3
         print('SNACK: Erro, valor insuficiente')
   elif dinheiro: # for maior que 3
         print('SNACK: Pedido confirmado, aqui está seu troco e seu pedido.')
   else: # for 3
         print('SNACK: Pedido confirmado')

