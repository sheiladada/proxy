#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import testesfuncoes

#conexões ativas: '10.0.0.1', 11111, '192.168.0.1', '192.168.0.2', 22222, 33333;
#10.0.0.1', 11112, '192.168.0.1', '192.168.0.2', 22221, 33333
#{'192.168.0.2': [22222, 22221]}

#adicionarConexao(self, ipCliente, portaCliente, ipRoteadorOrigem, ipRoteadorDestino, portaRoteadorDestino, portaClienteDestino)
respostaEsperadaCliente = {'10.0.0.1': {11111: ['192.168.0.1', '192.168.0.2', 22222, 33333]}}
respostaEsperadaRot = {'192.168.0.2': [22222]}
testesfuncoes.testeAdicionarConexao('10.0.0.1', 11111, '192.168.0.1', '192.168.0.2', 22222, 33333, respostaEsperadaCliente, respostaEsperadaRot)

#adiciona conexão para o mesmo ipcliente com porta do cliente diferente e porta do roteador destino diferente
respostaEsperadaCliente = {'10.0.0.1': {11112: ['192.168.0.1', '192.168.0.2', 22221, 33333], 11111: ['192.168.0.1', '192.168.0.2', 22222, 33333]}}
respostaEsperadaRot = {'192.168.0.2': [22222, 22221]}
testesfuncoes.testeAdicionarConexao('10.0.0.1', 11112, '192.168.0.1', '192.168.0.2', 22221, 33333, respostaEsperadaCliente, respostaEsperadaRot)

#adiciona conexão para a mesma porta cliente, deve dar exceção
respostaEsperadaCliente = {'10.0.0.1': {11112: ['192.168.0.1', '192.168.0.2', 22221, 33333], 11111: ['192.168.0.1', '192.168.0.2', 22222, 33333]}}
respostaEsperadaRot = {'192.168.0.2': [22222, 22221]}
testesfuncoes.testeAdicionarConexao('10.0.0.1', 11111, '192.168.0.1', '192.168.0.2', 22223, 33333, respostaEsperadaCliente, respostaEsperadaRot)

#adiciona conexão para a mesma porta roteador destino, deve dar exceção
respostaEsperadaCliente = {'10.0.0.1': {11112: ['192.168.0.1', '192.168.0.2', 22221, 33333], 11111: ['192.168.0.1', '192.168.0.2', 22222, 33333]}}
respostaEsperadaRot = {'192.168.0.2': [22222, 22221]}
testesfuncoes.testeAdicionarConexao('10.0.0.1', 11113, '192.168.0.1', '192.168.0.2', 22221, 33333, respostaEsperadaCliente, respostaEsperadaRot)

#deleta conexão normalmente
respostaEsperadaCliente = {'10.0.0.1': {11112: ['192.168.0.1', '192.168.0.2', 22221, 33333]}}
respostaEsperadaRot = {'192.168.0.2': [22221]}
testesfuncoes.testeAdicionarConexao('10.0.0.1', 11111, respostaEsperadaCliente, respostaEsperadaRot)

#deleta conexão com porta que não está no dicionário
respostaEsperadaCliente = {'10.0.0.1': {11112: ['192.168.0.1', '192.168.0.2', 22221, 33333]}}
respostaEsperadaRot = {'192.168.0.2': [22221]}
testesfuncoes.testeAdicionarConexao('10.0.0.1', 11113, respostaEsperadaCliente, respostaEsperadaRot)

#deleta conexão com porta que não está no dicionário
respostaEsperadaCliente = {'10.0.0.1': {11112: ['192.168.0.1', '192.168.0.2', 22221, 33333]}}
respostaEsperadaRot = {'192.168.0.2': [22221]}
testesfuncoes.testeAdicionarConexao('10.0.0.1', 11112, respostaEsperadaCliente, respostaEsperadaRot)
