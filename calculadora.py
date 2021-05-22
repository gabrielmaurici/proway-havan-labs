import os
import pickle
from datetime import datetime as dt

menu = 0
while menu != 3: #while para deixar o programa rodando em loop, só encerra quando o usuário da input no menu com o número 3

    # Função pra validar entrada de dados do usuário nos menus, evitando que o programa encerre caso ele digite uma string.
    def leiaInt(mensagem): 
        ok = False
        valor = 0
        while True:
            num = str(input(mensagem))
            if num .isnumeric():
                valor = int(num)
                ok = True
            else:
                print('OPÇÃO INVÁLIDA - Escolha uma opção do menu')
            if ok:
                break                
        return valor

    # Função chamada pela leiaFloat, indetifica se uma string é um número decimal (Float)
    def verificarFloat(numero):
        try:
            float(numero)
        except ValueError:
            return False
        return True
    
    # Função para validar entrada de dados do usuário, enquanto não for Float, pede pro usuário digitar um valor.
    def leiaFloat(mensagem):
        while True:   
            numero = input(mensagem)
            if verificarFloat(numero) == True:
                numero = float(numero)
                break
            else:
                print('Digite um Valor!!!!')
        return numero

    # Função para converter uma data string em inteira no padrão 'Ano, mês e dia'
    def dataInt(mensagem):
            dataString = input(mensagem).strip()
            while len(dataString) < 10:
                dataString = input('Você precisa digitar uma Data (ex: 00/00/0000): ').strip()
            dataInteira = dt.strftime(dt.strptime(dataString, '%d/%m/%Y'), '%Y%m%d')
            dataInteira = int(dataInteira)
            return dataInteira

    # Função para converter data para string, no padrão 'Dia, mês e ano'
    def formatarData (variavel):
        variavel['data'] = str(variavel['data'])
        dataFormatada = dt.strptime(variavel['data'], '%Y%m%d')
        dataFormatada = dataFormatada.strftime('%d/%m/%Y')
        return dataFormatada

    os.system('cls')

    print('Casa de Câmbio Muito Dinheiro')
    print('------------------------------')
    print('1 - Nova Transação de Moedas')
    print('2 - Relatório de Transações')
    print('3 - SAIR!!!')

    menu = int(input())

    # If referente a opção 'Nova Transação de Moedas'
    if menu == 1:
        os.system('cls')

        cliente = str(input('Digite o nome do Cliente: ')).title().strip()
        while len(cliente) <= 2:
            os.system('cls')
            cliente = str(input('Você precisa digitar o nome do seu Cliente: ')).title().strip()

        dataInteira = dataInt('Digite a Data da Transação: ')

        os.system('cls')

        if menu == 1:
            print('Moedas DISPONÍVEIS para conversão:')
            print('----------------------------------')
            print('1 - REAL')
            print('2 - DOLAR')
            print('3 - EURO')
            print('4 - PESO ARG')
            print('----------------------------------')

            nomeMoeda = {1: 'REAL', 2: 'DOLAR', 3: 'EURO', 4: 'PESO ARG'}
            siglaMoeda = {1: 'BRL', 2: 'US$', 3: 'EUR', 4: 'ARS'}

            moedaOrigem = leiaInt('Escolha uma Moeda de Origem disponível no menu: ')
            
            numero1 = 0
            while numero1 < 1:    
                numero1 = leiaFloat('Digite o valor em {}: '.format(nomeMoeda[moedaOrigem]))
            print('----------------------------------')

            moedaDestino = leiaInt('Escolha uma Moeda de Destino disponível no menu: ')
            while moedaOrigem == moedaDestino:
                moedaDestino = leiaInt('A Moeda de Destino deve ser DIFERENTE da Moeda de Origem, escolha novamente: ')
            
            numero2 = 0
            while numero2 < 0.01:    
                numero2 = leiaFloat('Digite o valor da cotação do {} em relação ao {} hoje: '.format(nomeMoeda[moedaDestino], nomeMoeda[moedaOrigem]))
            
            # If para conversão do câmbio, se moeda de destino for diferente de REAL, converte a taxa para real.
            if moedaDestino != 1:
                numero3 = 0
                print('----------------------------------')
                while numero3 < 0.01:
                    numero3 = leiaFloat('Digite o valor da cotação do REAL em relação ao {} para o cálculo da Taxa: '.format(nomeMoeda[moedaDestino]))

                resultado = numero1 / numero2
                resultadoTaxa = resultado / numero3
                resultadoTaxaConvertida = resultadoTaxa / 10
                print('----------------------------------\n')
                print('Transação Conlcuida com Sucesso!!!\n')
                print('Valor da conversão: {} {:.2f}'.format(siglaMoeda[moedaDestino], resultado))
                print('Valor dos 10% da Taxa de Transação: R$ {:.2f}'.format(resultadoTaxaConvertida))
                print('----------------------------------')
                input()
            else:
                resultado = numero1 / numero2
                resultadoTaxaConvertida = resultado /10
                print('----------------------------------\n')
                print('Transação Conlcuida com Sucesso!!!\n')
                print('Valor da conversão: {} {:.2f}'.format(siglaMoeda[moedaDestino], resultado))
                print('Valor dos 10% da Taxa de Transação: R$ {:.2f}'.format(resultadoTaxaConvertida))
                print('----------------------------------')
                input()
            # Dicionário para receber todos os dados do cliente referente a transação
            dicionarioTransacoes = {'cliente': cliente, 'data': dataInteira, 'moedaOrigem': nomeMoeda[moedaOrigem], 'moedaDestino': nomeMoeda[moedaDestino],
            'siglaOrigem': siglaMoeda[moedaOrigem], 'siglaDestino': siglaMoeda[moedaDestino], 'valorOrigem': numero1, 'valorConvertido': resultado, 
            'valorTaxa': resultadoTaxaConvertida}

            transacoes = list() # Lista que ira receber os dicionários com os dados do cliente
            
            # Abre o arquivo 'transacoes.txt' para puxar os dados anteriores e inserir a nova transação
            arquivo = open('transacoes.txt', 'rb')
            transacoes = pickle.load(arquivo)
            transacoes.append(dicionarioTransacoes)
            arquivo.close()

            arquivo = open('transacoes.txt', 'wb')
            pickle.dump(transacoes, arquivo)
            arquivo.close()
    
    # If referente a opção 'Relatório das Transações'
    if menu == 2:
        os.system('cls')

        # Abre o arquivo 'transacoes.txt' para receber todas as transações na lista de dicionario 'transacoes'
        arquivo = open('transacoes.txt', 'rb')
        transacoes = pickle.load(arquivo)
        arquivo.close()

        print('1 - Pesquisar por nome do Cliente')
        print('2 - Intervalo de Datas')
        print('3 - Lista com todas as Operações')
        print('----------------------------------')
        menuRelatorios = int(input())

        # If referente a opção 'Pesquisar por nome do Cliente'
        if menuRelatorios == 1:
            os.system('cls')

            nome = str(input('Digite o nome do Cliente: ')).title().strip()
            while len(nome) < 2:
                nome = str(input('Você precisa digitar o nome de um Cliente: ')).title().strip()

            controle = 0
            total = 0
            # For para ler as transações da lista 'transacoes' e filtrar pelo nome digitado pelo usuário
            for pessoas in transacoes:
                if pessoas['cliente'] == nome:
                    dataFormatada = formatarData(pessoas)
                    controle = 1
                    print('----------------------------------')
                    print('Nome: ', pessoas['cliente'])
                    print('Data: ', dataFormatada)
                    print('Moeda Origem: ', pessoas['moedaOrigem'])
                    print('Moeda Destino: ' ,pessoas['moedaDestino'])
                    print('Valor Origem: {} {:.2f}'.format(pessoas['siglaOrigem'], pessoas['valorOrigem']))
                    print('Valor Convertido: {} {:.2f}'.format(pessoas['siglaDestino'], pessoas['valorConvertido']))
                    print('Valor Taxa: R$ {:.2f}'.format(pessoas['valorTaxa']))
                    total += pessoas['valorTaxa']
            if controle == 0:
                print('----------------------------------')
                print('Não existem transações com este Nome!!!')

            print('----------------------------------')
            print('Total das Taxas cobradas sobre este Cliente: R$ {:.2f}'.format(total))     
            input()
        
        # If referente a opção 'Intervalo de Datas'
        if menuRelatorios == 2:
            os.system('cls')

            dataInt1 = dataInt('Digite a Data Inicial: ')
            dataInt2 = dataInt('Digite a Data Final: ')
 
            controle = 0
            total = 0
            # For para ler os dados da lista 'transacoes' e filtrar a busca pelo intervalo de datas escolhido pelo usuário
            for data in transacoes:
                if (data['data'] >= dataInt1) and (data['data'] <= dataInt2):
                    dataFormatada = formatarData(data)
        
                    controle = 1
                    print('----------------------------------')
                    print('Nome: ', data['cliente'])
                    print('Data: ', dataFormatada)
                    print('Moeda Origem: ', data['moedaOrigem'])
                    print('Moeda Destino: ' ,data['moedaDestino'])
                    print('Valor Origem: {} {:.2f}'.format(data['siglaOrigem'], data['valorOrigem']))
                    print('Valor Convertido: {} {:.2f}'.format(data['siglaDestino'], data['valorConvertido']))
                    print('Valor Taxa: R$ {:.2f}'.format(data['valorTaxa']))
                    total += data['valorTaxa']
            print('----------------------------------')
            print('Total das Taxas cobradas sobre todas as Transações neste intervalo de Datas: R$ {:.2f}'.format(total))
            if controle == 0 :
                print('----------------------------------')
                print('Não existem transações neste intervalo de Datas!!!')
            input()

        total = 0
        # If referente a opção 'Lista com todas as Operações'
        if menuRelatorios == 3:
            os.system('cls')
            # For para ler e imprimir todos os dados da lista 'transacoes'
            for transacao in transacoes:
                dataFormatada = formatarData(transacao)

                print('----------------------------------')
                print('Nome: ', transacao['cliente'])
                print('Data: ', dataFormatada)
                print('Moeda Origem: ', transacao['moedaOrigem'])
                print('Moeda Destino: ' ,transacao['moedaDestino'])
                print('Valor Origem: {} {:.2f}'.format(transacao['siglaOrigem'], transacao['valorOrigem']))
                print('Valor Convertido: {} {:.2f}'.format(transacao['siglaDestino'], transacao['valorConvertido']))
                print('Valor Taxa: R$ {:.2f}'.format(transacao['valorTaxa']))
                total += transacao['valorTaxa']
            print('----------------------------------')
            print('Total das Taxas cobradas sobre todos os Clientes: R$ {:.2f}'.format(total))
            input()