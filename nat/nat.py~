#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#COMO FAZER PARA IMPORTAR TUDO SE ELES NÃO ESTÃO NA MESMA PASTA
import netaddr
import difflib
import random
import conexoesAtuais
import tabClasseRot
import paramiko
import cmdRoteador

class Nat:

  #portas minimas e máximas para serem usadas como porta
  __portaMin = 10000
  __portaMax = 49151
#cria a conexão nat com todos e devolve lista de roteadores
#precisa passar no ipOrigem e lista destino o IP e a máscara
  def criar(self, ipOrigem, portaOrigem, listaDestino):
    rotDestino = []
    conexoes = conexoesAtuais.ConexaoAtual()
    tabelaClRot = tabClasseRot.TabelaClasseRoteador()
    # cmdRot faz comandos no roteador
    cmdRot = cmdRoteador.CmdRot()
    ipOrg = netaddr.IPNetwork(ipOrigem)
    rotProximos = tabelaClRot.get(str(ipOrg.network))
    # não existe classe perto para este roteador, FAZER
    if not rotProximos:
      #>>> seq = difflib.SequenceMatcher(a = a.lower(),b = b.lower())
      #>>> seq.ratio()
      #ESCREVER O QUE FAZER SE NÃO TEM UM ROTEADOR PRÓXIMO
    else:
    #portas de 10000 a 49151
    #essas são os roteadores dos clientes, faço isso para caso a conexão com ele não der certo, ir para o próximo
      for rotProximo in rotProximos:
        #VER PORTAS LIVRES AQUI, SE NÃO TEM LIVRE, JÁ PULA PARA O PROXIMO rotProximo
        #lista de IP destinos e porta destinos próximas
        #para cada porta destino encontro o IP de saída próximo
        for ipDestino, portaDst in listaDestino:
          # ACHO QUE AQUI PRECISA ANALISAR A PORTA LIVRE DO ROTEADOR MAIS PRÓXIMO
          # lista de roteadores próximos ao ip destino
          ipDst = netaddr.IPNetwork(ipDestino)
          rotProxDsts = tabelaClRot.get(str(ipDst.network))
          if not rotProxDsts:
            #ESCREVER O QUE FAZER SE NÃO TEM UM ROTEADOR PRÓXIMO
          else:
            # gera a lista
            # faz essa iteração porque pode dar pau no que tentou conectar
            for rotProxDst in rotProxDsts:
              listaPortas = conexoes.getRoteadoresAtivos().get(rotProxDst)
              portaOcp = listaPortas.pop()
              if portaOcp = self.__portaMax:
                portaL = self.__portaMin
              else:
                portaL = portaOcp + 1
              if portaL not in portaOcp:
                  try:
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    #MUDAR A SENHA DEPOIS
                    ssh.connect(str(ipDst.ip),port=portaLivre,username='root',password='root')
                    if not cmdRot.portaLivre(portaL, ssh):
                      raise
                    #adicionarConexao(self, ipCliente, portaCliente, ipRoteadorOrigem,portaRoteadorOrigem(FALTA), ipRoteadorDestino, portaRoteadorDestino, ipClienteDestino, portaClienteDestino)
                    conexoes.adicionarConexao(str(ipOrg.ip), portaOrigem,rotProximo,portaLOrg ,rotProxDst, portaL, str(ipDst.ip),portaDst)
                    # AGORA FAZER OS COMANDOS QUE ADICIONAM O COMANDO IPTABLES
                    
                    # vai quebrar o loop do rotProxDst
                    break
                  except:
                    # para continuar no loop
                    pass
      # deu tudo certo, sai do loop
      rotDestino.append([rotProximo, portaLOrg])
      break
    return rotDestino
