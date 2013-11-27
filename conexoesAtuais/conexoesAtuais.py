#!/usr/bin/env python
# -*- coding: utf-8 -*- 

class ConexaoAtual:
  
  __clientesAtivos = {}
  __roteadoresAtivos = {}

#  def __init__():

#FALTA AQUI IP CLIENTE DESTINO
  def adicionarConexao(self, ipCliente, portaCliente, ipRoteadorOrigem, ipRoteadorDestino, portaRoteadorDestino, portaClienteDestino):

    #tem a chave, esse cliente já possui
    if self.__clientesAtivos.get(ipCliente) is not None and self.__clientesAtivos[ipCliente].has_key(portaCliente):
      raise RuntimeError('Porta do cliente ocupada.')
    elif not self.__clientesAtivos.has_key(ipCliente):
      self.__clientesAtivos[ipCliente]={}

    #ou não tem a chave cliente no primeiro dicionario ou não tem a porta cliente
    #Ver se a porta ativa do roteador não é a mesma que eu quero colocar, se for, não adiciona nada
    if self.__roteadoresAtivos.has_key(ipRoteadorDestino):
      #lista de portas que estão sendo usadas
      for porta in self.__roteadoresAtivos[ipRoteadorDestino]: 
        if porta == portaRoteadorDestino:
          raise RuntimeError('Porta do roteador destino ocupada.')
    else:
      self.__roteadoresAtivos[ipRoteadorDestino] = []
      #a porta não foi utilizada, adiciono nas portas ativas do roteador e adiciono a conexão nos clientes ativos
    self.__roteadoresAtivos[ipRoteadorDestino].append(portaRoteadorDestino)
    self.__clientesAtivos[ipCliente][portaCliente] = [ipRoteadorOrigem, ipRoteadorDestino, portaRoteadorDestino, portaClienteDestino]

  def deletarConexao(self, ipCliente, portaCliente):

    if not self.__clientesAtivos.has_key(ipCliente):
      raise RuntimeError('Não existe conexão para este IP Cliente.')
    elif not self.__clientesAtivos[ipCliente].has_key(portaCliente):
      raise RuntimeError('Não existe conexão para este para esta porta de IP Cliente.')
    else:
      #Conexão caracterizada por: {'10.0.0.1': {11112: ['192.168.0.1', '192.168.0.2', 22221, 33333]}}, 22221 é a porta do roteador destino
      ipRoteador = self.__clientesAtivos[ipCliente][portaCliente][1]
      portaRoteador =  self.__clientesAtivos[ipCliente][portaCliente][2]
      if not self.__roteadoresAtivos.has_key(ipRoteador):
        raise RuntimeError('Não existe conexão para o IP roteador especificado, inconsistência de dados.')
      elif not portaRoteador in self.__roteadoresAtivos[ipRoteador]:
        raise RuntimeError('Não existe conexão para a porta do roteador especificado, inconsistência de dados.')
      else:
        self.__roteadoresAtivos[ipRoteador].remove(portaRoteador)
        #lista vazia, apaga a chave do roteador
        if not self.__roteadoresAtivos[ipRoteador]:
          del self.__roteadoresAtivos[ipRoteador]
        #apaga a entrada do dicionario da porta cliente
        del self.__clientesAtivos[ipCliente][portaCliente]
        #lista vazia, apaga a chave do cliente
        if not self.__clientesAtivos[ipCliente]:
          del self.__clientesAtivos[ipCliente]

  def getRoteadoresAtivos(self):
    return self.__roteadoresAtivos

  def getClientesAtivos(self):
    return self.__clientesAtivos