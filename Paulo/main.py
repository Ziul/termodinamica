#!/usr/bin/python
# -*- coding:utf-8 -*-
import curses
from interface import *

#inicializa curses
if __name__ == '__main__':
	curses.wrapper(MyApp)
