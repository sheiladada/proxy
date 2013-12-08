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

  def insereRegras(self, ipO,rotO,portaLO,rotD, portaLD, ipD,portaD, sshO, sshD):

    arqIptables = '/etc/rc.d/rc.local'
    comandoRO = ["iptables -t -nat -A PREROUTING -s " + ipO + " -d " + rotO + "-p tcp  --dport " + portaLO + " -i $GREEN_DEV -j DNAT --to " + rotD + ":" + portaLD, "iptables -t -nat -A POSTROUTING -s " + ipO + " -d " + rotD + "-p tcp -o $RED_DEV -j SNAT --to-source " + rotO]
    comandoRD = ["iptables -t -nat -A PREROUTING -s " + rotO + " -d " + rotD + "-p tcp  --dport " + portaLD + " -i $RED_DEV -j DNAT --to " + ipD + ":" + portaD, "iptables -t -nat -A POSTROUTING -s " + rotO + " -d " + ipD + "-p tcp -o $GREEN_DEV -j SNAT --to-source " + rotD]

    for idx, comando in comandoRO:
      sshO.exec_command(comando)
      comandoRO[idx] = comando.replace('iptables', '$IPT')

    for idx, comando in comando RD:
      sshD.exec_command(comando)
      comandoRO[idx] = comando.replace('iptables', '$IPT')

    ftpO = sshO.open_sftp()
    ftpO.get(arqIptables, ipO)
    #abrir arquivo, editar e fechar
    ftpO.put(ipO, arqIptables)
    ftpO.close()
	#get coloca no remoto para o local
	#esse pega o teste local e bota la
	#ftp.put('teste','/etc/rc.d/rc.local')
	ftp.get('/etc/rc.d/rc.local', 'arquivo')
    ftp.close()

