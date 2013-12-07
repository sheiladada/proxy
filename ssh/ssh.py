#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import paramiko

class Ssh():

  __conexaoSsh = {}

  def adicionar(self, ip, senha, usuario):
    if self.__conexaoSsh.has_key(ip):
      self.conexaoSsh[ip][2].close()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port=222,username=usuario,password=senha)
    conexaoSsh[ip]=[usuario, senha, ssh]

  def fechar(self, ip):
    self.conexaoSsh[ip][2].close()
    del conexaoSsh[ip]

  def fecharTodos(self):
    for senha, usuario, conexao in self.__conexaoSsh.values():
      conexao.close()
    self.__conexaoSsh = {}

  def getConexoes(self):
    return self.__conexaoSsh

  def getConexao(self, ip):
    return return self.__conexaoSsh[ip][2]

