# -*- coding:utf-8 -*-

import csv
import scipy.interpolate as sp
import numpy

'''
 Esta classe carrega os dados da tabela A4 ou A5e os mantem organizados
 nos seguintes vetores:
		self.dados['Temperature']	<- coluna de temperatura
		self.dados['Pressure']		<- coluna de pressão
		self.dados['Volume_min']	<- coluna de volume liquid
		self.dados['Volume_max'] = 	<- coluna de volume vapor
		self.dados['Energy_min'] = 	<- coluna de energia liquid
		self.dados['Energy_max'] = 	<- coluna de energia vapor
		self.dados['Enthalpy_min'] = <- coluna de entalpia liquid
		self.dados['Enthalpy_max'] = <- coluna de entalpia vapor
		self.dados['Entropy_min'] = <- coluna de entropia liquid
		self.dados['Entropy_max'] = <- <- coluna de entalpia vapor
'''
class water(object):
	""" Class doc """
	#Temperatura
	Temperature=numpy.array([0])
	#Pressão
	Press=numpy.array([0])
	#Volume
	Volume_min=numpy.array([0])
	Volume_max=numpy.array([0])
	#Energia
	Energy_min=numpy.array([0])
	Energy_max=numpy.array([0])
	#Entalpia
	Enthalpy_min=numpy.array([0])
	Enthalpy_max=numpy.array([0])
	#Entropia
	Entropy_min=numpy.array([0])
	Entropy_max=numpy.array([0])
	
	def __init__ (self,path):
		""" Class initialiser """
		# abre arquivo
		csvfile=open(path, 'rb')
		# lê dados, considerando arquivo csv usando virgula como separador de dados
		reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
		for row in reader:
			self.Temperature=numpy.append(self.Temperature,float(row[0]))
			self.Press=numpy.append(self.Press,float(row[1]))
			self.Volume_min=numpy.append(self.Volume_min,float(row[2]))
			self.Volume_max=numpy.append(self.Volume_max,float(row[3]))
			self.Energy_min=numpy.append(self.Energy_min,float(row[4]))
			#self.Temperature=numpy.append(self.Temperature,float(row[5])
			self.Energy_max=numpy.append(self.Energy_max,float(row[6]))
			self.Enthalpy_min=numpy.append(self.Enthalpy_min,float(row[7]))
			#self.Temperature=numpy.append(self.Temperature,float(row[8]))
			self.Enthalpy_max=numpy.append(self.Enthalpy_max,float(row[9]))
			self.Entropy_min=numpy.append(self.Entropy_min,float(row[10]))
			#self.Temperature=numpy.append(self.Temperature,float(row[11])
			self.Entropy_max=numpy.append(self.Entropy_max,float(row[12]))
		self.Temperature=numpy.delete(self.Temperature,0)
		self.Press=numpy.delete(self.Press,0)
		self.Volume_min=numpy.delete(self.Volume_min,0)
		self.Volume_max=numpy.delete(self.Volume_max,0)
		self.Energy_min=numpy.delete(self.Energy_min,0)
		self.Energy_max=numpy.delete(self.Energy_max,0)
		self.Enthalpy_min=numpy.delete(self.Enthalpy_min,0)
		self.Enthalpy_max=numpy.delete(self.Enthalpy_max,0)
		self.Entropy_min=numpy.delete(self.Entropy_min,0)
		self.Entropy_max=numpy.delete(self.Entropy_max,0)
		# Preenche com as unidades e os nomes em inglês e português
		self.dados={'names':['Temperature','Pressure','Volume','Energy','Enthalpy','Entropy'],
			'unit':['[°C]','[kPa]','[m³/kg]','[kJ/kg]','[kJ/kg]','[kJ/kg.K]'],
			'more':['Temperatura', 'Pressão', 'Volume Especifico','Energia Interna', 'Entalpia', 'Entropia'],
			'index':['Temperature','Pressure','Volume_min','Volume_max','Energy_min','Energy_max','Enthalpy_min','Enthalpy_max','Entropy_min','Entropy_max'],
			'unit_index':['[°C]','[kPa]','[m³/kg]','[m³/kg]','[kJ/kg]','[kJ/kg]','[kJ/kg]','[kJ/kg]','[kJ/kg.K]','[kJ/kg.K]'],}
		# Estrutura o dado para acesso do usuario
		self.dados['Temperature'] = self.Temperature
		self.dados['Pressure'] = self.Press
		self.dados['Volume_min'] = self.Volume_min
		self.dados['Volume_max'] = self.Volume_max
		self.dados['Energy_min'] = self.Energy_min
		self.dados['Energy_max'] = self.Energy_max
		self.dados['Enthalpy_min'] = self.Enthalpy_min
		self.dados['Enthalpy_max'] = self.Enthalpy_max
		self.dados['Entropy_min'] = self.Entropy_min
		self.dados['Entropy_max'] = self.Entropy_max
	# Função de suporte, onde todos os dados são impressos
	def print_all(self):
		for i in self.dados['index']:
			print i
			print self.dados[i]

'''
 Esta classe carrega os dados da tabela A6 ou A7 e os mantem organizados
 nos seguintes vetores:
		self.dados['Temperature']	<- coluna de temperatura
		self.dados['Pressure']		<- coluna de pressão
		self.dados['Volume']	<- coluna de volume
		self.dados['Energy'] = 	<- coluna de energia
		self.dados['Enthalpy'] = <- coluna de entalpia
		self.dados['Entropy'] = <- <- coluna de entropia
'''
class waterNext(object):
	""" Class doc """
	#Temperatura
	Temperature=numpy.array([0])
	#Pressão
	Press=numpy.array([0])
	#Volume
	Volume=numpy.array([0])
	#Energia
	Energy=numpy.array([0])
	#Entalpia
	Enthalpy=numpy.array([0])
	#Entropia
	Entropy=numpy.array([0])
	
	def __init__ (self,path):
		""" Class initialiser """
		csvfile=open(path, 'rb')
		reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
		for row in reader:
			self.Temperature=numpy.append(self.Temperature,float(row[0]))
			self.Volume=numpy.append(self.Volume,float(row[1]))
			self.Energy=numpy.append(self.Energy,float(row[2]))
			self.Enthalpy=numpy.append(self.Enthalpy,float(row[3]))
			self.Entropy=numpy.append(self.Entropy,float(row[4]))
		self.Temperature=numpy.delete(self.Temperature,0)
		self.Press=numpy.delete(self.Press,0)
		self.Volume=numpy.delete(self.Volume,0)
		self.Energy=numpy.delete(self.Energy,0)
		self.Enthalpy=numpy.delete(self.Enthalpy,0)
		self.Entropy=numpy.delete(self.Entropy,0)
		'''completing dictionary'''
		self.dados={'names':['Temperature','Pressure','Volume','Energy','Enthalpy','Entropy'],
			'unit':['[°C]','[kPa]','[m³/kg]','[kJ/kg]','[kJ/kg]','[kJ/kg.K]'],
			'more':['Temperatura', 'Pressão', 'Volume Especifico','Energia Interna', 'Entalpia', 'Entropia'],
			'index':['Temperature','Pressure','Volume','Energy','Enthalpy','Entropy'],
			'unit_index':['[°C]','[kPa]','[m³/kg]','[kJ/kg]','[kJ/kg]','[kJ/kg.K]']}
		self.dados['Temperature'] = self.Temperature
		self.dados['Pressure'] = self.Press
		self.dados['Volume'] = self.Volume
		self.dados['Energy'] = self.Energy
		self.dados['Enthalpy'] = self.Enthalpy
		self.dados['Entropy'] = self.Entropy
	def print_all(self):
		for i in self.dados['index']:
			print i
			print self.dados[i]
		
if __name__ == '__main__':
	print "Este não!"


