#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import conexoesAtuais
import sys

def testeAdicionarConexao(ipCliente, portaCliente, ipRoteadorOrigem, ipRoteadorDestino, portaRoteadorDestino, portaClienteDestino, respostaEsperadaCliente, respostaEsperadaRot):
  conexoes = conexoesAtuais.ConexaoAtual()
  try:
    conexoes.adicionarConexao( ipCliente, portaCliente, ipRoteadorOrigem, ipRoteadorDestino, portaRoteadorDestino, portaClienteDestino)
  except Exception, err:
    sys.stderr.write('EXCEÇÃO: %s\n' % str(err)) 
  if (conexoes.getClientesAtivos() != respostaEsperadaCliente):
    print "testeAdicionarConexao", ipCliente, portaCliente, ipRoteadorOrigem, ipRoteadorDestino, portaRoteadorDestino, portaClienteDestino, "falhou, resposta esperada: ", respostaEsperadaCliente, " resposta dada: ", conexoes.getClientesAtivos()
  if(conexoes.getRoteadoresAtivos() != respostaEsperadaRot):
    print "testeAdicionarConexao", ipCliente, portaCliente, ipRoteadorOrigem, ipRoteadorDestino, portaRoteadorDestino, portaClienteDestino, "falhou, resposta esperada: ", respostaEsperadaRot, " resposta dada: ", conexoes.getRoteadoresAtivos()

def testeDeletarConexao(ipCliente, portaCliente, respostaEsperadaCliente, respostaEsperadaRot):
  conexoes = conexoesAtuais.ConexaoAtual()
  try:
    conexoes.deletarConexao(ipCliente, portaCliente)
  except Exception, err:
    sys.stderr.write('EXCEÇÃO: %s\n' % str(err)) 
  if (conexoes.getClientesAtivos() != respostaEsperadaCliente):
    print "testeDeletarConexao", ipCliente, portaCliente,  "falhou, resposta esperada: ", respostaEsperadaCliente, " resposta dada: ", conexoes.getClientesAtivos()
  if(conexoes.getRoteadoresAtivos() != respostaEsperadaRot):
    print "testeDeletarConexao", ipCliente, portaCliente, "falhou, resposta esperada: ", respostaEsperadaRot, " resposta dada: ", conexoes.getRoteadoresAtivos()
