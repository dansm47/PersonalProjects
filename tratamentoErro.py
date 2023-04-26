print('teste de tratamento de erro usando try e except')

a = int(0)      
while a == 0:    
    try:
            numero = int(input('digite um número ')) 
            break #o codigo ira tentar executar a linha de cima, caso seja inserido pelo usuario um numero tipo int, o break é executado e para o laço, se não, executa o except e o laço continua até o usuario digitar um número
           
            

    except ValueError: 
        
            print('Erro!!, vc não digitou um número, tente novamente ')

print(f'vc digitou um número: {numero}')       

        
            



