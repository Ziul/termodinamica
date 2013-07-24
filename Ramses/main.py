#!/usr/bin/python
# -*- coding:utf-8 -*-

from ui import *

if __name__ == '__main__':
	app = wx.App(False)
	path='./a4.csv'
	# Passa tabela saturada como dado inicial para a interface
	frame = MainUI(path)
	frame.Show()
	app.MainLoop()
	del app
