
import sys

if 'launchCoal' in sys.modules:
	del sys.modules['launchCoal']
else:
	sys.path.append('F:/dev')
	sys.path.append('F:/dev/Coal/bin/')

import launchCoal
