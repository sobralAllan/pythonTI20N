from Model import Model

class Control:
    def __init__(self):
        self.modelo = Model() #Instanciando a classe model
        self.opcao  = 0

    def mostrarMenu(self):
        print('Escolha uma das opções abaixo: ' +
              '\n1. Sair'                       +
              '\n2. Trocar'                     +
              '\n3. Tabuada'                    +
              '\n4. Média de Três notas')

    def operacoes(self):
        while(self.opcao != 1):
            self.mostrarMenu()
            self.opcao = int(input('Informe o número: '))
            if self.opcao == 1:
                print('Obrigado')
            elif self.opcao == 2:
                valorA = int(input('Informe um valor para A: '))
                valorB = int(input('Informe um valor para B: '))
                print(self.modelo.trocar(valorA,valorB))
            elif self.opcao == 3:
                num = int(input('Informe um número: '))
                print(self.modelo.tabuada(num))
            elif self.opcao == 4:
                nota1 = float(input('Primeira Nota: '))
                while(nota1 < 0 or nota1 > 10):
                    print('Erro, informe uma nota entre 0 e 10')
                    nota1 = float(input('Primeira Nota: '))

                nota2 = float(input('Segunda Nota: '))
                while(nota2 <0 or nota2 > 10):
                    print('Erro, informe uma nota  entre 0 e 10')
                    nota2 = float(input('Segunda Nota: '))

                nota3 = float(input('Terceira Nota: '))
                while(nota3 < 0 or nota3 > 10):
                    print('Erro, informe uma nota entre 0 e 10')
                    nota3 = float(input('Terceira Nota: '))

                print(self.modelo.mediaTres(nota1,nota2,nota3))
            else:
                print('Opção escolhida não é válida!')