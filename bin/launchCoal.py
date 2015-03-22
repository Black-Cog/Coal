

###############################################################################################
# Environment
###############################################################################################


import sys

softwareEnvironment = 'f:/software/'

FORGE_VERSION = '0.0.0.1dev'
ANVIL_VERSION = '0.0.0.1dev'

forgePath  = '%sforge_%s' %( softwareEnvironment, FORGE_VERSION )
anvilPath  = '%sanvil_%s' %( softwareEnvironment, ANVIL_VERSION )
parentPath = '/'.join( sys.path[0].replace('\\', '/').split('/')[:-2] )

envs = [ forgePath, anvilPath, parentPath ]

for env in envs:
	sys.path.append( env )


###############################################################################################
# Launcher
###############################################################################################


from PySide import QtCore, QtGui
import Forge
import Coal

# stand alone
if Forge.core.System().interpreter() == 'launchCoal' :
	app = QtGui.QApplication(sys.argv)
	widget = Coal.ui.ClassLoader()
	widget.app().showMaximized()
	sys.exit( app.exec_() )
# maya
else :
	widget = Coal.ui.ClassLoader()
	widget.app().showMaximized()

