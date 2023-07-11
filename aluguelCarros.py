import os

NomeCliente = []
CpfCliente = []
SenhaCliente = []
EnderecoCliente = []
TelefoneCliente = []
SaldoCliente = []
CarroAlugado = []
HorasAluguel = []

nomeVeiculo = ['Ford Fiesta', 'Volkswagen Gol', 'Chevrolet Onix', 'Fiat Uno', 'Toyota Corolla', 'Honda Civic',
               'BMW X1', 'Audi Q5', 'Mercedes-Benz Classe C', 'Tesla Model 3']
placaVeiculo = ['H13-BH6', 'J45-HD9', 'G78-DF2', 'R32-ED6', 'C92-PO1', 'T74-UN2', 'B51-MN6', 'A68-QW9', 'M83-PL7', 'T15-ES8']
valorHoraAluguel = [7.50, 8.00, 8.50, 7.00, 10.00, 9.50, 15.00, 18.00, 20.00, 25.00]


def cadastrarCliente():
    os.system('clear')
    print('========== CADASTRANDO NOVO CLIENTE')
    print()
    nome = input('Nome: ')
    cpf = input('CPF: ')
    senha = input('Senha: ')
    endereco = input('Endereço: ')
    telefone = input('Telefone: ')

    NomeCliente.append(nome)
    CpfCliente.append(cpf)
    SenhaCliente.append(senha)
    EnderecoCliente.append(endereco)
    TelefoneCliente.append(telefone)
    SaldoCliente.append(0)
    CarroAlugado.append(None) 

    os.system('clear')
    print('========== CLIENTE CADASTRADO COM SUCESSO!')
    pausar_execucao()


def exibirClientes():
    os.system('clear')
    print('========== RELATÓRIO DE CLIENTES\n')

    if not NomeCliente:
        print('Nenhum cliente cadastrado.\n')
    else:
        print(f'{"Nome":<15} {"CPF":<15} {"Endereço":<20} {"Telefone":<15} {"Saldo":<10} {"Carro Alugado":<20}')
        print('-' * 100)

        for i in range(len(NomeCliente)):
            nome = NomeCliente[i]
            cpf = CpfCliente[i]
            endereco = EnderecoCliente[i]
            telefone = TelefoneCliente[i]
            saldo = SaldoCliente[i]
            carro_alugado = nomeVeiculo[CarroAlugado[i]] if CarroAlugado[i] is not None else 'Nenhum'

            print(f'{nome:<15} {cpf:<15} {endereco:<20} {telefone:<15} R${saldo:<10.2f} {carro_alugado:<20}')

    pausar_execucao()


def pesquisarCliente():
    os.system('clear')
    print('========== PESQUISANDO CLIENTE')
    print()
    nome = input('Cliente a pesquisar: ')

    if nome in NomeCliente:
        indice = NomeCliente.index(nome)
        print(f'\nNome: \t\t{NomeCliente[indice]}')
        print(f'CPF: \t\t{CpfCliente[indice]}')
        print(f'Endereço: \t{EnderecoCliente[indice]}')
        print(f'Telefone: \t{TelefoneCliente[indice]}')
        print(f'Saldo: \t\tR${SaldoCliente[indice]:.2f}')
        if CarroAlugado[indice] is not None:
            print(f'Carro Alugado: \t{nomeVeiculo[CarroAlugado[indice]]}')
            print(f'Horas Aluguel: \t{HorasAluguel[indice]}')
        else:
            print('Carro Alugado: \tNenhum')
    else:
        print('Cliente não encontrado!')

    pausar_execucao()


def editarInformacoes():
    os.system('clear')
    print('========== EDITAR INFORMAÇÕES DO CLIENTE')
    print()
    validar, indice_cliente = login()

    if validar and indice_cliente is not None:
        print('Opções de edição:')
        print('[1] - Nome')
        print('[2] - CPF')
        print('[3] - Senha')
        print('[4] - Endereço')
        print('[5] - Telefone')
        print()
        op = input('Digite a opção desejada: ')

        if op == '1':
            novo_nome = input('Digite o novo nome: ')
            NomeCliente[indice_cliente] = novo_nome
            print('Nome atualizado com sucesso!')
        elif op == '2':
            novo_cpf = input('Digite o novo CPF: ')
            CpfCliente[indice_cliente] = novo_cpf
            print('CPF atualizado com sucesso!')
        elif op == '3':
            nova_senha = input('Digite a nova senha: ')
            SenhaCliente[indice_cliente] = nova_senha
            print('Senha atualizada com sucesso!')
        elif op == '4':
            novo_endereco = input('Digite o novo endereço: ')
            EnderecoCliente[indice_cliente] = novo_endereco
            print('Endereço atualizado com sucesso!')
        elif op == '5':
            novo_telefone = input('Digite o novo telefone: ')
            TelefoneCliente[indice_cliente] = novo_telefone
            print('Telefone atualizado com sucesso!')
        else:
            print('Opção inválida!')

    else:
        print('Login inválido')

    pausar_execucao()


def excluirCadastro():
    os.system('clear')
    print('========== EXCLUIR CADASTRO')
    print()
    validar, indice_cliente = login()

    if validar and indice_cliente is not None:
        print('Tem certeza de que deseja excluir o cadastro? Essa ação não pode ser desfeita.')
        print('[1] - Sim')
        print('[2] - Não')
        print()
        op = input('Digite a opção desejada: ')

        if op == '1':
            del NomeCliente[indice_cliente]
            del CpfCliente[indice_cliente]
            del SenhaCliente[indice_cliente]
            del EnderecoCliente[indice_cliente]
            del TelefoneCliente[indice_cliente]
            del SaldoCliente[indice_cliente]
            del CarroAlugado[indice_cliente]
            del HorasAluguel[indice_cliente]

            print('Cadastro excluído com sucesso!')
        elif op == '2':
            print('Exclusão de cadastro cancelada.')
        else:
            print('Opção inválida!')
    else:
        print('Login inválido')

    pausar_execucao()


def login(f=None):
    os.system('clear')
    print('========== TELA DE LOGIN')
    print()
    nome = input('Login: ')
    senha = input('Senha: ')

    if f == None:
        if nome in NomeCliente and senha in SenhaCliente:
            indice = NomeCliente.index(nome)
            if SenhaCliente[indice] == senha:
                return True, indice  

    return False, None


def alugarVeiculo():
    os.system('clear')
    print('========== ALUGUEL DE VEÍCULOS')
    print()
    validar, indice_cliente = login()

    if validar and indice_cliente is not None:
        if CarroAlugado[indice_cliente] is not None:
            print('Você já possui um veículo alugado.')
            pausar_execucao()
            return

        l = len(nomeVeiculo)

        if l == 0:
            print('Nenhum veículo disponível para aluguel.\n')
        else:
            print('========== VEÍCULOS DISPONÍVEIS PARA ALUGUEL')
            print(f'{"Código":<8} {"Veículo":<25} {"Placa":<12} {"Valor Hora":<15}')
            print('-' * 60)

            for i in range(l):
                print(f'{i:<8} {nomeVeiculo[i]:<25} {placaVeiculo[i]:<12} R${valorHoraAluguel[i]:<15.2f}')

            print()
            op = input('Digite o código do veículo desejado: ')

            try:
                indice_veiculo = int(op)

                if 0 <= indice_veiculo < l:
                    horas_aluguel = int(input('Digite o número de horas para aluguel: '))

                    valor_total = valorHoraAluguel[indice_veiculo] * horas_aluguel

                    if SaldoCliente[indice_cliente] >= valor_total:
                        CarroAlugado[indice_cliente] = indice_veiculo
                        HorasAluguel.append(horas_aluguel)  
                        SaldoCliente[indice_cliente] -= valor_total

                        os.system('clear')
                        print('========== ALUGUEL CONCLUÍDO')
                        print(f'Valor pago: R${valor_total:.2f}')
                        print(f'Saldo atual: R${SaldoCliente[indice_cliente]:.2f}')
                    else:
                        print('Saldo insuficiente para alugar o veículo.')
                else:
                    print('Código de veículo inválido!')
            except ValueError:
                print('Código de veículo inválido!')
    else:
        print('Login inválido')

    pausar_execucao()


def adicionarSaldo():
    os.system('clear')
    print('========== ADICIONAR SALDO')
    print()
    validar, indice_cliente = login()

    if validar and indice_cliente is not None:
        valor = float(input('Digite o valor a ser adicionado: '))
        SaldoCliente[indice_cliente] += valor

        os.system('clear')
        print('========== SALDO ADICIONADO COM SUCESSO')
        print(f'Saldo atual: R${SaldoCliente[indice_cliente]:.2f}')
    else:
        print('Login inválido')

    pausar_execucao()


def pausar_execucao():
    input('\nPressione [ENTER] para continuar...')


while True:
    os.system('clear')
    print('-----------MENU------------')
    print('[1] - CADASTRAR')
    print('[2] - ALUGAR')
    print('[3] - LISTAR CLIENTES')
    print('[4] - PESQUISAR')
    print('[5] - EDITAR INFORMAÇÕES DO CLIENTE')
    print('[6] - EXCLUIR CADASTRO')
    print('[7] - ADICIONAR SALDO')
    print('[8] - SAIR')
    print()
    op = input('Digite a opção desejada: ')

    if op == '1':
        cadastrarCliente()
    elif op == '2':
        alugarVeiculo()
    elif op == '3':
        exibirClientes()
    elif op == '4':
        pesquisarCliente()
    elif op == '5':
        editarInformacoes()
    elif op == '6':
        excluirCadastro()
    elif op == '7':
        adicionarSaldo()
    elif op == '8':
        break
