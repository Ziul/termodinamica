# -*- coding:utf-8 -*-

import csv
import scipy.interpolate as sp
import numpy

#try:
	#import pylab
#except:
	#print "Erro ao importar a MatPlotLib"
	#print "Consute http://sourceforge.net/projects/matplotlib/files/matplotlib/matplotlib-1.2.0/"

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
		csvfile=open(path, 'rb')
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
		'''completing dictionary'''
		self.dados={'names':['Temperature','Pressure','Volume','Energy','Enthalpy','Entropy'],
			'unit':['[°C]','[kPa]','[m³/kg]','[kJ/kg]','[kJ/kg]','[kJ/kg.K]'],
			'more':['Temperatura', 'Pressão', 'Volume Especifico','Energia Interna', 'Entalpia', 'Entropia'],
			'index':['Temperature','Pressure','Volume_min','Volume_max','Energy_min','Energy_max','Enthalpy_min','Enthalpy_max','Entropy_min','Entropy_max'],
			'unit_index':['[°C]','[kPa]','[m³/kg]','[m³/kg]','[kJ/kg]','[kJ/kg]','[kJ/kg]','[kJ/kg]','[kJ/kg.K]','[kJ/kg.K]'],}
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
	def print_all(self):
		for i in self.dados['index']:
			print i
			print self.dados[i]
	#def plot(self,escolha1,escolha2):
		#pylab.title(escolha1 + " x " + escolha2)
		#pylab.xlabel(escolha1)
		#pylab.ylabel(escolha2)
		#pylab.plot(self.dados[escolha1],self.dados[escolha2+"_min"],'r--',self.dados[escolha1],self.dados[escolha2+"_max"])
		#pylab.show()

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

class dados(object):
	x=numpy.array([0])
	y=numpy.array([0])
	linear=numpy.array([0])
	cubic=numpy.linspace(0, 1, 5)
	def __init__(self,path):
		csvfile=open(path, 'rb')
		reader = csv.reader(csvfile, delimiter=';', quotechar='\"')
		for row in reader:
			self.x= numpy.hstack([self.x,float(row[0])])
			self.y= numpy.hstack([self.y,float(row[1])])
		self.linear=sp.interp1d(self.x, self.y,kind='linear')
		self.cubic=sp.interp1d(self.x, self.y,kind='cubic')
	#def plot(self):
		#pylab.plot(self.x, self.linear(self.x),'bo',self.x, self.cubic(self.x),'r--')
		#pylab.text(self.x.max()/2, self.y.max()/2, "Linear",color='blue')
		#pylab.text(self.x.max()/2, self.y.max()/2-2/range(self.y), "Cubica",color='red')
		#pylab.show()
	def value(self,v):
		return self.cubic(v)
	def exist(self,x,y):
		return float(y-self.value(x))
		
if __name__ == '__main__':
	print "Este não!"


