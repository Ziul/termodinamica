#!/usr/bin/python
# -*- coding:utf-8 -*-

'''locais'''
from pontos import *
import output
import output1

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
except:
	print "Erro ao importar a wxPython"
	print "Consute http://sourceforge.net/projects/wxpython/files/wxPython/2.9.4.0/"

#saír do programa
def quitar(event):
	quit()

class Termo(wx.Panel):

	results=''
    #----------------------------------------------------------------------
    #método de inicialização da classe
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
		#Segunda opção
		self.second = wx.ComboBox(self, pos=(50, 60), choices=options,size=(200, -1), style=wx.CB_SORT)
		self.second.SetStringSelection(options[0])
		self.second_value = wx.TextCtrl(self, -1, "1", size=(50, -1),pos=(270,60),style=wx.TE_PROCESS_ENTER)
		
		#Terceira opção
		self.third =  wx.StaticText(self, label='Pressão [kPa]', pos=(50, 90))
		self.third.Hide()
		self.third_value = wx.ComboBox(self, pos=(270, 90), size=(90, -1), choices=[], style=wx.CB_SORT)
		self.third_value.Hide()
		
		#Quadro de saída
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
		
	#método de atualização de tela da classe	
	def show(self,event):
		self.third.Hide()
		self.third_value.Hide()
		self.results= output.saida(self) 
		self.text.SetValue(self.results['data'])
		
class Rankine(wx.Panel):

    #----------------------------------------------------------------------
    #método de inicialização da classe
	def __init__(self,parent,data):
		wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
		lista=['10', '50', '100' , '200',  '300',  '400',  '500' , '600',  '800','1000', '2000','3000','4000','5000','10000','20000','30000','40000','50000','60000']
		self.sair = wx.Button(self, 1, "Sair",(400,30))
		wx.StaticText(self, label='P1=\t\t\t\t  [KPa]', pos=(60, 65))
		self.p1=wx.ComboBox(self, pos=(100, 60), size=(90, -1), choices=lista, style=wx.CB_SORT)
		self.p1.SetSelection(3)
		
		wx.StaticText(self, label='P3=\t\t\t\t  [KPa]', pos=(60, 95))
		self.p3=wx.ComboBox(self, pos=(100, 90), size=(90, -1), choices=lista, style=wx.CB_SORT)
		self.p3.SetSelection(0)
		
		wx.StaticText(self, label='T3=\t\t\t[°C]', pos=(60, 125))
		self.t3=wx.TextCtrl(self, -1, "900", size=(50, -1),pos=(100,120),style=wx.TE_PROCESS_ENTER)
		self.results = data
		self.text = wx.StaticText(self,label='',pos=(50,180))
		self.update(0)
		
	#método de atualização de tela da classe	
	def update(self,event):
		try:			
			self.prova  = output1.saida(self.results,self)
			self.text.SetLabel(self.prova)
			
		except Exception, ex:
			print ex
			self.text.SetLabel('Valores fora do intervalo de interpolação')

		

		
		#------------------------Eventos--------------------------------
		self.Bind(wx.EVT_BUTTON, quitar, self.sair)
		self.p1.Bind(wx.EVT_COMBOBOX, self.update)
		self.p3.Bind(wx.EVT_COMBOBOX, self.update)
		#self.Bind(wx.EVT_TEXT, self.update,self.p1)
		self.Bind(wx.EVT_TEXT, self.update,self.t3)


		
		

#Classe para tratamento dos paideis/abas
class MainUI(wx.Frame):
	name="Termodinâmica"	#nome principal do programa
	def __init__(self,path):
		"""Constructor"""
		wx.Frame.__init__(self, None, wx.ID_ANY,self.name,size=(500,550))
		
		self.path=path
		self.notebook=wx.Notebook(self, wx.ID_ANY)
		#Primeira aba
		self.tabOne = Termo(self.notebook,path)
		self.notebook.AddPage(self.tabOne, "Estado Termodinâmico")
		self.results = output.saida(self.tabOne)
		#Segunda aba
		self.tabTwo = Rankine(self.notebook,self.results)
		self.notebook.AddPage(self.tabTwo, "Ciclo de Vapor de H2O")
		#evento de troca de aba
		self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.update, self.notebook)

		self.Layout()
		
		self.Show()

	def update(self,event):
		pass
		
if __name__ == '__main__':
	print "Not this one!"
