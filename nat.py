#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#COMO FAZER PARA IMPORTAR TUDO SE ELES NÃO ESTÃO NA MESMA PASTA
import netaddr
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

    listaRotPorta = []
    tabelaClRot = tabClasseRot.TabelaClasseRoteador()

    ipOrg = netaddr.IPNetwork(ipOrigem)
    rotOrgs = tabelaClRot.get(str(ipOrg.network))

    # não existe classe perto para este roteador, FAZER
    if not rotOrgs:
      raise RuntimeError("Não há roteadores próximos ao roteador cliente para esta topologia de rede.")
    else:
      for rotOrg in rotOrgs:
        try:
          listaRotPorta = self.geraRegras(str(ipOrg.ip),listaDestino, rotOrg)
          if listaRotPorta:
            break
        except RuntimeError, err:
          sys.stderr.write('EXCEÇÃO: %s\n' % str(err))
        except:
          #deixa passar as outras exceções para rodar todos os rotProximos que existem
           pass 
    return listaRotPorta

  def geraRegras(self, ipOrigem, listaDestino, rotO):

    listaRotPorta = []
    conexoes = conexoesAtuais.ConexaoAtual()
    tabelaClRot = tabClasseRot.TabelaClasseRoteador()
    # cmdRot faz comandos no roteador
    cmdRot = cmdRoteador.CmdRot()
    #conexao ssh, considera que todos os roteadores já estão conectados
    sshConexao = ssh.Ssh()

    sshRotO = sshConexao.getConexao(rotO)
    #lista de IP destinos e porta destinos próximas
    #para cada porta destino encontro o IP de saída próximo
    for ipDestino, portaDst in listaDestino:
      #dessa maneira, todos estarão vinculados ao mesmo IP roteador próximo ao cliente e porta destino diferente
      portaLO = portaLivre.encontra(conexoes.getRoteadoresAtivos().get(rotO), sshRotO)
      if portaLO:
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
              conexoes.adicionarConexao(ipOrigem,rotO,portaLO,rotProxDst, portaLD, str(ipDst.ip),portaDst)
              acao = '-A'
              cmdRot.escreveRegras(ipOrigem,rotO,portaLO,rotProxDst, portaLD, str(ipDst.ip),portaDst, sshRotO, sshRotD, acao )
              listaRotPorta.append((rotO, portaLO))
              break
      else:
        return []
    return listaRotPorta

  def deletar(self,ipO, listaRotPorta):

    conexoes = conexoesAtuais.ConexaoAtual()
    cmdRot = cmdRoteador.CmdRot()
    sshConexao = ssh.Ssh()

    # sempre vai ser o mesmo rotO, mas vou fazer como se pudesse mudar
    for rotO, portaRO in listaRotPorta:
      #listaConexao volta nessa ordem ipO(0), rotO(1), portaRO(2), rotD(3), portaRD(4), ipD(5), portaD(6)
      elemRede = conexoes.getRoteadorAtivo(ipO, rotO, portaRO)
      sshRotO = sshConexao.getConexao(rotO)
      sshRotD = sshConexao.getConexao(elemRede[3])
      acao = '-D'
      cmdRot.escreveRegras(elemRede[0],elemRede[1],elemRede[2],elemRede[3],elemRede[4],elemRede[5],elemRede[6], sshRotO, sshRotD,acao)
      conexoes.deletarConexao(ipO, rotO, portaRO)








