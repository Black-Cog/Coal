
import sys

if 'launchCoal' in sys.modules:
	del sys.modules['launchCoal']
else:
	sys.path.append('F:/software/coal_0.0.0.1dev/')
	sys.path.append('F:/software/coal_0.0.0.1dev/Coal/bin')

import launchCoal
