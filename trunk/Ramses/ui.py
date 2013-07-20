#!/usr/bin/python
# -*- coding:utf-8 -*-

'''locais'''
from pontos import *
import output
import output1
import os

'''externos'''
try:
	import scipy.interpolate as sp
except:
	print "Erro ao importar a SciPy"
	print "Consute http://sourceforge.net/projects/scipy/files/scipy/0.11.0/"
try:
	import numpy
except:
	print "Erro ao importar a NumPy"
	print "Consute http://sourceforge.net/projects/numpy/files/NumPy/1.7.0/ "
try:
	import wx
	import wx.lib.dialogs
except:
	print "Erro ao importar a wxPython"
	print "Consute http://sourceforge.net/projects/wxpython/files/wxPython/2.9.4.0/"

def quitar(event):
	quit()

class Termo(wx.Panel):

	results=''
    #----------------------------------------------------------------------
	def __init__(self,parent,path):
		wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
		
		self.path=path
		self.sair = wx.Button(self, 1, "Sair",(400,30))
		self.dados=water(path)
		#Primeira opção
		options = [	("{0} {1}".format(e,u) ) for e,u in zip(['Temperatura','Pressão'],self.dados.dados['unit'])]
		
		self.first = wx.ComboBox(self, pos=(50, 30), choices=options,size=(200, -1), style=wx.CB_SORT)
		self.first.SetStringSelection(options[0])
		self.first_value = wx.TextCtrl(self, -1, "200", size=(50, -1),pos=(270,30),style=wx.TE_PROCESS_ENTER)
		
		options = [	("{0} {1}".format(e,u) ) for e,u in zip(self.dados.dados['more'][2:],self.dados.dados['unit'][2:])]
		
		self.second = wx.ComboBox(self, pos=(50, 60), choices=options,size=(200, -1), style=wx.CB_SORT)
		self.second.SetStringSelection(options[0])
		self.second_value = wx.TextCtrl(self, -1, "1", size=(50, -1),pos=(270,60),style=wx.TE_PROCESS_ENTER)
		
		self.third =  wx.StaticText(self, label='Pressão [kPa]', pos=(50, 90))
		self.third.Hide()
		self.third_value = wx.ComboBox(self, pos=(270, 90), size=(90, -1), choices=[], style=wx.CB_SORT)
		self.third_value.Hide()
		
		self.text = wx.TextCtrl(self, pos=(50, 120), size=(400, 360),value="", style=wx.TE_MULTILINE)
		self.text.SetEditable(False)
		self.show(self)
		
		#Setando estado inicial
		self.third_value.SetSelection(8)
		self.show(self)
		#------------------------Eventos--------------------------------
		self.Bind(wx.EVT_BUTTON, quitar, self.sair)
		#self.Bind(wx.EVT_TEXT_ENTER, self.show,self.first_value)
		self.Bind(wx.EVT_TEXT, self.show,self.first_value)
		self.Bind(wx.EVT_TEXT, self.show,self.second_value)
		self.first.Bind(wx.EVT_COMBOBOX, self.show)
		self.second.Bind(wx.EVT_COMBOBOX, self.show)
		self.third_value.Bind(wx.EVT_COMBOBOX, self.show)
		
		
	def show(self,event):
		self.third.Hide()
		self.third_value.Hide()
		self.results= output.saida(self) 
		self.text.SetValue(self.results['data'])
		
		
		

class Rankine(wx.Panel):

    #----------------------------------------------------------------------
	def __init__(self,parent,data):
		wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
		self.sair = wx.Button(self, 1, "Sair",(400,30))
		self.p2 = wx.ComboBox(self, pos=(80, 190), size=(90, -1), choices=[], style=wx.CB_SORT)
		
		self.results = data
		self.prova  = output1.saida(data,self)
		self.text = wx.StaticText(self,label=self.prova,pos=(50,40))

		

		
		#------------------------Eventos--------------------------------
		self.Bind(wx.EVT_BUTTON, quitar, self.sair)


		
		


class MainUI(wx.Frame):
	name="Termodinâmica"
	def __init__(self,path):
		"""Constructor"""
		wx.Frame.__init__(self, None, wx.ID_ANY,self.name,size=(500,550))
		
		self.path=path
		self.notebook=wx.Notebook(self, wx.ID_ANY)

		self.tabOne = Termo(self.notebook,path)
		self.notebook.AddPage(self.tabOne, "Estado Termodinâmico")
		self.results = output.saida(self.tabOne)
		self.tabTwo = Rankine(self.notebook,self.results)
		self.notebook.AddPage(self.tabTwo, "Ciclo de Vapor de H2O")

		self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.update, self.notebook)
		self.tabTwo.p2.Bind(wx.EVT_COMBOBOX, self.update)

		self.Layout()
		
		self.Show()

	def update(self,event):
		os.system('clear')
		self.results = output.saida(self.tabOne)
		prova  = output1.saida(self.results,self.tabTwo)
		
		for i in self.results['names']:
			print 	i + ' = ' + str(self.results[i])
		if((self.results['superaquecido'] ==1) and (self.results['Entropy'] !=0) ):
			self.tabTwo.text.SetLabel(prova)
			self.tabTwo.text.Show(True)
			self.tabTwo.p2.Show(True)
		else:
			self.tabTwo.text.SetLabel("Não esta no estado superaquecido\n".center(60) + "ou estado invalido".center(45))
			#self.tabTwo.text.Hide()
			self.tabTwo.p2.Hide()
		
if __name__ == '__main__':
	print "Not this one!"
