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

        nome = str(input('Digite o nome do cliente: '))
        data = str(input('Digite a data da transação: '))

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
            numero1 = float(input('Digite o valor da Moeda de Origem: '))
            print('----------------------------------')
            moedaDestino = int(input('Escolha uma Moeda de Destino disponível no menu: '))
            if moedaOrigem == moedaDestino:
                print('A Moeda de Destino deve ser DIFERENTE da Moeda de Origem!')
            numero2 = float(input('Digite o valor da cotação do {} em relação ao {} hoje: '.format(nomeMoeda[moedaDestino], nomeMoeda[moedaOrigem])))
            print('----------------------------------')

            siglaMoeda = {1: 'BRL', 2: 'US$', 3: 'EUR', 4: 'ARS'}

            resultado = numero1 / numero2
            resultadoTaxa = resultado / 10
            print('Valor da conversão: {} {:.2f}'.format(siglaMoeda[moedaDestino], resultado))
            print('Valor dos 10% da Taxa de Transação: R$ {:.2f}'.format(resultadoTaxa))
            input()