
import Forge

class CoalActions():
	"""docstring for CoalActions"""

	@staticmethod
	def renderPreview():
		renderer = 'C:/Program Files/3Delight/bin/renderdl.exe'
		# file     = 'E:/141031_defaultProject/maya/3delight/rib_scene_001/rib/rib_python2.rib'
		file     = 'E:/141031_defaultProject/maya/3delight/untitled/rib/untitled_renderPass_0001.rib'
		flag     = '-id'
		command  = '%s %s %s' %( renderer, flag, file )

		# define class
		Fprocess = Forge.core.Process()

		Fprocess.launch( command=command )

	@staticmethod
	def render():
		renderer = 'C:/Program Files/3Delight/bin/renderdl.exe'
		file     = 'E:/141031_defaultProject/maya/3delight/rib_scene_001/rib/rib_python2.rib'

		command  = '%s %s' %( renderer, file )

		# define class
		Fprocess = Forge.core.Process()

		Fprocess.launch( command=command )
