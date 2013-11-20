#!/usr/bin/env python
# -*- coding: utf-8 -*- 

class TabelaClasseRoteador():

  __tabelaClasseRot = {}

  def adicionarRotClasse(self, classeIP, IPRoteador):

    if self.__tabelaClasseRot.has_key(classeIP):
      if IPRoteador in self.__tabelaClasseRot[classeIP]:
        print "O IPRoteador", IPRoteador, "já foi adicionado à classe", classeIP, "."
      else:
        self.__tabelaClasseRot[classeIP].append(IPRoteador)
    else:
      self.__tabelaClasseRot[classeIP] = [IPRoteador]

  def deletarRotClasse(self, classeIP, IPRoteador):

    listaRot = self.__tabelaClasseRot.get(classeIP)
    if listaRot:
        if IPRoteador in listaRot:
          self.__tabelaClasseRot[classeIP].remove(IPRoteador)
          if not self.__tabelaClasseRot[classeIP]:
            del self.__tabelaClasseRot[classeIP]
        else:
          print "O roteador", IPRoteador, "já foi deletado da lista da classe de IP", classeIP
    else:
      print "Não há registro de roteadores para a classe", classeIP

#  def listarRotClasse(s elf, classeIP):
  def getTabClasseRot(self):
    return self.__tabelaClasseRot
