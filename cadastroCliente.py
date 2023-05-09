import os

class Cadastro:
    
    def __init__(self,usuario,senha):
        self.listaClientes = []
        self.usuario = usuario
        self.senha = senha

    def cadastrar(self):
        novoCad = []
        novoCad.append(self.usuario)
        novoCad.append(self.senha)
        self.listaClientes.append(novoCad)

    def listarClientes(self):
        os.system('clear')
        print('Lista de clientes:')
        for i in range(len(self.listaClientes)):
            print(f'{i+1}. Usuário: {self.listaClientes[i][0]}, Senha: {self.listaClientes[i][1]}')
    

clientes = Cadastro(None, None)

for i in range(3):
    usuario = input('Digite o nome de usuário: ')
    senha = input('Digite a senha: ')
    new = Cadastro(usuario, senha)
    new.cadastrar()
    clientes.listaClientes.extend(new.listaClientes)

clientes.listarClientes()

    



    
            
    











