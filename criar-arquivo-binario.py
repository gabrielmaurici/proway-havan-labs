# Criar arquivo.txt binário
import pickle

transacoes = list()

arquivo = open('transacoes.txt', 'wb')
pickle.dump(transacoes, arquivo)
arquivo.close()