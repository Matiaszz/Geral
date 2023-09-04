
print(f'Opções disponíveis: + = Adição, - = Subtração,'\
'x = Multiplicação e % = Divisão ')
modulo = input('Digite o que você quer fazer: ')

if modulo == 'x':
    def multiplicacao(x=None, u= None, y=None, z=None,\
        w=input(f'Digite '), \
        v=input('Digite '), 
    ):
    
        x = w
        y = v
        u = int(x) * int(y)
        print(u)
        z = (f'{x} * {y} = {u}')
        print(z)  
    multiplicacao()

elif modulo == '+':
        def adicao (x=None, u= None, y=None, z=None,\
        w=input(f'Digite '), \
        v=input('Digite '), 
    ):
            
            x = w
            y = v
            u = int(x) + int(y)
            z = (f'{x} + {y} = {u}')
            print(z)  
        adicao()

elif modulo == '-':
        def subtracao (x=None, u= None, y=None, z=None,\
        w=input(f'Digite '), \
        v=input('Digite '), 
    ):
    
            x = w
            y = v
            u = int(x) - int(y)
            z = (f'{x} - {y} = {u}')
            print(z)  
        subtracao()

elif modulo == '%':
        def divisao (x=None, u= None, y=None, z=None,\
        w=input(f'Digite '), \
        v=input('Digite '), 
    ):
    
            x = w
            y = v
            u = int(x) / int(y)
            z = (f'{x} % {y} = {u}')
            print(z)  
        divisao()
else:
      print('Erro')