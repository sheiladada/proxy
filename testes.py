#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import conexoesAtuais

conexoes = conexoesAtuais.ConexaoAtual()

#adicionarConexao(self, ipCliente, portaCliente, ipRoteadorOrigem, ipRoteadorDestino, portaRoteadorDestino, portaClienteDestino)
if (conexoes.adicionarConexao('10.0.0.1', 11111, '192.168.0.1', '192.168.0.2', 22222, 33333)):
  print "Codigo correto"
  conexoes.printClientesAtivos()
  conexoes.printRoteadoresAtivos()

else:
  print "Erro no código"

#adiciona conexão para o mesmo ipcliente com porta do cliente diferente e porta do roteador destino diferente
if (conexoes.adicionarConexao('10.0.0.1', 11112, '192.168.0.1', '192.168.0.2', 22221, 33333)):
  print "Codigo correto"
  conexoes.printClientesAtivos()
  conexoes.printRoteadoresAtivos()

else:
  print "Erro no código"

#adiciona conexão para a mesma porta cliente, deve dar erro
if (conexoes.adicionarConexao('10.0.0.1', 11111, '192.168.0.1', '192.168.0.2', 22223, 33333)):
  print "Erro no código - aceitou a adição"

else:
  print "Código correto"
  conexoes.printClientesAtivos()
  conexoes.printRoteadoresAtivos()

#adiciona conexão para a mesma porta roteador destino, deve dar erro
if (conexoes.adicionarConexao('10.0.0.1', 11113, '192.168.0.1', '192.168.0.2', 22221, 33333)):
  print "Erro no código - aceitou a adição"

else:
  print "Código correto"
  conexoes.printClientesAtivos()
  conexoes.printRoteadoresAtivos()

