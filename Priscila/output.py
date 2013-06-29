#!/usr/bin/python
# -*- coding:utf-8 -*-

from pontos import *

def saida(ui):
	
	try:
		ui.dados=water(ui.path)
		escolha1 = ui.dados.dados['names'][ui.first.GetSelection()]
		escolha2 = ui.dados.dados['names'][ui.second.GetSelection()+2]
		value1 = float(ui.first_value.GetValue())
		value2 = float(ui.second_value.GetValue())
		inter_min = sp.interp1d(ui.dados.dados[escolha1], ui.dados.dados[escolha2+"_min"],kind='linear')
		inter_max = sp.interp1d(ui.dados.dados[escolha1], ui.dados.dados[escolha2+"_max"],kind='linear')
	except Exception, ex:
		ui.results= "Dados vazios ou não validos\n\n" + str(ex)
		ui.text.SetValue(ui.results)

	try:
		valores=''
		ui.third_value.Hide()
		ui.third.Hide()
		if (value2>=inter_min(value1)):
			if (value2<=inter_max(value1)):
				valores= "Esta no estado de água saturada\n".center(80) + "\n"
				for i,u in zip(ui.dados.dados['index'],ui.dados.dados['unit_index']):
					inter = sp.interp1d(ui.dados.dados[escolha1], ui.dados.dados[i],kind='linear')
					valores += ( i.rjust(13) +"\t\t=\t" + (str(inter(value1))+" "+ u).ljust(11)  + "\n")
				titulo =((inter(value1) - inter_min(value1)))/ (inter_min(value1)+inter_max(value1))
				valores += "        Titulo\t\t=\t"  + str(titulo) + "\n"
				valores += "----------------------------------------------------------------------------------------\n"
				valores += "Valores precisos:\n".center(90) + "\n"
				for i,u in zip(ui.dados.dados['names'][2:],ui.dados.dados['unit'][2:]):
					if((i != 'Pressure') and (i != 'Temperature') ):
						precise = ui.dados.dados[i+'_min'] + titulo * (ui.dados.dados[i+'_min'] + ui.dados.dados[i+'_max'])/2
						inter = sp.interp1d(ui.dados.dados[escolha1], precise,kind='linear')
						valores += ( i.rjust(13) +"\t\t=\t" + (str(inter(value1))+" "+ u).ljust(11)  + "\n")
				
				
			else:
				valores= "Esta no estado vapor superaquecido\n".center(80) + "\n"	# (acima do intervalo para saturada)
				lista=['10', '50', '100' , '200',  '300',  '400',  '500' , '600',  '800','1000', '2000','3000','4000','5000','10000','20000','30000','40000','50000','60000']
				print "Esta no estado vapor superaquecido"
				#ui.third =  wx.StaticText(ui.Painel, label='Pressão [kPa]', pos=(50, 90))
				value1 = ui.third_value.GetSelection()
				ui.third_value.Clear()
				for i in lista:
					ui.third_value.Append(i)
				ui.third_value.SetStringSelection(lista[value1])
				ui.third.Show(True)
				ui.third_value.Show(True)
				value1 = ui.third_value.GetSelection()
				ui.dados=waterNext('./a6/' + lista[value1] + '.csv')
				for i in ui.dados.dados['Temperature']:
					ui.dados.dados['Pressure'] = numpy.append(ui.dados.dados['Pressure'],float(lista[value1]))
				for i,u in zip(ui.dados.dados['index'],ui.dados.dados['unit_index']):
					inter = sp.interp1d(ui.dados.dados[escolha2], ui.dados.dados[i],kind='linear')
					valores += ( i.rjust(13) +"\t\t=\t" + (str(inter(value2))+" "+ u).ljust(11)  + "\n")

		else:
			valores= "Esta no estado liquido comprimido\n".center(80) + "\n"
			lista=['5','10','15','20','30','50']
			print "Esta no estado liquido comprimido"
			#ui.third =  wx.StaticText(ui.Painel, label='Pressão [MPa]', pos=(50, 90))
			value1 = ui.third_value.GetSelection()
			ui.third_value.Clear()
			for i in lista:
				ui.third_value.Append(i)
			ui.third_value.SetStringSelection(lista[value1])
			ui.third.Show(True)
			ui.third_value.Show(True)
			value1 = ui.third_value.GetSelection()
			ui.dados=waterNext('./a7/' + lista[value1] + '.csv')
			for i in ui.dados.dados['Temperature']:
				ui.dados.dados['Pressure'] = numpy.append(ui.dados.dados['Pressure'],float(lista[value1]))
			for i,u in zip(ui.dados.dados['index'],ui.dados.dados['unit_index']):
				inter = sp.interp1d(ui.dados.dados[escolha2], ui.dados.dados[i],kind='linear')
				valores += ( i.rjust(13) +"\t\t=\t" + (str(inter(value2))+" "+ u).ljust(11)  + "\n")
		
				
	except ValueError, ex:
		valores+= "\nFaixa de valores fora do intervalo de amostra\n" + str(ex)
		valores+= "\n\nProvavelmente fora do intervalo de interpolação\n\n\n" 
		
		valores += "%s: %.2e - %.2e\n" % (ui.dados.dados['more'][ui.first.GetSelection()],min(ui.dados.dados[escolha1]) , max(ui.dados.dados[escolha1]))
		
		try:
			print "%s: %.2e - %.2e\n" % (ui.dados.dados['more'][ui.second.GetSelection()],min(ui.dados.dados[escolha2]) , max(ui.dados.dados[escolha2]) )
		except Exception, ex:
			valores += "%s minima: %.2e - %.2e\n" % (ui.dados.dados['more'][ui.second.GetSelection()+2],min(ui.dados.dados[escolha2+'_min']) , max(ui.dados.dados[escolha2+'_min']) )
			valores +="%s máxima: %.2e - %.2e\n" % (ui.dados.dados['more'][ui.second.GetSelection()+2],min(ui.dados.dados[escolha2+'_max']) , max(ui.dados.dados[escolha2+'_max']) )

		
	return valores


if __name__ == "__main__":
	print 'Not this one'
	

