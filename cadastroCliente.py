import os

ClientesNomes = []
ClientesCode = []

def CadastrarCliente():
   
    clienteNome = input('Nome do cliente :')
    clienteCode = input('Codigo do cliente :')
    ClientesNomes.append(clienteNome)
    ClientesCode.append(clienteCode)
    input ('[ENTER] PARA CONTINUAR')

def VerificarStatusCliente():
    cliente = input('PESQUISA :')

    if cliente in ClientesNomes or ClientesCode:
        print('Cliente já cadastrado')
    else:
        print('Cliente não cadastrado')
    input ('[ENTER] PARA CONTINUAR')

def ListarClientes():
    i = len(ClientesNomes)
    j = 0
    print('LISTA DE CLIENTES')
    while j < i:
        print(f'Nome :{ClientesNomes[j]} | Codigo :{ClientesCode[j]}')
        j += 1
    input('[ENTER] - Para continuar')
    

while True:
    os.system('clear')
    print('-----------MENU------------')
    print('[1] - CADASTRAR')
    print('[2] - VERIFICAR CLIENTE')
    print('[3] - LISTAR CLIENTES')
    print('[4] - SAIR')
    op = input('>>')

    if op == '1':
        CadastrarCliente()
    elif op == '2':
        VerificarStatusCliente()
    elif op == '3':
        ListarClientes()
    elif op == '4':
        break




