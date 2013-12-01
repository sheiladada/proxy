#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import testesfuncoesCA

#conexões ativas: '10.0.0.1', 11111, '192.168.0.1', '192.168.0.2', 22222, 33333;
#10.0.0.1', 11112, '192.168.0.1', '192.168.0.2', 22221, 33333
#{'192.168.0.2': [22222, 22221]}

#adicionarConexao(self, ipCliente, portaCliente, ipRoteadorOrigem, ipRoteadorDestino, portaRoteadorDestino, ipClienteDestino, portaClienteDestino)
respostaEsperadaCliente = {'10.0.0.1': {11111: ['192.168.0.1', 44444, '192.168.0.2', 22222,'10.0.1.1', 33333]}}
respostaEsperadaRot = {'192.168.0.2': [22222], '192.168.0.1':[44444]}
testesfuncoesCA.testeAdicionarConexao('10.0.0.1', 11111, '192.168.0.1',44444, '192.168.0.2', 22222,'10.0.1.1', 33333, respostaEsperadaCliente, respostaEsperadaRot)

#adiciona conexão para o mesmo ipcliente com porta do cliente diferente e porta do roteador destino diferente
respostaEsperadaCliente = {'10.0.0.1': {11112: ['192.168.0.1',44441, '192.168.0.2', 22221,'10.0.1.1', 33333], 11111: ['192.168.0.1',44444, '192.168.0.2', 22222,'10.0.1.1', 33333]}}
respostaEsperadaRot = {'192.168.0.2': [22222, 22221],'192.168.0.1':[44444,44441]}
testesfuncoesCA.testeAdicionarConexao('10.0.0.1', 11112, '192.168.0.1', 44441,'192.168.0.2', 22221,'10.0.1.1', 33333, respostaEsperadaCliente, respostaEsperadaRot)

#adiciona conexão para a mesma porta cliente, deve dar exceção
respostaEsperadaCliente = {'10.0.0.1': {11112: ['192.168.0.1',44441, '192.168.0.2', 22221,'10.0.1.1', 33333], 11111: ['192.168.0.1',44444, '192.168.0.2', 22222,'10.0.1.1', 33333]}}
respostaEsperadaRot = {'192.168.0.2': [22222, 22221],'192.168.0.1':[44444,44441]}
testesfuncoesCA.testeAdicionarConexao('10.0.0.1', 11111, '192.168.0.1',44442, '192.168.0.2', 22223,'10.0.1.1', 33333, respostaEsperadaCliente, respostaEsperadaRot)

#adiciona conexão para a mesma porta roteador destino, deve dar exceção
respostaEsperadaCliente = {'10.0.0.1': {11112: ['192.168.0.1',44441, '192.168.0.2', 22221,'10.0.1.1', 33333], 11111: ['192.168.0.1',44444, '192.168.0.2', 22222,'10.0.1.1', 33333]}}
respostaEsperadaRot = {'192.168.0.2': [22222, 22221],'192.168.0.1':[44444,44441]}
testesfuncoesCA.testeAdicionarConexao('10.0.0.1', 11113, '192.168.0.1',44443, '192.168.0.2', 22221,'10.0.1.1', 33333, respostaEsperadaCliente, respostaEsperadaRot)

#adiciona conexão para a mesma porta roteador cliente, deve dar exceção
respostaEsperadaCliente = {'10.0.0.1': {11112: ['192.168.0.1',44441, '192.168.0.2', 22221,'10.0.1.1', 33333], 11111: ['192.168.0.1',44444, '192.168.0.2', 22222,'10.0.1.1', 33333]}}
respostaEsperadaRot = {'192.168.0.2': [22222, 22221],'192.168.0.1':[44444,44441]}
testesfuncoesCA.testeAdicionarConexao('10.0.0.1', 11114, '192.168.0.1',44441, '192.168.0.2', 22224,'10.0.1.1', 33333, respostaEsperadaCliente, respostaEsperadaRot)

#deleta conexão normalmente
respostaEsperadaCliente = {'10.0.0.1': {11112: ['192.168.0.1',44441, '192.168.0.2', 22221,'10.0.1.1', 33333]}}
respostaEsperadaRot = {'192.168.0.2': [22221],'192.168.0.1':[44441]}
testesfuncoesCA.testeDeletarConexao('10.0.0.1', 11111, respostaEsperadaCliente, respostaEsperadaRot)

#deleta conexão com porta que não está no dicionário
respostaEsperadaCliente = {'10.0.0.1': {11112: ['192.168.0.1',44441, '192.168.0.2', 22221,'10.0.1.1', 33333]}}
respostaEsperadaRot = {'192.168.0.2': [22221],'192.168.0.1':[44441]}
testesfuncoesCA.testeDeletarConexao('10.0.0.1', 11113, respostaEsperadaCliente, respostaEsperadaRot)

#deleta conexão com ip cliente que não está no dicionário
respostaEsperadaCliente = {'10.0.0.1': {11112: ['192.168.0.1',44441, '192.168.0.2', 22221,'10.0.1.1', 33333]}}
respostaEsperadaRot = {'192.168.0.2': [22221],'192.168.0.1':[44441]}
testesfuncoesCA.testeDeletarConexao('10.0.0.2', 11113, respostaEsperadaCliente, respostaEsperadaRot)

#deleta conexão com porta que não está no dicionário
respostaEsperadaCliente = {}
respostaEsperadaRot = {}
testesfuncoesCA.testeDeletarConexao('10.0.0.1', 11112, respostaEsperadaCliente, respostaEsperadaRot)
