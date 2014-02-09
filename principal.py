#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import nat
import tabClasseRot
import netaddr

fazerNat = nat.Nat()
tabelaCR = tabClasseRot.TabelaClasseRoteador()
# classeIP, IPRoteador
tabelaCR.adicionarRotClasse('10.0.0.253', '192.168.0.69')
tabelaCR.adicionarRotClasse('10.0.1.253', '192.168.0.31')

ipOrigem = '10.0.0.253/24'
listaDestino = [('10.0.1.253/24', 11111)]

fazerNat.criar(ipOrigem, listaDestino)




