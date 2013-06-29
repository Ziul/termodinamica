#!/usr/bin/python
# -*- coding:utf-8 -*-

'''locais'''
from pontos import *
import output

'''externos'''
try:
	import numpy
except:
	print "Erro ao importar a NumPy"
	print "Consute http://sourceforge.net/projects/numpy/files/NumPy/1.7.0/ "
try:
	import scipy.interpolate as sp
except:
	print "Erro ao importar a SciPy"
	print "Consute http://sourceforge.net/projects/scipy/files/scipy/0.11.0/"
try:
	import wx
	import wx.lib.dialogs
except:
	print "Erro ao importar a wxPython"
	print "Consute http://sourceforge.net/projects/wxpython/files/wxPython/2.9.4.0/"

class Form(wx.Frame):

	name="Termodinâmica"
	results=''
    #----------------------------------------------------------------------
	def __init__(self,path):
		wx.Frame.__init__(self, None, wx.ID_ANY,self.name,size=(500,500))
		
		self.path=path
		self.Painel = wx.Panel(self)
		self.sair = wx.Button(self.Painel, 1, "Sair",(400,30))
		self.dados=water(path)
		#Primeira opção
		options = [	("{0} {1}".format(e,u) ) for e,u in zip(['Temperatura','Pressão'],self.dados.dados['unit'])]
		
		self.first = wx.ComboBox(self.Painel, pos=(50, 30), choices=options,size=(200, -1), style=wx.CB_SORT)
		self.first.SetStringSelection(options[0])
		self.first_value = wx.TextCtrl(self.Painel, -1, "100", size=(50, -1),pos=(270,30),style=wx.TE_PROCESS_ENTER)
		
		options = [	("{0} {1}".format(e,u) ) for e,u in zip(self.dados.dados['more'][2:],self.dados.dados['unit'][2:])]
		
		self.second = wx.ComboBox(self.Painel, pos=(50, 60), choices=options,size=(200, -1), style=wx.CB_SORT)
		self.second.SetStringSelection(options[0])
		self.second_value = wx.TextCtrl(self.Painel, -1, "25", size=(50, -1),pos=(270,60),style=wx.TE_PROCESS_ENTER)
		
		self.third =  wx.StaticText(self.Painel, label='Pressão [MPa]', pos=(50, 90))
		self.third.Hide()
		self.third_value = wx.ComboBox(self.Painel, pos=(270, 90), size=(90, -1), choices=[], style=wx.CB_SORT)
		self.third_value.Hide()
		
		self.text = wx.TextCtrl(self.Painel, pos=(50, 120), size=(400, 360),value="", style=wx.TE_MULTILINE)
		self.text.SetEditable(False)
		
		#------------------------Eventos--------------------------------
		self.Bind(wx.EVT_BUTTON, self.quitar, self.sair)
		#self.Bind(wx.EVT_TEXT_ENTER, self.show,self.first_value)
		self.Bind(wx.EVT_TEXT, self.show,self.first_value)
		self.Bind(wx.EVT_TEXT, self.show,self.second_value)
		self.first.Bind(wx.EVT_COMBOBOX, self.show)
		self.second.Bind(wx.EVT_COMBOBOX, self.show)
		self.third_value.Bind(wx.EVT_COMBOBOX, self.show)
		
		
	def show(self,event):
		self.third.Hide()
		self.third_value.Hide()
		valores = output.saida(self)
		self.results= valores
		self.text.SetValue(self.results)
		
					
	def quitar(self,event):
		quit()
		


	
if __name__ == '__main__':
	app = wx.App(False)
	path='./a4.csv'

	frame = Form(path)
	frame.Show()
	app.MainLoop()
	del app
