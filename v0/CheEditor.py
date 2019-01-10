#!/usr/bin/python
import os

#variavel que recebe texto digitado
texto=""
#nome do arquivo que vai receber o conteudo
nomearq=""
#var que indica a acao a ser tomada em relacao ao nomearq
gravarsn=""

#inicio do editor
os.system('clear')
print('###############################################')
os.system('figlet Che Editor')
os.system('\n')
print('###############################################')
os.system('\n')
os.system('\n')
nomearq = input("Nome do arquivo: ")
os.system('clear')
texto=""
gravarsn=""

while True:
	linha = input(" > ")
	if linha == ":q":
		break
	texto = texto + linha + "\n"
#ao sair do primeiro loop, exibe o que foi digitado

while True:
	gravarsn=input("(w) substituir arquivo atual || (a) adicionar atual\n (q) sair sem gravar\n: ")
	if gravarsn == "q":
		print("Saindo sem gravar")
		break
	if gravarsn == "w":
		#abre o arquivo e sobreescreve o conteudo
		arq = open(nomearq, "w")
		arq.write(texto)
		arq.close()
		print("Texto substituido")
		break
	if gravarsn == "a":
		#adiciona ao final do arquivo
		arq = open(nomearq, "a")
		arq.write(texto)
		arq.close()
		print("Linhas adicionadas")
		break
