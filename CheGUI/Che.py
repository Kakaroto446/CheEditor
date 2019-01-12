#! /usrbin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
from tkFileDialog import asksaveasfilename,askopenfilename

#classe principal do editor
class App:
	#função inicial
	def __init__(self):
		self.root = Tk()
		self.root.wm_title("CheEditor")
		self.root.geometry('700x400')
		self.root.bind('<Control-s>', self.salvar)
		self.root.bind('<Control-x>', self.abrir)

		#scrollbar
		scrollbar = Scrollbar(self.root)
		scrollbar.pack(side=RIGHT, fill=Y)

		#barra menu
		menubar = Menu(self.root)

		menuarq = Menu(menubar)
		menuarq.add_command(label="Salvar", command=self.salvar)
		menuarq.add_command(label="Abrir", command=self.abrir)
		menubar.add_cascade(label="Arquivo", menu=menuarq)

		menuajuda = Menu(menubar)
		menuajuda.add_command(label="Sobre", command=self.sobre)
		menubar.add_cascade(label="Ajuda", menu=menuajuda)
		self.root.config(menu=menubar)

		menunome = Menu(menubar)

		#onde fica o texto
		self.text = Text(self.root)
		self.text.pack(expand=YES, fill=BOTH)
		self.text.configure(background='#1a1a1a')
		self.text.configure(fg='white')
		self.text.config(insertbackground='white')
		self.text.config(font=("Courier", 11))

		#configuração da scrollbar
		self.text.config(yscrollcommand=scrollbar.set)
		scrollbar.config(command=self.text.yview)

		#janela
		self.root.mainloop()

	#função que salva o arquivo
	def salvar(self, _event=None):
		fileName = asksaveasfilename()
		try:
			file = open(fileName, 'w')
			textoutput = self.text.get(0.0, END)
			file.write(textoutput)
		except:
			pass
		finally:
			arq.close()

	#função de abrir
	def abrir(self):
		fileName = askopenfilename()
		try:
			file = open(fileName, 'r')
			contents = file.read()

			self.text.delete(0.0, END)
			self.text.insert(0.0, contents)
			self.root.wm_title("CheEditor/" +fileName)

		except:
			pass

	#função do sobre
	def sobre(self):
		root = Tk()
		root.wm_title("Sobre")
		texto=("CheEditor: Versão GUI-1.0")
		textONlabel = Label(root, text=texto)
		textONlabel.pack()

#inicia o editor
App()
