#!/usr/bin/python
# -*- coding:utf-8 -*-

from pontos import *

def saida(ui):
	
	try:
		ui.dados=water('./a4.csv')
		escolha1 = ui.first[0]
		escolha2 = ui.second[0]
		value1 = float(ui.first[1])
		value2 = float(ui.second[1])
		inter_min = sp.interp1d(ui.dados.dados[escolha1], ui.dados.dados[escolha2+"_min"],kind='linear')
		inter_max = sp.interp1d(ui.dados.dados[escolha1], ui.dados.dados[escolha2+"_max"],kind='linear')
	except Exception, ex:
		ui.results= "Dados vazios ou não validos\n\n" + str(ex)

	try:
		valores=''
		if (value2>=inter_min(value1)):
			if (value2<=inter_max(value1)):
				valores= "Esta no estado de água saturada\n".center(50) + "\n"
				for i,u in zip(ui.dados.dados['index'],ui.dados.dados['unit_index']):
					inter = sp.interp1d(ui.dados.dados[escolha1], ui.dados.dados[i],kind='linear')
					valores += ( i.rjust(13) +"\t\t=\t" + (str(inter(value1))+" "+ u).ljust(11)  + "\n")
				titulo =((value2 - inter_min(value1)))/ (inter_max(value1)-inter_min(value1))
				valores += "        Titulo\t\t=\t"  + str(titulo) + "\n"
				valores += "-------------------------------------------------------------\n"
				valores += "Valores interpolados:\n".center(50) + "\n"
				for i,u in zip(ui.dados.dados['names'][2:],ui.dados.dados['unit'][2:]):
					if((i != 'Pressure') and (i != 'Temperature') ):
						precise = ui.dados.dados[i+'_min'] + titulo * (ui.dados.dados[i+'_min'] + ui.dados.dados[i+'_max'])/2
						inter = sp.interp1d(ui.dados.dados[escolha1], precise,kind='linear')
						valores += ( i.rjust(13) +"\t\t=\t" + (str(inter(value1))+" "+ u).ljust(11)  + "\n")
				
				
			else:
				valores= "Esta no estado vapor superaquecido\n".center(50) + "\n"	# (acima do intervalo para saturada)
				lista=['10', '50', '100' , '200',  '300',  '400',  '500' , '600',  '800','1000', '2000','3000','4000','5000','10000','20000','30000','40000','50000','60000']
				value1 = lista.index(ui.third_value)
				ui.dados=waterNext('./a6/' + lista[value1] + '.csv')
				for i in ui.dados.dados['Temperature']:
					ui.dados.dados['Pressure'] = numpy.append(ui.dados.dados['Pressure'],float(lista[value1]))
				for i,u in zip(ui.dados.dados['index'],ui.dados.dados['unit_index']):
					inter = sp.interp1d(ui.dados.dados[escolha2], ui.dados.dados[i],kind='linear')
					valores += ( i.rjust(13) +"\t\t=\t" + (str(inter(value2))+" "+ u).ljust(11)  + "\n")

		else:
			valores= "Esta no estado liquido comprimido\n".center(50) + "\n"
			lista=['5','10','15','20','30','50']
			value1 = lista.index(ui.third_value)
			
			ui.dados=waterNext('./a7/' + lista[value1] + '.csv')
			for i in ui.dados.dados['Temperature']:
				ui.dados.dados['Pressure'] = numpy.append(ui.dados.dados['Pressure'],float(lista[value1]))
			for i,u in zip(ui.dados.dados['index'],ui.dados.dados['unit_index']):
				inter = sp.interp1d(ui.dados.dados[escolha2], ui.dados.dados[i],kind='linear')
				valores += ( i.rjust(13) +"\t\t=\t" + (str(inter(value2))+" "+ u).ljust(11)  + "\n")
		
				
	except ValueError, ex:
		valores+= "\nFaixa de valores fora do intervalo de amostra\n" + str(ex)
		valores+= "\n\nProvavelmente fora do intervalo de interpolação\n\n" 

		
	return valores
