#!/usr/bin/python
# -*- coding:utf-8 -*-
import curses																
from curses import panel													 
from saida import *

class Data(object):
	first=[]
	second=[]
	third=''
	results=''
	def __init__(self):
		pass

class Menu(object):														  

	def __init__(self, items, stdscreen):									
		self.window = stdscreen.subwin(0,0)								  
		self.window.keypad(1)												
		self.panel = panel.new_panel(self.window)							
		self.panel.hide()													
		panel.update_panels()												

		self.position = 0													
		self.items = items['names']
		self.items.append(['exit'])
		self.values=[0.0,0.0,' ']

	def navigate(self, n):												   
		self.position += n												   
		if self.position < 0:												
			self.position = 0												
		elif self.position >= len(self.items):							   
			self.position = len(self.items)-1								

	def calc(self):
			data = Data()
			data.first.append(self.items[0][0])
			data.second.append(self.items[1][0])
			data.first.append(self.values[0])
			data.second.append(self.values[1])
			self.window.addstr(5,3,saida(data),curses.A_NORMAL)
			
	def display(self):													   
		self.panel.top()													 
		self.panel.show()													
		self.window.clear()												  

		while True:														  
			self.window.refresh()											
			curses.doupdate()
			msg=''
			for index, item in enumerate(self.items):
				if index == self.position:								   
					mode = curses.A_REVERSE								  
				else:														
					mode = curses.A_NORMAL								   
				if(len(item)<=1):
					msg = '%d. %s' % (index, item[0])  + str(self.values[index])
				else:
					msg = '%d. < %s >'.ljust(20) % (index, item[0]) +'\t' + str(self.values[index]).rjust(5) + '\n'
				self.window.addstr(1+index, 1, msg, mode)		

			#key = self.window.getch()
			key = self.window.getkey()

			if (key == 'KEY_ENTER') or (key == '\n'):
				if(self.position== 2):
					break;
				else:
					self.calc()
			
			if key == 'KEY_UP':									   
				self.navigate(-1)											

			elif key == 'KEY_DOWN':
				self.navigate(1)

			elif key == 'KEY_RIGHT':
				self.items[self.position].append(self.items[self.position][0])
				self.items[self.position].remove(self.items[self.position][0])
			
			elif key == 'KEY_LEFT':	
				self.items[self.position].insert(0,self.items[self.position].pop())
				
			else:
				try:

					if(self.position != len(self.items)-1):
						self.window.addstr(10, 10, key, curses.A_NORMAL)
						curses.echo()
						texto = key + self.window.getstr()
						self.values[self.position] = float(texto)
						curses.noecho()
				except Exception, ex:
					pass
			self.window.clear()												  
			self.panel.hide()													
			panel.update_panels()												
			curses.doupdate()

class MyApp(object):														 

	def __init__(self, stdscreen):										   
		self.screen = stdscreen											  
		curses.curs_set(0)												   

		opcoes ={'names':[['Temperature','Pressure'],['Volume','Energy','Enthalpy','Entropy']]}
		
		primeira = Menu(opcoes, self.screen)
			   
		primeira.display()												  

if __name__ == '__main__':													   
	curses.wrapper(MyApp)  
