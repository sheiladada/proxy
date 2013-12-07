#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import ssh
import paramiko

def conexaoSsh(ip, usuario, senha, palavraEsperada):
  conexao = ssh.Ssh()
  conexao.adicionar(ip, usuario, senha)
  enviaEcho(ip, palavraEsperada )


def enviaEcho(ip, palavraEsperada):
  conexao = ssh.Ssh()
  conexaoFeita = conexao.getConexao(ip)
  stdin, stdout, stderr = conexaoFeita.exec_command("echo \"" + palavraEsperada + "\"")
  palavraDada = stdout.readlines()
  palavraFinal = palavraDada[0].replace('\n','')
  if palavraFinal != palavraEsperada:
    print palavraFinal
    print palavraEsperada
    print "Teste ssh falhou."

#Faltam mais testes aqui que não entram no escopo do projeto, por isso não estão inclusos.
