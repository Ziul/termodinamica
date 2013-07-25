#!/usr/bin/python
# -*- coding:utf-8 -*-

from pontos import *

def output(p4,p3,t3):
	data={	'H1':0,
			'H2':0,
			'H3':0,
			'H4':0,
			'W_liquido':0,
			'Eficiencia':0}
	
	p1=p4
	p2=p3
	t3=t3

	dado=water('./a4.csv')
	inter_min = sp.interp1d(dado.dados['Pressure'], dado.dados["Enthalpy_min"],kind='linear')
	data['H1']=float(inter_min(p1)) #valor de H1
	
	dado=waterNext('./a6/' + str(int(p3))+ '.csv')
	interpol = sp.interp1d(dado.dados['Temperature'], dado.dados['Enthalpy'],kind='linear')
	data['H3']=float(interpol(t3)) #valor de H3
	
	interpol = sp.interp1d(dado.dados['Temperature'], dado.dados['Entropy'],kind='linear')
	s3=interpol(t3) #valor de S3

	dado=water('./a4.csv')
	inter_min = sp.interp1d(dado.dados['Pressure'], dado.dados["Volume_min"],kind='linear')
	v1= inter_min(p1) #valor para V1
	
	inter_min = sp.interp1d(dado.dados['Pressure'], dado.dados["Entropy_min"],kind='linear')
	inter_max = sp.interp1d(dado.dados['Pressure'], dado.dados["Entropy_max"],kind='linear')
	x =float(((s3 - inter_min(p4)))/ (inter_max(p4)-inter_min(p4))) #calcula o titulo
	
	#atualiza funções de interpolação
	inter_min = sp.interp1d(dado.dados['Pressure'], dado.dados["Enthalpy_min"],kind='linear')
	inter_max = sp.interp1d(dado.dados['Pressure'], dado.dados["Enthalpy_max"],kind='linear')
	data['H4']= (1-x) * inter_min(p4) + x*inter_max(p4) #valor de H4
	
	data['H2'] =data['H1']+ v1*(p2-p1) #valor de H2

	#---------Eficiência-e-Trabalho-Liquido-------------------

	data['W_liquido'] = (data['H3']-data['H4']) - (data['H2']-data['H1'])
	data['Eficiencia']=data['W_liquido']/(data['H3']-data['H2'])

	return data

if __name__ == "__main__":
	print output(300.0,600.0,300.0)	#P4, P3, T3
