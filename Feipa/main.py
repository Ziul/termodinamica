#!/usr/bin/python
# -*- coding:utf-8 -*-

from pontos import *
import janela
import os
from rankine import *
from termo import *

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

if __name__ == '__main__':
	os.system(['clear','cls'][os.name == 'nt'])
	app = wx.App(False)
	path='./a4.csv'
	j=janela.choose()
	j.buildme("Escolha de modulo","Qual modulo deseja carregar?",['Estado Termodinâmico','Ciclo de Rankine'])
	j.Show(False)
	if (j.selection ==0):
		termo(path)
	else:
		rankine(path)


