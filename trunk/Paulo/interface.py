# -*- coding:utf-8 -*-
import curses
from curses import panel
from saida import *
import sys

class Data(object):
	first=[]
	second=[]
	third_value='10'
	results=''
	def __init__(self,screen):
		self.first=[]
		self.second=[]
		self.screen=screen

class Menu(object):

	def __init__(self, items, stdscreen):
		self.window = stdscreen.subwin(0,0)
		self.window.keypad(1)
		self.panel = panel.new_panel(self.window)
		self.panel.hide()
		panel.update_panels()

		self.position = 0
		self.items = items['names']
		self.unit = items['unit']
		self.values=[' ' for i in range(len(items['names']))]

	def navigate(self, n):
		self.position += n
		self.position %= len(self.items)

	def calc(self):
		try:			
			data = Data(self.window)
			data.first.append(self.items[0][0])
			data.second.append(self.items[1][0])
			data.first.append(self.values[0])
			data.second.append(self.values[1])
			self.window.addstr(6,3,saida(data) ,curses.A_NORMAL)
			del data
		except Exception, ex:
			self.window.addstr(6,3,str(ex) + '\n' + str(data.first) ,curses.A_REVERSE)

	def display(self):
		self.panel.top()
		self.panel.show()
		self.window.clear()

		while True:
			self.window.refresh()
			panel.update_panels()
			self.window.clear()
			self.panel.hide()
			curses.doupdate()
			msg=''
			for index, (item,u) in enumerate(zip(self.items,self.unit)):
				if index == self.position:
					mode = curses.A_REVERSE
				else:
					mode = curses.A_NORMAL
				if(len(item)<=1):
					msg = '%d. %s' % (index, item[0])  + str(self.values[index])
				else:
					msg = '%d. < %s >'.ljust(20) % (index, item[0]) + str(self.values[index]).rjust(5) + str(u[0]).rjust(6)+ '\n'
				self.window.addstr(1+index, 1, msg, mode)

			#key = self.window.getch()
			key = self.window.getkey()

			if (key == '\n'):
				if(self.position==  len(self.items)-1):
					break;
				else:
					self.calc()
					self.window.refresh()
					panel.update_panels()
					curses.doupdate()

			if key == 'KEY_UP':
				self.navigate(-1)

			elif key == 'KEY_DOWN':
				self.navigate(1)

			elif key == 'KEY_RIGHT':
				self.items[self.position].append(self.items[self.position][0])
				self.items[self.position].remove(self.items[self.position][0])
				
				self.unit[self.position].append(self.unit[self.position][0])
				self.unit[self.position].remove(self.unit[self.position][0])

			elif key == 'KEY_LEFT':
				self.items[self.position].insert(0,self.items[self.position].pop())
				self.unit[self.position].insert(0,self.unit[self.position].pop())

			else:
				if(self.position != len(self.items)-1):
					self.window.addstr(self.position+1, 60, key, curses.A_NORMAL)
					curses.echo()
					texto = key + self.window.getstr()
					try:
						self.values[self.position] = float(texto)
					except Exception, ex:
						self.window.addstr(self.position+1, 40, str(ex), curses.A_NORMAL)
					self.window.addstr(self.position+1, 60, key, curses.A_NORMAL)
					curses.noecho()
					sys.stdout.flush()

class SubMenu(Menu):
	
	def __init__(self, data, stdscreen):
		self.window = stdscreen.subwin(0,0)
		self.window.keypad(1)
		self.panel = panel.new_panel(self.window)
		self.panel.hide()
		panel.update_panels()

		self.position = 0
		self.items = ['Pressure']
		self.values=data
		
	def display(self):
		self.panel.top()
		self.panel.show()
		self.window.clear()
		index=0
		while True:
			self.window.refresh()
			panel.update_panels()
			self.window.clear()
			self.panel.hide()
			curses.doupdate()
			self.window.addstr(0, 15, 'é necessário a entrada de um novo valor de pressão', curses.A_NORMAL)
			msg = '%s\t\t<%s> [kPa]' % ( self.items[0],self.values[index])
			self.window.addstr(3, 0, msg, curses.A_REVERSE)
			
			key = self.window.getkey()
			
			if (key == '\n'):
				return self.values[index]
			
			elif key == 'KEY_RIGHT':
				index +=1
				index %= len(self.values)
				
			elif key == 'KEY_LEFT':
				index -=1
				index %= len(self.values)

class MyApp(object):

	def __init__(self, stdscreen):
		self.screen = stdscreen
		#curses.curs_set(0)

		opcoes ={'names':[ 
			['Temperature','Pressure'],
			['Volume','Energy','Enthalpy','Entropy'],
			['exit']
			],
			'unit':[
			['[°C]','[kPa]'],
			['[m³/kg]','[kJ/kg]','[kJ/kg]','[kJ/kg.K]'],
			['']
			]}

		primeira = Menu(opcoes, self.screen)

		res= primeira.display()
		curses.endwin()
		print res
