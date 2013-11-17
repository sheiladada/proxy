#!/usr/bin/env python
# -*- coding: utf-8 -*- 

class ConexaoAtual:
  
  __clientesAtivos = {}
  __roteadoresAtivos = {}

#  def __init__():

  def adicionarConexao(self, ipCliente, portaCliente, ipRoteadorOrigem, ipRoteadorDestino, portaRoteadorDestino, portaClienteDestino):

    #tem a chave, esse cliente já possui
    try:
      if self.__clientesAtivos.get(ipCliente) is not None and self.__clientesAtivos[ipCliente].has_key(portaCliente):
        raise ClienteOcupadoErro
      elif not self.__clientesAtivos.has_key(ipCliente):
        self.__clientesAtivos[ipCliente]={}

      # ou não tem a chave cliente no primeiro dicionario ou não tem a porta cliente
      # Ver se a porta ativa do roteador não é a mesma que eu quero colocar, se for, não adiciona nada
      if self.__roteadoresAtivos.has_key(ipRoteadorDestino):
        #lista de portas que estão sendo usadas
        for porta in self.__roteadoresAtivos[ipRoteadorDestino]: 
          if porta == portaRoteadorDestino:
            raise DestinoOcupadoErro
      else:
        self.__roteadoresAtivos[ipRoteadorDestino] = []
        #a porta não foi utilizada, adiciono nas portas ativas do roteador e adiciono a conexão nos clientes ativos
      self.__roteadoresAtivos[ipRoteadorDestino].append(portaRoteadorDestino)
      self.__clientesAtivos[ipCliente][portaCliente] = [ipRoteadorOrigem, ipRoteadorDestino, portaRoteadorDestino, portaClienteDestino]
    except ClienteOcupadoErro:
      print ("Porta do cliente ocupada.")
    except DestinoOcupadoErro:
      print ("Porta do roteador destino ocupada.")

  def printRoteadoresAtivos(self):
    print self.__roteadoresAtivos

  def printClientesAtivos(self):
    print self.__clientesAtivos
