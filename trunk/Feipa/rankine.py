#!/usr/bin/python
# -*- coding:utf-8 -*-

import janela
from pontos import *

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
except:
	print "Erro ao importar a wxPython"
	print "Consute http://sourceforge.net/projects/wxpython/files/wxPython/2.9.4.0/"

#Lista de opções de pressão P3
lista=['10', '50', '100' , '200',  '300',  '400',  '500' , '600',  '800','1000', '2000','3000','4000','5000','10000','20000','30000','40000','50000','60000']
#carrega tabela A6
dado=waterNext('./a6/' + lista[0] + '.csv')
class data(object):
	def calculator(self,event):
		h=[0,0,0,0] #vetor com os valores de entalpia
		try:
			#infere que no ponto 3 esta superaquecido
			dado=waterNext('./a6/' + self.p3.GetValue() + '.csv')
			inter = sp.interp1d(dado.dados['Temperature'], dado.dados['Enthalpy'],kind='linear')
			h[2]=float(inter(float(self.t3.GetValue())))
			# H3 salvo
			
			#Colhe o valor de S3 e mantem salvo P1
			inter = sp.interp1d(dado.dados['Temperature'], dado.dados['Entropy'],kind='linear')
			value2=float(inter(float(self.t3.GetValue())))	#S3
			value1 = float(self.p1.GetValue())				#P1
			#-----
			
			#infere que no ponto 1 esta no saturado
			#carrega tabela A4
			dado=water('./a4.csv')
			inter_min = sp.interp1d(dado.dados['Pressure'], dado.dados["Enthalpy_min"],kind='linear')
			#interpola P1 na entalpia liquid.
			h[0]=float(inter_min(float(self.p1.GetValue())))
			# H1 salvo
			#-----
			inter_min = sp.interp1d(dado.dados['Pressure'], dado.dados["Volume_min"],kind='linear')
			#interpola P1 no volume liquid.
			v1= float(inter_min(float(self.p1.GetValue())))
			# V1 salvo
			
			inter_min = sp.interp1d(dado.dados['Pressure'], dado.dados["Entropy_min"],kind='linear')
			inter_max = sp.interp1d(dado.dados['Pressure'], dado.dados["Entropy_max"],kind='linear')
			# x= (S3-S1_min)/(S1_max-S1_min)
			titulo =float(((value2 - inter_min(value1)))/ (inter_max(value1)-inter_min(value1)))
			
			inter_min = sp.interp1d(dado.dados['Pressure'], dado.dados["Enthalpy_min"],kind='linear')
			inter_max = sp.interp1d(dado.dados['Pressure'], dado.dados["Enthalpy_max"],kind='linear')
			# H4 = (1-x)*H1_min + x*H1_max
			h[3]= (1-titulo) * inter_min(value1) + titulo*inter_max(value1)
			# H4 salvo
			
			# H2 = H1 + V1(P3-P1)
			h[1] =h[0]+ v1*(float(self.p3.GetValue())-float(self.p1.GetValue()))
			# H2 salvo
			
			
			#Calcula potência e eficiência
			saida= h[2]-h[1] -h[3] +h[0]
			eficiencia = 1 - (h[3]-h[0])/(h[2]-h[1])
			#imprime valores na tela de depuração (terminal)
			print "h[] = " + str(h)
			print 'Titulo = ' + str(titulo)
			print 'V1 = ' + str(v1)
			print 'S3 = ' + str(value2)
			print 'Saida = ' + str(saida)
			print 'Eficiencia = ' + str(eficiencia)
			
			# Define texto para ser impresso na janela
			self.saida.SetLabel("Saída = "+str(saida)+ ' kJ/kg\nEficiencia = ' + str(eficiencia))
		except Exception, e:
			# Caso algum estado inesperado aconteça
			self.saida.SetLabel("Saída = -----")
			print e
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			print(exc_type, fname, exc_tb.tb_lineno)

#Construção da janela
def rankine(path):
	app = wx.App(False)
	print "Rankine"
	rankine_frame=wx.Frame( None, wx.ID_ANY,'Ciclo de Rankine',size=(900,450))
	panel=wx.Panel( parent=rankine_frame, id=wx.ID_ANY)
	rankine_frame.Show()
	d=data();
	img = wx.Image("./Rankine_cycle_layout.png", wx.BITMAP_TYPE_ANY)
	img = img.Scale(img.GetWidth()*0.8,img.GetHeight()*0.8)
	png = wx.StaticBitmap(panel, -1, wx.BitmapFromImage(img),pos=(0,0))

	wx.StaticText(panel, label='P1=\t\t\tKPa', pos=(660, 65))
	d.p1=wx.TextCtrl(panel, -1, "300", size=(50, -1),pos=(700,60),style=wx.TE_PROCESS_ENTER)
	wx.StaticText(panel, label='P3 = \t\t\t  KPa', pos=(660, 145))
	d.t3=wx.TextCtrl(panel, -1, "300", size=(50, -1),pos=(700,100),style=wx.TE_PROCESS_ENTER)
	wx.StaticText(panel, label='T3=\t\t\t°C', pos=(660, 105))
	d.p3=wx.ComboBox(panel, pos=(700, 140), size=(90, -1), choices=lista, style=wx.CB_SORT)
	d.p3.SetSelection(0)
	calc = wx.Button(panel, 1, "Calcular",(680,220))
	d.saida = wx.StaticText(panel, label='Saída =', pos=(700, 260))
	panel.Bind(wx.EVT_BUTTON, d.calculator, calc)
	app.MainLoop()


if __name__ == "__main__":
	rankine('./a6.csv')

