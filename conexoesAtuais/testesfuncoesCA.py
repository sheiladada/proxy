#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import conexoesAtuais
import sys

def testeAdicionarConexao(ipCliente,ipRoteadorOrigem, portaRoteadorOrigem,ipRoteadorDestino, portaRoteadorDestino,ipClienteDestino, portaClienteDestino, respostaEsperadaCliente, respostaEsperadaRot):
  conexoes = conexoesAtuais.ConexaoAtual()
  try:
    conexoes.adicionarConexao( ipCliente,ipRoteadorOrigem,portaRoteadorOrigem, ipRoteadorDestino, portaRoteadorDestino,ipClienteDestino, portaClienteDestino)
  except Exception, err:
    sys.stderr.write('EXCEÇÃO: %s\n' % str(err)) 
  if (conexoes.getClientesAtivos() != respostaEsperadaCliente):
    print "testeAdicionarConexao", ipCliente, ipRoteadorOrigem, portaRoteadorOrigem, ipRoteadorDestino, portaRoteadorDestino, portaClienteDestino, "falhou, resposta esperada: ", respostaEsperadaCliente, " resposta dada: ", conexoes.getClientesAtivos()
  if(conexoes.getRoteadoresAtivos() != respostaEsperadaRot):
    print "testeAdicionarConexao", ipCliente, ipRoteadorOrigem,portaRoteadorOrigem, ipRoteadorDestino, portaRoteadorDestino, portaClienteDestino, "falhou, resposta esperada: ", respostaEsperadaRot, " resposta dada: ", conexoes.getRoteadoresAtivos()

def testeDeletarConexao(ipCliente, ipRO, portaRO, respostaEsperadaCliente, respostaEsperadaRot):
  conexoes = conexoesAtuais.ConexaoAtual()
  try:
    conexoes.deletarConexao(ipCliente, ipRO, portaRO)
  except Exception, err:
    sys.stderr.write('EXCEÇÃO: %s\n' % str(err)) 
  if (conexoes.getClientesAtivos() != respostaEsperadaCliente):
    print "testeDeletarConexao", ipCliente, ipRO, portaRO,  "falhou, resposta esperada: ", respostaEsperadaCliente, " resposta dada: ", conexoes.getClientesAtivos()
  if(conexoes.getRoteadoresAtivos() != respostaEsperadaRot):
    print "testeDeletarConexao", ipCliente, ipRO, portaRO, "falhou, resposta esperada: ", respostaEsperadaRot, " resposta dada: ", conexoes.getRoteadoresAtivos()
