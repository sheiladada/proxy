#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import conexoesAtuais
import sys

conexoes = conexoesAtuais.ConexaoAtual()

#conexões ativas: '10.0.0.1', 11111, '192.168.0.1', '192.168.0.2', 22222, 33333;
#10.0.0.1', 11112, '192.168.0.1', '192.168.0.2', 22221, 33333
#{'192.168.0.2': [22222, 22221]}


#adicionarConexao(self, ipCliente, portaCliente, ipRoteadorOrigem, ipRoteadorDestino, portaRoteadorDestino, portaClienteDestino)
try:
  conexoes.adicionarConexao('10.0.0.1', 11111, '192.168.0.1', '192.168.0.2', 22222, 33333)
  print "Código correto"
  conexoes.printClientesAtivos()
  conexoes.printRoteadoresAtivos()
  #{'10.0.0.1': {11111: ['192.168.0.1', '192.168.0.2', 22222, 33333]}}
  #{'192.168.0.2': [22222]}
except Exception, err:
  sys.stderr.write('ERRO: %s\n' % str(err)) 
  print ("Não foi adicionada conexão. Código incorreto")

#adiciona conexão para o mesmo ipcliente com porta do cliente diferente e porta do roteador destino diferente
try:
  conexoes.adicionarConexao('10.0.0.1', 11112, '192.168.0.1', '192.168.0.2', 22221, 33333)
  print "Código correto"
  conexoes.printClientesAtivos()
  conexoes.printRoteadoresAtivos()
  #{'10.0.0.1': {11112: ['192.168.0.1', '192.168.0.2', 22221, 33333], 11111: ['192.168.0.1', '192.168.0.2', 22222, 33333]}}
  #{'192.168.0.2': [22222, 22221]}
except Exception, err:
  sys.stderr.write('ERRO: %s\n' % str(err)) 
  print ("Não foi adicionada conexão. Código incorreto")

#adiciona conexão para a mesma porta cliente, deve dar erro
try:
  conexoes.adicionarConexao('10.0.0.1', 11111, '192.168.0.1', '192.168.0.2', 22223, 33333)
  print "Código incorreto. Adicionou conexão."
  conexoes.printClientesAtivos()
  conexoes.printRoteadoresAtivos()
except Exception, err:
  sys.stderr.write('ERRO: %s\n' % str(err)) 
  print ("Não foi adicionada conexão. Código correto.")
  conexoes.printClientesAtivos()
  conexoes.printRoteadoresAtivos()
  #{'10.0.0.1': {11112: ['192.168.0.1', '192.168.0.2', 22221, 33333], 11111: ['192.168.0.1', '192.168.0.2', 22222, 33333]}}
  #{'192.168.0.2': [22222, 22221]}

#adiciona conexão para a mesma porta roteador destino, deve dar erro
try:
  conexoes.adicionarConexao('10.0.0.1', 11113, '192.168.0.1', '192.168.0.2', 22221, 33333)
  print "Código incorreto. Adicionou conexão."
  conexoes.printClientesAtivos()
  conexoes.printRoteadoresAtivos()
except Exception, err:
  sys.stderr.write('ERRO: %s\n' % str(err)) 
  print ("Não foi adicionada conexão. Código correto")
  conexoes.printClientesAtivos()
  conexoes.printRoteadoresAtivos()
  #{'10.0.0.1': {11112: ['192.168.0.1', '192.168.0.2', 22221, 33333], 11111: ['192.168.0.1', '192.168.0.2', 22222, 33333]}}
  #{'192.168.0.2': [22222, 22221]}

#deleta conexão normalmente
try:
  conexoes.deletarConexao('10.0.0.1', 11111)
  conexoes.printClientesAtivos()
  conexoes.printRoteadoresAtivos()
  #{'10.0.0.1': {11112: ['192.168.0.1', '192.168.0.2', 22221, 33333]}}
  #{'192.168.0.2': [22221]}
except Exception, err:
  sys.stderr.write('ERRO: %s\n' % str(err))
  print("Não foi deletada a conexão. Código incorreto.")

#deleta conexão com porta que não está no dicionário
try:
  conexoes.deletarConexao('10.0.0.1', 11113)
  print("Foi deletada conexão inexistente. Código incorreto.")
except Exception, err:
  sys.stderr.write('ERRO: %s\n' % str(err))
  print("Não foi deletada conexão. Código correto.")
  #{'10.0.0.1': {11112: ['192.168.0.1', '192.168.0.2', 22221, 33333]}}
  #{'192.168.0.2': [22221]}
