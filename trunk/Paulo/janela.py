# -*- coding:utf-8 -*-

import wx
import wx.lib.dialogs
 
########################################################################
class text(wx.Frame):
	
	#----------------------------------------------------------------------
	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, "Impressão de valores")
		panel = wx.Panel(self, wx.ID_ANY)

	def buildme(self,titulo,msg):
		dlg = wx.lib.dialogs.ScrolledMessageDialog(self, msg, titulo)
		dlg.ShowModal()

		dlg.Destroy()


class choose(wx.Frame):
 
	#----------------------------------------------------------------------
	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, "SingleChoiceDialog Tutorial")
		panel = wx.Panel(self, wx.ID_ANY)

	def buildme(self,titulo_janela='The Caption',texto="What's your favorite langauge?",lista=["A", "VB"]):
		dlg = wx.SingleChoiceDialog(
				self, texto, titulo_janela,
				lista, 
				wx.CHOICEDLG_STYLE
				)

		if dlg.ShowModal() == wx.ID_OK:
			self.selection = dlg.GetSelection()


class read_value(wx.Frame):
 
	#----------------------------------------------------------------------
	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY,"TextEntryDialog Tutorial")
		panel = wx.Panel(self, wx.ID_ANY)

		#----------------------------------------------------------------------
	def buildme(self, titulo="Titulo", text="Pergunta?" , intervalo=''):
		"""
		Based on the wxPython demo by the same name
		"""
		dlg = wx.TextEntryDialog(
		self, text,
		titulo, intervalo)
				
		#dlg.SetValue("Python is the best!")

		if dlg.ShowModal() == wx.ID_OK:
			self.selection = float(dlg.GetValue())
		else:
			quit()
		#dlg.Destroy()
 
 
 # Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = read_value()
    frame.buildme()
    print frame.selection
    frame.Show(False)
