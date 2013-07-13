#!/usr/bin/python
# -*- coding:utf-8 -*-
import janela
from pontos import *
import os

def termo(path):
	dado=water(path)
	save=water(path)
	j=janela.choose()
	j.buildme("Primeira entrada","Escolha a primeira entrada",[
		("{0} {1}".format(e,u) ) for e,u in zip(['Temperatura','Pressão'],dado.dados['unit'])
		])
	j.Show(False)
	escolha1 = dado.dados['names'][j.selection]



	dado.dados['names'].remove(dado.dados['names'][0])
	dado.dados['names'].remove(dado.dados['names'][0])

	dado.dados['unit'].remove(dado.dados['unit'][0])
	dado.dados['unit'].remove(dado.dados['unit'][0])

	dado.dados['more'].remove(dado.dados['more'][0])
	dado.dados['more'].remove(dado.dados['more'][0])


	j.buildme("Segunda entrada","Escolha a segunda entrada",[
		(str(e) +" {1}".format(e,u) ) for e,u in zip(dado.dados['more'],dado.dados['unit'])
		])
	j.Show(False)
	escolha2 = dado.dados['names'][j.selection]
	del j

	j=janela.read_value()
	j.buildme(escolha1,"Entre como valor para a " + save.dados['more'][save.dados['names'].index(escolha1)] +" "+ save.dados['unit'][save.dados['names'].index(escolha1)])
	j.Show(False)
	value1 = j.selection

	j=janela.read_value()
	j.buildme(escolha2,"Entre como valor para " + save.dados['more'][save.dados['names'].index(escolha2)] +" "+ save.dados['unit'][save.dados['names'].index(escolha2)])
	j.Show(False)
	value2 = j.selection

	inter_min = sp.interp1d(dado.dados[escolha1], dado.dados[escolha2+"_min"],kind='linear')
	inter_max = sp.interp1d(dado.dados[escolha1], dado.dados[escolha2+"_max"],kind='linear')

	try:
		
		if (value2>=inter_min(value1)):
			if (value2<=inter_max(value1)):
				valores= "Esta no estado de água saturada\n".center(90) + "\n"
				for i,u in zip(dado.dados['index'],dado.dados['unit_index']):
					inter = sp.interp1d(dado.dados[escolha1], dado.dados[i],kind='linear')
					valores += ( i.rjust(13) +"\t\t=\t" + (str(inter(value1))+" "+ u).ljust(11)  + "\n")
				titulo =((value2 - inter_min(value1)))/ (inter_max(value1)-inter_min(value1))
				valores += "        Titulo\t\t=\t"  + str(titulo) + "\n"
				valores += "--------------------------------------------------------------------------\n"
				valores += "Valores precisos:\n".center(55) + "\n"
				for i,u in zip(save.dados['names'][2:],save.dados['unit']):
					if((i != 'Pressure') and (i != 'Temperature') ):
						precise = dado.dados[i+'_min'] + titulo * (dado.dados[i+'_min'] + dado.dados[i+'_max'])/2
						inter = sp.interp1d(dado.dados[escolha1], precise,kind='linear')
						valores += ( i.rjust(13) +"\t\t=\t" + (str(inter(value1))+" "+ u).ljust(11)  + "\n")
							
			else:
				valores= "Esta no estado vapor superaquecido\n".center(90) + "\n"	# (acima do intervalo para saturada)
				j=janela.choose()
				lista=['10', '50', '100' , '200',  '300',  '400',  '500' , '600',  '800','1000', '2000','3000','4000','5000','10000','20000','30000','40000','50000','60000']
				j.buildme("Não é saturada","Entre novamente com o valor para a Pressão [kPa]",lista)
				j.Show(False)
				value1 = j.selection
				dado=waterNext('./a6/' + lista[value1] + '.csv')
				for i in dado.dados['Temperature']:
					dado.dados['Pressure'] = numpy.append(dado.dados['Pressure'],float(lista[value1]))
				#dado.print_all()
				for i,u in zip(dado.dados['index'],dado.dados['unit_index']):
					inter = sp.interp1d(dado.dados[escolha2], dado.dados[i],kind='linear')
					valores += ( i.rjust(13) +"\t\t=\t" + (str(inter(value2))+" "+ u).ljust(11)  + "\n")
				

		else:
			valores= "Esta no estado liquido comprimido\n".center(90) + "\n" # (abaixo do intervalo para saturada)

			j=janela.choose()
			lista=['5','10','15','20','30','50']
			j.buildme("Não é saturada","Entre novamente com o valor para a Pressão [kPa]",lista)
			j.Show(False)
			value1 = j.selection
			dado=waterNext('./a7/' + lista[value1] + '.csv')
			for i in dado.dados['Temperature']:
				dado.dados['Pressure'] = numpy.append(dado.dados['Pressure'],float(lista[value1]))
			#dado.print_all()
			for i,u in zip(dado.dados['index'],dado.dados['unit_index']):
				inter = sp.interp1d(dado.dados[escolha2], dado.dados[i],kind='linear')
				valores += ( i.rjust(13) +"\t\t=\t" + (str(inter(value2))+" "+ u).ljust(11)  + "\n")



	except ValueError:
		valores= "Faixa de valores fora do intervalo de amostra".center(90)

	j=janela.text()
	j.buildme(escolha2,valores)

	j.Show()
