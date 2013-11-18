#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import testesfuncoesTCR

tabelaEsperada = {'10.0.0.0':['192.168.0.1']}
testesfuncoesTCR.testeAdicionarRotClasse('10.0.0.0', '192.168.0.1', tabelaEsperada)

tabelaEsperada = {'10.0.0.0':['192.168.0.1', '192.168.0.2']}
testesfuncoesTCR.testeAdicionarRotClasse('10.0.0.0', '192.168.0.2', tabelaEsperada)

#adicionar um elemento já existente
tabelaEsperada = {'10.0.0.0':['192.168.0.1', '192.168.0.2']}
testesfuncoesTCR.testeAdicionarRotClasse('10.0.0.0', '192.168.0.1', tabelaEsperada)

tabelaEsperada = {'10.0.1.0':['192.168.0.1'], '10.0.0.0':['192.168.0.1', '192.168.0.2']}
testesfuncoesTCR.testeAdicionarRotClasse('10.0.1.0', '192.168.0.1', tabelaEsperada)

listaEsperada = ['192.168.0.1', '192.168.0.2']
testesfuncoesTCR.testeListarRotClasse( '10.0.0.0', listaEsperada)

listaEsperada = []
testesfuncoesTCR.testeListarRotClasse( '10.0.0.3', listaEsperada)

tabelaEsperada = {'10.0.0.0':['192.168.0.1', '192.168.0.2']}
testesfuncoesTCR.testeDeletarRotClasse('10.0.1.0', '192.168.0.1', tabelaEsperada)

tabelaEsperada = {'10.0.0.0':['192.168.0.2']}
testesfuncoesTCR.testeDeletarRotClasse('10.0.0.0', '192.168.0.1', tabelaEsperada)

