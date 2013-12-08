#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import cmdRoteador

def encontra(listaPortas, conexaoSSH):
  portaMin = 10000
  portaMax = 49151
  cmdRot = cmdRoteador.CmdRot()
  if not listaPortas: 
    portaL = portaMin
  else:
    portaOcp = listaPortas.pop()
    if portaOcp == portaMax:
      portaL = portaMin
    else:
      portaL = portaOcp + 1
    if portaL in listaPortas:
      return None
    else:
      if cmdRot.portaLivre(portaL, conexaoSSH):
        return portaL
  return None
