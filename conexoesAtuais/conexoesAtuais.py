#!/usr/bin/env python
# -*- coding: utf-8 -*- 

class ConexaoAtual:
  
  __clientesAtivos = {}
  __roteadoresAtivos = {}

#  def __init__():

  def adicionarConexao(self, ipCliente,ipRoteadorOrigem,portaRO, ipRoteadorDestino, portaRoteadorDestino, ipClienteDestino, portaClienteDestino):

    #tem a chave, esse cliente já possui
    if self.__clientesAtivos.has_key(ipCliente) and self.__clientesAtivos[ipCliente].has_key(ipRoteadorOrigem) and self.__clientesAtivos[ipCliente][ipRoteadorOrigem].has_key(portaRO):
      raise RuntimeError('Conexão já existente.')

    if not self.__clientesAtivos.has_key(ipCliente):
      self.__clientesAtivos[ipCliente]={}
    if not self.__clientesAtivos[ipCliente].has_key(ipRoteadorOrigem):
      self.__clientesAtivos[ipCliente][ipRoteadorOrigem] = {}
    #ou não tem a chave cliente no primeiro dicionario ou não tem a porta cliente
    #Ver se a porta ativa do roteador não é a mesma que eu quero colocar, se for, não adiciona nada
    if self.__roteadoresAtivos.has_key(ipRoteadorDestino):
      #lista de portas que estão sendo usadas
      for porta in self.__roteadoresAtivos[ipRoteadorDestino]: 
        if porta == portaRoteadorDestino:
          raise RuntimeError('Porta do roteador destino ocupada.')
    else:
      self.__roteadoresAtivos[ipRoteadorDestino] = []

    if self.__roteadoresAtivos.has_key(ipRoteadorOrigem):
      #lista de portas que estão sendo usadas
      for porta in self.__roteadoresAtivos[ipRoteadorOrigem]: 
        if porta == portaRO:
          raise RuntimeError('Porta do roteador origem ocupada.')
    else:
      self.__roteadoresAtivos[ipRoteadorOrigem] = []
      #a porta não foi utilizada, adiciono nas portas ativas do roteador e adiciono a conexão nos clientes ativos
    self.__roteadoresAtivos[ipRoteadorDestino].append(portaRoteadorDestino)
    self.__roteadoresAtivos[ipRoteadorOrigem].append(portaRO)
    self.__clientesAtivos[ipCliente][ipRoteadorOrigem][portaRO] =[ipRoteadorDestino, portaRoteadorDestino, ipClienteDestino, portaClienteDestino]

  def deletarConexao(self, ipCliente, ipRO, portaRO):

    if not self.__clientesAtivos.has_key(ipCliente):
      raise RuntimeError('Não existe conexão para este IP Cliente.')
    elif not self.__clientesAtivos[ipCliente].has_key(ipRO):
      raise RuntimeError('Não existe conexão para este cliente com este ip roteador')
    elif not self.__clientesAtivos[ipCliente][ipRO].has_key(portaRO):
      raise RuntimeError('Não existe conexão para este cliente com o roteador através desta porta destino.')
    else:
      #Conexão caracterizada por: {'10.0.0.1': {'192.168.0.1':{ 44444:[ '192.168.0.2', 22222,'10.0.1.1', 33333]}}}
      ipRoteador = self.__clientesAtivos[ipCliente][ipRO][portaRO][0]
      portaRoteador =  self.__clientesAtivos[ipCliente][ipRO][portaRO][1]
      if not self.__roteadoresAtivos.has_key(ipRoteador):
        raise RuntimeError('Não existe conexão para o IP roteador destino especificado, inconsistência de dados.')
      elif not portaRoteador in self.__roteadoresAtivos[ipRoteador]:
        raise RuntimeError('Não existe conexão para a porta do roteador destino especificado, inconsistência de dados.')
      elif not self.__roteadoresAtivos.has_key(ipRO):
        raise RuntimeError('Não existe conexão para o IP roteador origem especificado, inconsistência de dados.')
      elif not portaRO in self.__roteadoresAtivos[ipRO]:
        raise RuntimeError('Não existe conexão para a porta do roteador origem especificado, inconsistência de dados.')
      else:
        self.__roteadoresAtivos[ipRoteador].remove(portaRoteador)
        self.__roteadoresAtivos[ipRO].remove(portaRO)
        #lista vazia, apaga a chave do roteador
        if not self.__roteadoresAtivos[ipRoteador]:
          del self.__roteadoresAtivos[ipRoteador]
        #lista vazia, apaga a chave do roteador
        if not self.__roteadoresAtivos[ipRO]:
          del self.__roteadoresAtivos[ipRO]
        #apaga a entrada do dicionario da porta cliente
        del self.__clientesAtivos[ipCliente][ipRO][portaRO]
        #lista vazia, apaga a chave do cliente
        if not self.__clientesAtivos[ipCliente][ipRO]:
          del self.__clientesAtivos[ipCliente][ipRO]
        if not self.__clientesAtivos[ipCliente]:
          del self.__clientesAtivos[ipCliente]

  def getRoteadoresAtivos(self):
    return self.__roteadoresAtivos

  def getClientesAtivos(self):
    return self.__clientesAtivos
