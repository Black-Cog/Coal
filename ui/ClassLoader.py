
import sys
import Anvil.core
import Main
import Coal.core

class ClassLoader():

	def __init__(self):
		# load main ui
		self.main = Main.Main()

	def app( self ):
		return self.main.window

