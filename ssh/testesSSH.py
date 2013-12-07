#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import testesfuncoesSSH
import ssh

testesfuncoesSSH.conexaoSsh('192.168.0.31', 'root', 'Iptv092012', "teste1")
testesfuncoesSSH.conexaoSsh('192.168.0.69', 'root', 'Iptv092012', "teste2")
testesfuncoesSSH.enviaEcho('192.168.0.31', 'teste3')
testesfuncoesSSH.enviaEcho('192.168.0.69', 'teste4')

conexao = ssh.Ssh()
conexao.fecharTodos()
