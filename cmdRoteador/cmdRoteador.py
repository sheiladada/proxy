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

  def insereRegras(self, )
