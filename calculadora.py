
while True:


    primeiro_numero = input('Digite um número: ')
    segundo_numero = input('Digite outro número: ')
    operador = input('O que você quer fazer com esses números?: ')
    floti = float(primeiro_numero)
    floti2 = float(segundo_numero)

    if primeiro_numero or segundo_numero is f'{primeiro_numero or segundo_numero + '%'}




    if primeiro_numero :
        print(primeiro_numero)
    if segundo_numero:
        print (segundo_numero)
    if primeiro_numero == primeiro_numero + '%':
         print('Teste')
    if segundo_numero == segundo_numero + '%':
         print('Teste 2')
#    if primeiro_numero or segundo_numero == '%':
#         print('Esta calculadora não suporta porcentagens por enquanto, atualizações em breve.') 
    else:
        print('erro')

    if operador == '+': 
        print (float(f'{primeiro_numero}') + float(f'{segundo_numero}'))  
    elif operador == '-':
            print(float(f'{primeiro_numero}') - float (f'{segundo_numero}'))
    elif operador == '*':
        print(float(f'{primeiro_numero}') * float(f'{segundo_numero}')) 
    elif operador == '//':
        print(float(f'{primeiro_numero}') // float(f'{segundo_numero}')) 
    
    condicao = input('Deseja fazer mais uma conta?: ')
    if condicao == 'n':
         break
    
print('acabou')
