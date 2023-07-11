from random import randint   

class Random:
    def __init__(self):

        self.num = randint(0,10)

    def JogoAdivinhacao(self):
        a = int(0)
        while a == 0:
            numChoice = int(input('Digite um número de 0 a 10:\n '))
            if numChoice == self.num:
                print(f' Parabéns, vc acertou o número, resposta: {self.num}')
                a += 1
            elif numChoice > 10:
                print('número invalido, escolha um número entre 0 e 10')
            elif numChoice != self.num:
                print(' número errado, tente novamente')
            else:
                print('erro')



