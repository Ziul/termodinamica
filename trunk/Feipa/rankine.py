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

class data(object):
	valores=[]
	
	def calculator(self,event):
		valores = [	float(self.h1.GetValue()),
					float(self.h2.GetValue()),
					float(self.h3.GetValue()),
					float(self.h4.GetValue())]
		print valores
		self.saida.SetLabel("Saída = "+str(valores))
	
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
	
	wx.StaticText(panel, label='H1 =', pos=(760, 65))
	d.h1=wx.TextCtrl(panel, -1, "1", size=(50, -1),pos=(800,60),style=wx.TE_PROCESS_ENTER)
	wx.StaticText(panel, label='H2 =', pos=(760, 105))
	d.h2=wx.TextCtrl(panel, -1, "1", size=(50, -1),pos=(800,100),style=wx.TE_PROCESS_ENTER)
	wx.StaticText(panel, label='H3 =', pos=(760, 145))
	d.h3=wx.TextCtrl(panel, -1, "1", size=(50, -1),pos=(800,140),style=wx.TE_PROCESS_ENTER)
	wx.StaticText(panel, label='H4 =', pos=(760, 185))
	d.h4=wx.TextCtrl(panel, -1, "1", size=(50, -1),pos=(800,180),style=wx.TE_PROCESS_ENTER)
	calc = wx.Button(panel, 1, "Calcular",(780,220))
	d.saida = wx.StaticText(panel, label='Saída =', pos=(700, 260))
	panel.Bind(wx.EVT_BUTTON, d.calculator, calc)
	app.MainLoop()


if __name__ == "__main__":
	rankine('./a4.csv')
	
