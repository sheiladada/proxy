#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import tabClasseRot

#Testes adicionarRotClasse, deletarRotClasse, listarRotClasse

def testeAdicionarRotClasse(self, classeIP, IPRoteador, tabelaEsperada):
  tabela = tabClasseRot.TabelaClasseRoteador()
  tabela.adicionarRotClasse(classeIP, IPRoteador)
  if tabela.getTabClasseRot() != tabelaEsperada:
    print "testeAdicionarRotClasse", classeIP, IPRoteador, "falhou, resposta esperada:", tabelaEsperada, "resposta dada:", tabela.getTabClasseRot()

def testeDeletarRotClasse(self, classeIP, IPRoteador, tabelaEsperada):
  tabela = tabClasseRot.TabelaClasseRoteador()
  tabela.deletarRotClasse(classeIP, IPRoteador)
  if tabela.getTabClasseRot() != tabelaEsperada:
    print "testeDeletarRotClasse", classeIP, IPRoteador, "falhou, resposta esperada:", tabelaEsperada, "resposta dada:", tabela.getTabClasseRot()

def testeListarRotClasse(self, classeIP, listaEsperada):
  tabela = tabClasseRot.TabelaClasseRoteador()
  listaObtida = tabela.listarRotClasse(classeIP)
  if listaObtida != tabelaEsperada:
    print "testeListarRotClasse", classeIP, IPRoteador, "falhou, resposta esperada:", tabelaEsperada, "resposta dada:", tabela.getTabClasseRot()
