#!/usr/bin/env python
# -*- coding: utf-8 -*- 

f = open('arquivo','a')

ipO = '10.0.0.1'
rotO = '192.168.0.200'
portaLO = 222222
rotD = '192.168.0.100'
portaLD = 44444

comandoRO = ["iptables -t -nat -A PREROUTING -s " + ipO + " -d " + rotO + " -p tcp  --dport " + str(portaLO) + " -i $GREEN_DEV -j DNAT --to " + rotD + ":" + str(portaLD), "iptables -t -nat -A POSTROUTING -s " + ipO + " -d " + rotD + " -p tcp -o $RED_DEV -j SNAT --to-source " + rotO]

finalInsercao = ''
for comando in comandoRO:
  finalInsercao = finalInsercao + '\n' + comando

f.write(finalInsercao)
print "FIM DA EXECUCAO, PODE IR PROCURAR O ARQUIVO NA PASTA"

f.close()


