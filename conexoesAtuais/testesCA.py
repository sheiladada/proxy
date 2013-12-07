#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import testesfuncoesCA

#conexões ativas: '10.0.0.1', 11111, '192.168.0.1', '192.168.0.2', 22222, 33333;
#10.0.0.1', 11112, '192.168.0.1', '192.168.0.2', 22221, 33333
#{'192.168.0.2': [22222, 22221]}

#adicionarConexao(self, ipCliente, ipRoteadorOrigem, portaRoteadorOrigem ipRoteadorDestino, portaRoteadorDestino, ipClienteDestino, portaClienteDestino)
respostaEsperadaCliente = {'10.0.0.1': {'192.168.0.1':{ 44444:[ '192.168.0.2', 22222,'10.0.1.1', 33333]}}}
respostaEsperadaRot = {'192.168.0.2': [22222], '192.168.0.1':[44444]}
testesfuncoesCA.testeAdicionarConexao('10.0.0.1', '192.168.0.1',44444, '192.168.0.2', 22222,'10.0.1.1', 33333, respostaEsperadaCliente, respostaEsperadaRot)

#adiciona conexão para o mesmo ipcliente com portas dos roteadores diferentes
respostaEsperadaCliente = {'10.0.0.1': {'192.168.0.1':{44441:[ '192.168.0.2', 22221,'10.0.1.1', 33333], 44444: ['192.168.0.2', 22222,'10.0.1.1', 33333]}}}
respostaEsperadaRot = {'192.168.0.2': [22222, 22221],'192.168.0.1':[44444,44441]}
testesfuncoesCA.testeAdicionarConexao('10.0.0.1','192.168.0.1', 44441,'192.168.0.2', 22221,'10.0.1.1', 33333, respostaEsperadaCliente, respostaEsperadaRot)

#adiciona conexão para a mesma porta roteador cliente, deve dar exceção
respostaEsperadaCliente = {'10.0.0.1': {'192.168.0.1':{44441:[ '192.168.0.2', 22221,'10.0.1.1', 33333], 44444: ['192.168.0.2', 22222,'10.0.1.1', 33333]}}}
respostaEsperadaRot = {'192.168.0.2': [22222, 22221],'192.168.0.1':[44444,44441]}
testesfuncoesCA.testeAdicionarConexao('10.0.0.1', '192.168.0.1',44444, '192.168.0.2', 22223,'10.0.1.1', 33333, respostaEsperadaCliente, respostaEsperadaRot)

#adiciona conexão para a mesma porta roteador destino, deve dar exceção
respostaEsperadaCliente = {'10.0.0.1': {'192.168.0.1':{44441:[ '192.168.0.2', 22221,'10.0.1.1', 33333], 44444: ['192.168.0.2', 22222,'10.0.1.1', 33333]}}}
respostaEsperadaRot = {'192.168.0.2': [22222, 22221],'192.168.0.1':[44444,44441]}
testesfuncoesCA.testeAdicionarConexao('10.0.0.1', '192.168.0.1',44442, '192.168.0.2', 22221,'10.0.1.1', 33333, respostaEsperadaCliente, respostaEsperadaRot)

#deleta conexão normalmente
respostaEsperadaCliente = {'10.0.0.1': {'192.168.0.1':{44441:[ '192.168.0.2', 22221,'10.0.1.1', 33333]}}}
respostaEsperadaRot = {'192.168.0.2': [22221],'192.168.0.1':[44441]}
testesfuncoesCA.testeDeletarConexao('10.0.0.1', '192.168.0.1', 44444, respostaEsperadaCliente, respostaEsperadaRot)

#deleta conexão com porta roteador cliente que não está no dicionário
respostaEsperadaCliente = {'10.0.0.1': {'192.168.0.1':{44441:[ '192.168.0.2', 22221,'10.0.1.1', 33333]}}}
respostaEsperadaRot = {'192.168.0.2': [22221],'192.168.0.1':[44441]}
testesfuncoesCA.testeDeletarConexao('10.0.0.1','192.168.0.1', 44444, respostaEsperadaCliente, respostaEsperadaRot)

#deleta conexão com ip cliente que não está no dicionário
respostaEsperadaCliente = {'10.0.0.1': {'192.168.0.1':{44441:[ '192.168.0.2', 22221,'10.0.1.1', 33333]}}}
respostaEsperadaRot = {'192.168.0.2': [22221],'192.168.0.1':[44441]}
testesfuncoesCA.testeDeletarConexao('10.0.0.2', '192.168.0.2', 44441, respostaEsperadaCliente, respostaEsperadaRot)

#deleta última conexão
respostaEsperadaCliente = {}
respostaEsperadaRot = {}
testesfuncoesCA.testeDeletarConexao('10.0.0.1', '192.168.0.1',44441, respostaEsperadaCliente, respostaEsperadaRot)
