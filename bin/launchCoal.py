import sys
from PySide import QtCore, QtGui

parentPath = '/'.join( sys.path[0].replace('\\', '/').split('/')[:-2] )
sys.path.append( parentPath )

import Forge


# print sys.path
# import Forge
# import Forge.ForgeCore
# global checkInterpretor
# Fpython = Forge.ForgeCore.Python()
# print Fpython.interpreter()
# sys.argv[0].replace('\\', '/').split('/')[-1]

# print sys.path[0]
# print parentPath
# check
# checkInterpretor()


import Coal

if Forge.core.Python().interpreter() == 'launchCoal' :
	app = QtGui.QApplication(sys.argv)
	widget = Coal.ui.ClassLoader()
	widget.app().showMaximized()
	sys.exit( app.exec_() )
else :
	widget = Coal.ui.ClassLoader()
	widget.app().showMaximized()

