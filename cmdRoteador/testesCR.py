#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import paramiko
import cmdRoteador

comandos = cmdRoteador.CmdRot()

ipO = '10.0.0.253'
rotO = '192.168.0.69'
portaLO = 33333
rotD = '192.168.0.31'
portaLD = 33331
ipD = '10.0.1.253'
portaD = 33330

sshO = paramiko.SSHClient()
sshO.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshO.connect(rotO,port=222,username='root',password='Iptv092012')

sshD = paramiko.SSHClient()
sshD.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshD.connect(rotD,port=222,username='root',password='Iptv092012')

comandos.escreveRegras(ipO,rotO,portaLO,rotD, portaLD, ipD,portaD, sshO, sshD, '-A')
comandos.escreveRegras(ipO,rotO,portaLO,rotD, portaLD, ipD,portaD, sshO, sshD, '-D')
# No fim vou ter regras no roteador cliente:
#"iptables -t -nat -A PREROUTING -s 10.0.0.253 -d 192.168.0.69 -p tcp  --dport 33333 -i $GREEN_DEV -j DNAT --to 192.168.0.31:33331"
#"iptables -t -nat -A POSTROUTING -s 10.0.0.253 -d 192.168.0.31 -p tcp -o $RED_DEV -j SNAT --to-source 192.168.0.69"

#Vou ter no roteador destino:
#"iptables -t -nat -A PREROUTING -s 192.168.0.69 -d 192.168.0.31 -p tcp  --dport 33331 -i $RED_DEV -j DNAT --to 10.0.1.253:33330" 
#"iptables -t -nat -A POSTROUTING -s 192.168.69 -d 10.0.1.253 -p tcp -o $GREEN_DEV -j SNAT --to-source 192.168.0.31"
