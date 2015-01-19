import sys
from PySide import QtCore, QtGui

parentPath = '/'.join( sys.path[0].replace('\\', '/').split('/')[:-2] )
sys.path.append( parentPath )

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

