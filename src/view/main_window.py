import PySimpleGUI as sg

class MainWindow(object):
	def __init__(self):
		sg.theme('DarkAmber')
		self.menu_form = [["File",["&Open"]], \
						["Help", "!About..."]]
		self.menu_bar = [[sg.Menu(self.menu_form)]]