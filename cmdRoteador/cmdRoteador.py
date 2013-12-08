#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import re

class CmdRot():

  def portaLivre(self, porta, ssh):
    stdin, stdout, stderr = ssh.exec_command("netstat -anpt")
    stdin.close()
    ipPortas = stdout.readlines()
    listaPorta = []
    for ipPorta in ipPortas:
      # ipPorta contém o ip e a porta 
      listaIpPorta = ipPorta.split()
      portaOcp = re.match(r"^([0-9]{1,3}\.){3}([0-9]{1,3}):([0-9]+)",listaIpPorta[3])
      if portaOcp:
        listaPorta.append(int(portaOcp.group(3)))
    if porta in listaPorta:
      return False
    else:
      return True

  def insereRegras(self, comandos, ssh, rot):

    # comandos que irão escrever no arquivo do iptables
    comandosArq = ''
    arqIptables = '/etc/rc.d/rc.local'

    for comando in comandos:
      ssh.exec_command(comando)
      comandoArq = comando.replace('iptables', '$IPT')
      comandosArq = comandosArq + '\n' + comandoArq

    ftp = ssh.open_sftp()
    ftp.get(arqIptables, rot)
    #abrir arquivo, editar e fechar
    f = open(rot,'a')
    f.write(comandosArq)
    f.close()
    ftp.put(rot, arqIptables)
    ftp.close()

  def escreveRegras(self, ipO,rotO,portaLO,rotD, portaLD, ipD,portaD, sshO, sshD):

    arqIptables = '/etc/rc.d/rc.local'

    comandoRO = ["iptables -t -nat -A PREROUTING -s " + ipO + " -d " + rotO + " -p tcp  --dport " + str(portaLO) + " -i $GREEN_DEV -j DNAT --to " + rotD + ":" + str(portaLD), "iptables -t -nat -A POSTROUTING -s " + ipO + " -d " + rotD + " -p tcp -o $RED_DEV -j SNAT --to-source " + rotO]
    comandoRD = ["iptables -t -nat -A PREROUTING -s " + rotO + " -d " + rotD + " -p tcp  --dport " + str(portaLD) + " -i $RED_DEV -j DNAT --to " + ipD + ":" + str(portaD), "iptables -t -nat -A POSTROUTING -s " + rotO + " -d " + ipD + " -p tcp -o $GREEN_DEV -j SNAT --to-source " + rotD]

    self.insereRegras(comandoRO, sshO, rotO)
    self.insereRegras(comandoRD, sshD, rotD)


