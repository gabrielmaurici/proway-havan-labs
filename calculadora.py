import os

menu = 0
while menu != 3:

    os.system('clear')

    print('Casa de Câmbio Muito Dinheiro')
    print('------------------------------')
    print('1 - Nova Transação de Moedas')
    print('2 - Relatório de Transações')
    print('3 - SAIR!!!')

    menu = int(input())

    
    if menu == 1:
        os.system('clear')

        cliente = str(input('Digite o nome do Cliente: '))
        while len(cliente) <=2:
            os.system('clear')
            nome = str(input('Você precisa digitar o nome do seu Cliente: '))

        data = str(input('Digite a Data da Transação: '))
        while len(data) < 10:
            os.system('clear')
            data = str(input('Você precisa digitar uma Data para a Transação (ex: 00/00/0000): '))

        os.system('clear')

        if menu == 1:
            print('Moedas DISPONÍVEIS para conversão:')
            print('----------------------------------')
            print('1 - REAL')
            print('2 - DOLAR')
            print('3 - EURO')
            print('4 - PESO ARG')
            print('----------------------------------')

            nomeMoeda = {1: 'REAL', 2: 'DOLAR', 3: 'EURO', 4: 'PESO ARG'}

            moedaOrigem = int(input('Escolha uma Moeda de Origem disponível no menu: '))
            while (moedaOrigem < 1) or (moedaOrigem > 4):
                moedaOrigem = int(input('OPÇÃO INVÁLIDA - Escolha uma moeda apresentada no menu: '))

            numero1 = float(input('Digite o valor em {}: '.format(nomeMoeda[moedaOrigem])))
            while numero1 < 1:    
                numero1 = float(input('Você deve digitar um valor em {} para prosseguir: '.format(nomeMoeda[moedaOrigem])))
            print('----------------------------------')

            moedaDestino = int(input('Escolha uma Moeda de Destino disponível no menu: '))
            while (moedaDestino < 1) or (moedaDestino > 4):
                moedaDestino = int(input('OPÇÃO INVÁLIDA - Escolha uma moeda apresentada no menu: '))
            
            while moedaOrigem == moedaDestino:
                moedaDestino = int(input('A Moeda de Destino deve ser DIFERENTE da Moeda de Origem, escolha novamente: '))

            numero2 = float(input('Digite o valor da cotação do {} em relação ao {} hoje: '.format(nomeMoeda[moedaDestino], nomeMoeda[moedaOrigem])))
            while numero2 < 1:    
                numero2 = float(input('Você deve digitar o valor da cotação do {} para prosseguir: '.format(nomeMoeda[moedaDestino])))
            print('----------------------------------')

            siglaMoeda = {1: 'BRL', 2: 'US$', 3: 'EUR', 4: 'ARS'}

            resultado = numero1 / numero2
            resultadoTaxa = resultado / 10
            print('Transação Conlcuida com Sucesso!!!')
            print()
            print('Valor da conversão: {} {:.2f}'.format(siglaMoeda[moedaDestino], resultado))
            print('Valor dos 10% da Taxa de Transação: R$ {:.2f}'.format(resultadoTaxa))
            print('----------------------------------')
            input()