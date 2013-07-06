#!/usr/bin/python
# -*- coding:utf-8 -*-

import wx
from pontos import *
selection=0
def saida(results,ui):
	prova = "Considerações:".center(80) + \
		"\n I) Regime permanente \
		\n II) Adiabático Reversível (isotrópico) \
		\n III) Não há variação de energia cinética \
		\n\n\n \
		\nH1 = " + str(results['Enthalpy'])+ \
		"\nS1 = S2 = " + str(results['Entropy']) + \
		"\nP1 = " + str(results['Pressure']) + ".0\nP2="
			
	ui.lista=['10', '50', '100' , '200',  '300',  '400',  '500' , '600',  '800','1000', '2000','3000','4000','5000','10000','20000','30000','40000','50000','60000']
	
	if str(results['Pressure']) in ui.lista:
		del ui.lista[ui.lista.index(str(results['Pressure'])):]
	
	selection = ui.p2.GetSelection()
	ui.p2.Clear()
	for i in ui.lista:
		ui.p2.Append(i)
	try:
		ui.p2.SetStringSelection(ui.lista[selection])
	except Exception, ex:
		ui.p2.SetStringSelection(ui.lista[0])
	selection = ui.p2.GetSelection()	
	
	
	dados=waterNext('./a6/' + ui.lista[ui.p2.GetSelection()]+ '.csv')
	inter = sp.interp1d(dados.dados['Entropy'] , dados.dados['Enthalpy'],kind='linear')
	
	try:
		ui.h2 =  inter(results['Entropy'])
		ui.W =  results['Enthalpy'] - ui.h2
		print "W = " + str(results['Enthalpy']) + ' - ' + str(ui.h2) + ' = '  + str(ui.W)
		prova += "\n\n H2= " + str(ui.h2) +\
		"\n W = H1-H2 = "+ str(ui.W)
	except Exception, ex:
		prova += "\n\nW=!\n\nFora do intervalo de interpolação"
		print ex
		print "Intervalo de entalpia: " + str(max(dados.dados['Enthalpy'])) + ' ~ ' + str(min(dados.dados['Enthalpy']))
		print "Intervalo de entropia: " +  str(max(dados.dados['Entropy'])) + ' ~ ' + str(min(dados.dados['Entropy']))
		
	
	
	return prova

if __name__ == "__main__":
	print "Not this one"
