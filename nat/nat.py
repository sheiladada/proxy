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
import ssh
import portaLivre

class Nat:

  #portas minimas e máximas para serem usadas como porta
#  __portaMin = 10000
#  __portaMax = 49151
#cria a conexão nat com todos e devolve lista de roteadores
#precisa passar no ipOrigem e lista destino o IP e a máscara
  def criar(self, ipOrigem, listaDestino):

    rotDestino = []

    conexoes = conexoesAtuais.ConexaoAtual()
    tabelaClRot = tabClasseRot.TabelaClasseRoteador()
    # cmdRot faz comandos no roteador
    cmdRot = cmdRoteador.CmdRot()
    #conexao ssh, considera que todos os roteadores já estão conectados
    sshConexao = ssh.Ssh()

    ipOrg = netaddr.IPNetwork(ipOrigem)
    rotProximos = tabelaClRot.get(str(ipOrg.network))

    # não existe classe perto para este roteador, FAZER
    if not rotProximos:
      raise RuntimeError("Não há roteadores próximos ao roteador cliente para esta topologia de rede.")
    else:
      for rotProximo in rotProximos:
        geraRegras(rotProximo)

                      # vai quebrar o loop do rotProxDst
                      break
                    except:
                      # para continuar no loop
                      pass
        # deu tudo certo, sai do loop
      rotDestino.append([rotProximo, portaLOrg])
      break
    return rotDestino

  def geraRegras(self, ipOrigem, listaDestino, rotO):

    rotDestino = []
    conexoes = conexoesAtuais.ConexaoAtual()
    tabelaClRot = tabClasseRot.TabelaClasseRoteador()
    # cmdRot faz comandos no roteador
    cmdRot = cmdRoteador.CmdRot()
    #conexao ssh, considera que todos os roteadores já estão conectados
    sshConexao = ssh.Ssh()

    sshRotO = sshConexao.getConexao(rotO)
    portaLO = portaLivre.encontra(conexoes.getRoteadoresAtivos().get(rotO), sshRotO)
    if portaLO:
      #lista de IP destinos e porta destinos próximas
      #para cada porta destino encontro o IP de saída próximo
      for ipDestino, portaDst in listaDestino:
        ipDst = netaddr.IPNetwork(ipDestino)
        rotProxDsts = tabelaClRot.get(str(ipDst.network))
        if not rotProxDsts:
          raise RuntimeError("Não há roteadores próximos ao roteador destino para esta topologia de rede.")
        else:
          # gera a lista
          # faz essa iteração porque pode dar pau no que tentou conectar
          for rotProxDst in rotProxDsts:
            sshRotD = sshConexao.getConexao(rotProxDst)
            portaLD = portaLivre.encontra(conexoes.getRoteadoresAtivos().get(rotProxDst), sshRotD)
            if portaLD:
              #adicionarConexao(ipCliente,ipRoteadorOrigem,portaRO, ipRoteadorDestino, portaRoteadorDestino, ipClienteDestino, portaClienteDestino)
              try:
                conexoes.adicionarConexao(str(ipOrg.ip),rotProximo,portaLO,rotProxDst, portaLD, str(ipDst.ip),portaDst)
                # AGORA FAZER OS COMANDOS QUE ADICIONAM O COMANDO IPTABLES
              except:
                  raise RuntimeError("Não foi possível realizar a conexão ssh.")
        rotDestino.append([rotProximo, portaLOrg])
      return rotDestino
    return []
