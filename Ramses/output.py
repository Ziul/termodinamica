#!/usr/bin/python
# -*- coding:utf-8 -*-

from pontos import *

def saida(ui):
	vlr={	'names':['Temperature','Pressure','Volume','Energy','Enthalpy','Entropy','Titulo'],
			'unit':['[°C]','[kPa]','[m³/kg]','[kJ/kg]','[kJ/kg]','[kJ/kg]'],
			'more':['Temperatura', 'Pressão', 'Volume Especifico','Energia Interna', 'Entalpia', 'Entropia','Titulo'],
	'data':'','Temperature':0,'Pressure':0,'Volume':0,'Energy':0,'Enthalpy':0,'Entropy':0,'Titulo':0,
	'superaquecido':0}
	#levanta dados disponíveis na interface
	try:
		ui.dados=water(ui.path)
		escolha1 = ui.dados.dados['names'][ui.first.GetSelection()]
		escolha2 = ui.dados.dados['names'][ui.second.GetSelection()+2]
		value1 = float(ui.first_value.GetValue())
		value2 = float(ui.second_value.GetValue())
		inter_min = sp.interp1d(ui.dados.dados[escolha1], ui.dados.dados[escolha2+"_min"],kind='linear')
		inter_max = sp.interp1d(ui.dados.dados[escolha1], ui.dados.dados[escolha2+"_max"],kind='linear')
	except Exception, ex:
		valores= "Dados vazios ou não validos\n\n" + str(ex)

	try:
		valores=''
		ui.third_value.Hide()
		ui.third.Hide()
		if (value2>=inter_min(value1)):
			if (value2<=inter_max(value1)):
				#Entra no estado saturada se estiver entre valor liquid. e vapor
				vlr['superaquecido']=0
				valores= "Esta no estado de água saturada\n".center(80) + "\n"
				#interpola dados
				for i,u in zip(ui.dados.dados['index'],ui.dados.dados['unit_index']):
					inter = sp.interp1d(ui.dados.dados[escolha1], ui.dados.dados[i],kind='linear')
					valores += ( i.rjust(13) +"\t\t=\t" + (str(inter(value1))+" "+ u).ljust(11)  + "\n")
				#calcula titulo
				titulo =((value2 - inter_min(value1)))/ (inter_max(value1)-inter_min(value1))
				valores += "        Titulo\t\t=\t"  + str(titulo) + "\n"
				valores += "----------------------------------------------------------------------------------------\n"
				valores += "Valores exatos:\n".center(90) + "\n"
				#calcula os dados usando o titulo
				for i,u in zip(ui.dados.dados['names'][2:],ui.dados.dados['unit'][2:]):
					if((i != 'Pressure') and (i != 'Temperature') ):
						#precise = ui.dados.dados[i+'_min'] + titulo * (ui.dados.dados[i+'_min'] + ui.dados.dados[i+'_max'])/2
						precise = ui.dados.dados[i+'_min'] + titulo * (ui.dados.dados[i+'_max'] - ui.dados.dados[i+'_min'])
						inter = sp.interp1d(ui.dados.dados[escolha1], precise,kind='linear')
						valores += ( i.rjust(13) +"\t\t=\t" + (str(inter(value1))+" "+ u).ljust(11)  + "\n")
						vlr[i] = float(inter(value1))
				vlr[escolha1] = value1
				if(escolha1=='Pressure'):
					inter = sp.interp1d(ui.dados.dados[escolha1], ui.dados.dados['Temperature'],kind='linear')
					vlr['Temperature'] = float(inter(value1))
				else:
					inter = sp.interp1d(ui.dados.dados[escolha1], ui.dados.dados['Pressure'],kind='linear')
					vlr['Pressure'] = float(inter(value1))
				vlr['Titulo'] = titulo
				
				
			else:
				#se estiver acima do valor de vapor
				vlr['superaquecido']=1
				valores= "Esta no estado vapor superaquecido\n".center(80) + "\n"	# (acima do intervalo para saturada)
				lista=['10', '50', '100' , '200',  '300',  '400',  '500' , '600',  '800','1000', '2000','3000','4000','5000','10000','20000','30000','40000','50000','60000']
				value1 = ui.third_value.GetSelection()
				ui.third_value.Clear()
				#atualiza dado da terceira tabela a ser coletado
				for i in lista:
					ui.third_value.Append(i)
				ui.third_value.SetStringSelection(lista[value1])
				ui.third.Show(True)
				ui.third_value.Show(True)
				value1 = ui.third_value.GetSelection()
				#carrega tabela A6
				ui.dados=waterNext('./a6/' + lista[value1] + '.csv')
				#atualiza valores de pressão
				for i in ui.dados.dados['Temperature']:
					ui.dados.dados['Pressure'] = numpy.append(ui.dados.dados['Pressure'],float(lista[value1]))
				#interpola dados
				for i,u in zip(ui.dados.dados['index'],ui.dados.dados['unit_index']):
					inter = sp.interp1d(ui.dados.dados[escolha2], ui.dados.dados[i],kind='linear')
					valores += ( i.rjust(13) +"\t\t=\t" + (str(inter(value2))+" "+ u).ljust(11)  + "\n")
					vlr[i] = float(inter(value2))
				vlr['Titulo'] = 1
				vlr['Pressure'] = int(vlr['Pressure'])

		else:
			#se estiver abaixo do valor liquid
			vlr['superaquecido']=-1
			valores= "Esta no estado liquido comprimido\n".center(80) + "\n"
			lista=['5','10','15','20','30','50']
			#atualiza valor da pressão a ser coletado
			value1 = ui.third_value.GetSelection()
			ui.third_value.Clear()
			for i in lista:
				ui.third_value.Append(i)
			ui.third_value.SetStringSelection(lista[value1])
			ui.third.Show(True)
			ui.third_value.Show(True)
			value1 = ui.third_value.GetSelection()
			#carrega tabela A7
			ui.dados=waterNext('./a7/' + lista[value1] + '.csv')
			for i in ui.dados.dados['Temperature']:
				ui.dados.dados['Pressure'] = numpy.append(ui.dados.dados['Pressure'],float(lista[value1]))
			#interpola dados
			for i,u in zip(ui.dados.dados['index'],ui.dados.dados['unit_index']):
				inter = sp.interp1d(ui.dados.dados[escolha2], ui.dados.dados[i],kind='linear')
				valores += ( i.rjust(13) +"\t\t=\t" + (str(inter(value2))+" "+ u).ljust(11)  + "\n")
				vlr[i] = inter(value2)
			vlr['Titulo'] = 0
		
	#caso ocorra algum estado inesperado
	except ValueError, ex:
		if(vlr['superaquecido']):
			value1 = float(lista[ui.third_value.GetSelection()])
		if((value1) and (value2)):
			valores+= "\nFaixa de valores fora do intervalo de amostra\n\n"
			if(vlr['superaquecido']==0):
				try:
					valores += "%.2f < %s < %.2f\n" % (min(ui.dados.dados[escolha1]),ui.dados.dados['more'][ui.first.GetSelection()] , max(ui.dados.dados[escolha1]) )
					valores += "%.3e < %s < %.3e\n" % (min(ui.dados.dados[escolha2+'_min']),ui.dados.dados['more'][ui.second.GetSelection()+2], max(ui.dados.dados[escolha2+'_max']) )
				except Exception, ex:
					pass
			else:
				valores += "%.3e < %s < %.3e\n" % (min(ui.dados.dados[escolha2]),ui.dados.dados['more'][ui.second.GetSelection()+2], max(ui.dados.dados[escolha2]) )
				valores+= "\nSelecione um valor de pressão valido para a entrada desejada"
		else:
			valores += "\nEntre com um valor!\n"
	except Exception, ex:
		valores= "\nEntre com um valor\n"
		pass

	vlr['data'] = valores
	return vlr


if __name__ == "__main__":
	print 'Not this one'
	

