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
	import wx.lib.dialogs
except:
	print "Erro ao importar a wxPython"
	print "Consute http://sourceforge.net/projects/wxpython/files/wxPython/2.9.4.0/"

lista=['10', '50', '100' , '200',  '300',  '400',  '500' , '600',  '800','1000', '2000','3000','4000','5000','10000','20000','30000','40000','50000','60000']
dado=waterNext('./a6/' + lista[0] + '.csv')
class data(object):
	def calculator(self,event):
		valores=[]
		h=[0,0,0,0]
		try:			
			valores = [	float(self.t1.GetValue()),
						float(self.t2.GetValue()),
						float(self.t3.GetValue()),
						float(self.t4.GetValue()),
						int(self.p1.GetValue()),
						int(self.p2.GetValue()),
						int(self.p3.GetValue()),
						int(self.p4.GetValue())]
			for i in range(4):
				dado=waterNext('./a6/' + str(valores[4+i]) + '.csv')
				inter = sp.interp1d(dado.dados['Temperature'], dado.dados['Enthalpy'],kind='linear')
				h[i]=float(inter(valores[i]))
			saida=h[2] - h[3] -h[0] + h[1]
			print h
			self.saida.SetLabel("Saída = "+str(saida)+ ' kJ/kg')
		except Exception, ex:
			self.saida.SetLabel("Saída = -----")
			print ex
	
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
	
	wx.StaticText(panel, label='T1 =\t\t  P1=', pos=(660, 65))
	d.t1=wx.TextCtrl(panel, -1, "300", size=(50, -1),pos=(700,60),style=wx.TE_PROCESS_ENTER)
	d.p1=wx.ComboBox(panel, pos=(800, 60), size=(90, -1), choices=lista, style=wx.CB_SORT)
	d.p1.SetSelection(0)
	wx.StaticText(panel, label='T2 =\t\t  P2=', pos=(660, 105))
	d.t2=wx.TextCtrl(panel, -1, "300", size=(50, -1),pos=(700,100),style=wx.TE_PROCESS_ENTER)
	d.p2=wx.ComboBox(panel, pos=(800, 100), size=(90, -1), choices=lista, style=wx.CB_SORT)
	d.p2.SetSelection(0)
	wx.StaticText(panel, label='T3 =\t\t  P3=', pos=(660, 145))
	d.t3=wx.TextCtrl(panel, -1, "300", size=(50, -1),pos=(700,140),style=wx.TE_PROCESS_ENTER)
	d.p3=wx.ComboBox(panel, pos=(800, 140), size=(90, -1), choices=lista, style=wx.CB_SORT)
	d.p3.SetSelection(0)
	wx.StaticText(panel, label='T4 =\t\t  P4=', pos=(660, 185))
	d.t4=wx.TextCtrl(panel, -1, "300", size=(50, -1),pos=(700,180),style=wx.TE_PROCESS_ENTER)
	d.p4=wx.ComboBox(panel, pos=(800, 180), size=(90, -1), choices=lista, style=wx.CB_SORT)
	d.p4.SetSelection(0)
	calc = wx.Button(panel, 1, "Calcular",(680,220))
	d.saida = wx.StaticText(panel, label='Saída =', pos=(700, 260))
	panel.Bind(wx.EVT_BUTTON, d.calculator, calc)
	app.MainLoop()


if __name__ == "__main__":
	rankine('./a6.csv')
	
