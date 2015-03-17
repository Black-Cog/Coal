
import Coal

class FnShader( object ):
	"""docstring for FnShader"""

	@staticmethod
	def queryShader( arg ):
		path    = arg.textfield_pathWorkspace.text()
		slPath  = '%s/shader/BCmonolithic.sl' %( path )
		sdlPath = '%s/shader/BCmonolithic.sdl' %( path )

		slFile  = open( slPath )
		sdlFile = open( sdlPath )
		attrList = []

		# query attr and type inside sdl file
		for i in sdlFile:
			if i.startswith( '"' ):
				tmpSplit = i.split( '"' )
				if len( tmpSplit ) == 5:
					if tmpSplit[4].startswith( ' 2' ):
						tmpList = [ tmpSplit[1] ]
						if tmpSplit[4].startswith( ' 2 1' ) : tmpList.append( 'float' )
						if tmpSplit[4].startswith( ' 2 3' ) : tmpList.append( 'color' )
						if tmpSplit[4].startswith( ' 2 4' ) : tmpList.append( 'string' )
						attrList.append(tmpList)

		# query defalut value inside sl file
		for attr in attrList:
			for line in slFile:
				if attr[0] in line and not '//' in line:
					tmpValue = line.split( '=' )[-1].replace(' ', '').replace(';', '').replace('\n', '')

					# fix color error
					if '(' in tmpValue:
						strValues = tmpValue.replace( '(', '' ).replace( ')', '' ).split( ',' )
						tmpValue  = str( [ float(strValues[0]), float(strValues[1]), float(strValues[2]) ] )

					attr.append( tmpValue )
					break

		return attrList
