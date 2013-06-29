#!/usr/bin/python
# -*- coding:utf-8 -*-

'''locais'''
from pontos import *
import janela

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
		
		self.third =  wx.StaticText(self.Painel, label=self.dados.dados['more'][self.first.GetSelection()], pos=(50, 90))
		self.third.Show(False)
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

		try:
			self.dados=water(path)
			escolha1 = self.dados.dados['names'][self.first.GetSelection()]
			escolha2 = self.dados.dados['names'][self.second.GetSelection()+2]
			value1 = float(self.first_value.GetValue())
			value2 = float(self.second_value.GetValue())
			inter_min = sp.interp1d(self.dados.dados[escolha1], self.dados.dados[escolha2+"_min"],kind='linear')
			inter_max = sp.interp1d(self.dados.dados[escolha1], self.dados.dados[escolha2+"_max"],kind='linear')
		except Exception, ex:
			self.results= "Dados vazios ou não validos\n\n" + str(ex)
			self.text.SetValue(self.results)

		try:
			valores=''
			if (value2>=inter_min(value1)):
				if (value2<=inter_max(value1)):
					valores= "Esta no estado de água saturada\n".center(80) + "\n"
					for i,u in zip(self.dados.dados['index'],self.dados.dados['unit_index']):
						inter = sp.interp1d(self.dados.dados[escolha1], self.dados.dados[i],kind='linear')
						valores += ( i.rjust(13) +"\t\t=\t" + (str(inter(value1))+" "+ u).ljust(11)  + "\n")
					titulo =((inter(value1) - inter_min(value1)))/ (inter_min(value1)+inter_max(value1))
					valores += "        Titulo\t\t=\t"  + str(titulo) + "\n"
					valores += "----------------------------------------------------------------------------------------\n"
					valores += "Valores precisos:\n".center(90) + "\n"
					for i,u in zip(self.dados.dados['names'][2:],self.dados.dados['unit'][2:]):
						if((i != 'Pressure') and (i != 'Temperature') ):
							precise = self.dados.dados[i+'_min'] + titulo * (self.dados.dados[i+'_min'] + self.dados.dados[i+'_max'])/2
							inter = sp.interp1d(self.dados.dados[escolha1], precise,kind='linear')
							valores += ( i.rjust(13) +"\t\t=\t" + (str(inter(value1))+" "+ u).ljust(11)  + "\n")
					
					
				else:
					valores= "Esta no estado vapor superaquecido\n".center(80) + "\n"	# (acima do intervalo para saturada)
					lista=['10', '50', '100' , '200',  '300',  '400',  '500' , '600',  '800','1000', '2000','3000','4000','5000','10000','20000','30000','40000','50000','60000']
					print "Esta no estado vapor superaquecido"
					self.third =  wx.StaticText(self.Painel, label='Pressão [kPa]', pos=(50, 90))
					value1 = self.third_value.GetSelection()
					self.third_value.Clear()
					for i in lista:
						self.third_value.Append(i)
					self.third_value.SetStringSelection(lista[value1])
					self.third.Show(True)
					self.third_value.Show(True)
					value1 = self.third_value.GetSelection()
					'''
					if (lista.index(value1)):
						j=janela.choose()
						j.buildme("Não é saturada","Entre novamente como o valor para a Pressão [kPa]",lista)
						j.Show(False)
						value1 = j.selection
						self.first_value.SetValue( lista[value1])
					'''
					self.dados=waterNext('./a6/' + lista[value1] + '.csv')
					for i in self.dados.dados['Temperature']:
						self.dados.dados['Pressure'] = numpy.append(self.dados.dados['Pressure'],float(lista[value1]))
					for i,u in zip(self.dados.dados['index'],self.dados.dados['unit_index']):
						inter = sp.interp1d(self.dados.dados[escolha2], self.dados.dados[i],kind='linear')
						valores += ( i.rjust(13) +"\t\t=\t" + (str(inter(value2))+" "+ u).ljust(11)  + "\n")

			else:
				valores= "Esta no estado liquido comprimido\n".center(80) + "\n"
				lista=['5','10','15','20','30','50']
				print "Esta no estado liquido comprimido"
				self.third =  wx.StaticText(self.Painel, label='Pressão [MPa]', pos=(50, 90))
				value1 = self.third_value.GetSelection()
				self.third_value.Clear()
				for i in lista:
					self.third_value.Append(i)
				self.third_value.SetStringSelection(lista[value1])
				self.third.Show(True)
				self.third_value.Show(True)
				value1 = self.third_value.GetSelection()
				'''
				if (lista.index(value1)):
					j=janela.choose()
					j.buildme("Não é saturada","Entre novamente como o valor para a Pressão [kPa]",lista)
					j.Show(False)
					value1 = j.selection
					self.first_value.SetValue( lista[value1])
				'''
				self.dados=waterNext('./a7/' + lista[value1] + '.csv')
				for i in self.dados.dados['Temperature']:
					self.dados.dados['Pressure'] = numpy.append(self.dados.dados['Pressure'],float(lista[value1]))
				for i,u in zip(self.dados.dados['index'],self.dados.dados['unit_index']):
					inter = sp.interp1d(self.dados.dados[escolha2], self.dados.dados[i],kind='linear')
					valores += ( i.rjust(13) +"\t\t=\t" + (str(inter(value2))+" "+ u).ljust(11)  + "\n")
			
					
		except ValueError, ex:
			valores+= "\nFaixa de valores fora do intervalo de amostra\n" + str(ex)
			valores+= "\n\nProvavelmente fora do intervalo de interpolação\n\n\n" 
			
			valores += "%s: %.2e - %.2e\n" % (self.dados.dados['more'][self.first.GetSelection()],min(self.dados.dados[escolha1]) , max(self.dados.dados[escolha1]))
			
			try:
				print "%s: %.2e - %.2e\n" % (self.dados.dados['more'][self.second.GetSelection()],min(self.dados.dados[escolha2]) , max(self.dados.dados[escolha2]) )
			except Exception, ex:
				valores += "%s minima: %.2e - %.2e\n" % (self.dados.dados['more'][self.second.GetSelection()+2],min(self.dados.dados[escolha2+'_min']) , max(self.dados.dados[escolha2+'_min']) )
				valores +="%s máxima: %.2e - %.2e\n" % (self.dados.dados['more'][self.second.GetSelection()+2],min(self.dados.dados[escolha2+'_max']) , max(self.dados.dados[escolha2+'_max']) )

			
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
