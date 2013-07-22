#!/usr/bin/python
# -*- coding:utf-8 -*-

import wx
from pontos import *

def saida(results,ui):
	lista=['10', '50', '100' , '200',  '300',  '400',  '500' , '600',  '800','1000', '2000','3000','4000','5000','10000','20000','30000','40000','50000','60000']
	
	p1=float(ui.p1.GetValue()+'.0')
	p4=p1
	p3=float(ui.p3.GetValue()+'.0')
	p2=p3
	h=[0,0,0,0,0]	# h[0] <= sentinela
	err=''			# Erro
	t3=float(ui.t3.GetValue())

	print "P1=%.0fkpa, P3=%.0fkpa, T3= %.0f°C" %(p1,p3,t3)
	#--------- Calculando H3  ------------
	dado=waterNext('./a6/' + str(int(p3))+ '.csv')
	inter = sp.interp1d(dado.dados['Temperature'], dado.dados['Enthalpy'],kind='linear')
	h[3]=float(inter(t3))
	
	#Colhe o valor de S3 e mantem salvo P1
	inter = sp.interp1d(dado.dados['Temperature'], dado.dados['Entropy'],kind='linear')
	s3=float(inter(t3))	#S3
	
	#--------- Calculando H1  ------------
	#infere que no ponto 1 esta no saturado
	dado=water('./a5.csv')
	inter_min = sp.interp1d(dado.dados['Pressure'], dado.dados["Enthalpy_min"],kind='linear')
	h[1]=float(inter_min(p1))

	#--------- Calculando H4  ------------
	inter_min = sp.interp1d(dado.dados['Pressure'], dado.dados["Volume_min"],kind='linear')
	v1= float(inter_min(p1))
	
	inter_min = sp.interp1d(dado.dados['Pressure'], dado.dados["Entropy_min"],kind='linear')
	inter_max = sp.interp1d(dado.dados['Pressure'], dado.dados["Entropy_max"],kind='linear')
	titulo =float(((s3 - inter_min(p1)))/ (inter_max(p1)-inter_min(p1)))
	
	inter_min = sp.interp1d(dado.dados['Pressure'], dado.dados["Enthalpy_min"],kind='linear')
	inter_max = sp.interp1d(dado.dados['Pressure'], dado.dados["Enthalpy_max"],kind='linear')

	h[4]= (1-titulo) * inter_min(p1) + titulo*inter_max(p1)
	
	#--------- Calculando H2  ------------
	h[2] =h[1]+ v1*(p3-p1)


#---------------------------------------------------------
	print 'Hn = ' + str(h[1:])
	Wt=h[3]-h[4]
	Wb=h[2]-h[1]
	Qin=h[3]-h[2]
	n=(Wt-Wb)/Qin
	
	saida = 'Wt = %.2e\nWb = %.2e\nQin = %.2e\nn = %.2e\n' %(Wt,Wb,Qin,n)
	saida +='\n\n' + err
	print saida

	return saida

if __name__ == "__main__":
	print "Not this one"
