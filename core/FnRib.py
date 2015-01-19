
import Forge
import Coal

class FnRib( object ):
	"""docstring for FnRib"""

	@staticmethod
	def structFolders( path ):

		# define class
		Fsystem = Forge.core.System()

		# define path
		folderCamera = '%s/camera' %( path )
		folderLight  = '%s/light'  %( path )
		folderShader = '%s/shader' %( path )
		folderObject = '%s/object' %( path )
		folderStat   = '%s/stat'   %( path )
		folderImage  = '%s/image'  %( path )

		Fsystem.mkdir( path=[folderCamera, folderLight, folderShader, folderObject, folderStat, folderImage] )

	def setRibWorld( self, arg ):

		# define filename
		passname = 'beauty'
		path     = arg.textfield_pathWorkspace.text()
		filename = '%s/%s.rib' %( path, passname )
		shaders  = ['BCmonolithic']

		# define class
		Fsystem = Forge.core.System()

		# define meshs
		if arg.interpreter == 'maya' : meshs = self.getMayaMesh( arg )
		else : meshs = self.getMesh( arg )

		# define global inside content
		content  = self.ribGlobal( arg=arg, passname=passname )

		# define frame inside content
		content  += '\nFrameBegin 1'
		content  += '\n    WorldBegin'
		content  += '\n        ReadArchive "light/light.rib"'
		for shader in shaders:
			content  += '\n        ArchiveBegin "%s surface"' %( shader )
			content  += '\n            Surface "F:/dev/BCshading/sdl/BCmonolithic"'
			content  += '\n        ArchiveEnd'
		content  += '\n        ReadArchive "%s surface"' %( shaders[0] )
		for mesh in meshs:
			content += '\n        ReadArchive "object/%s.rib"' %( mesh )
		content  += '\n    WorldEnd'
		content  += '\nFrameEnd'
		content  += '\n'

		Fsystem.setFile( path=filename, content=content, type='w' )



	@staticmethod
	def ribGlobal( arg, passname ):
		"""Return string global"""

		formatMult   = arg.floatfield_formatMult.value()
		formatX      = int( arg.intfield_formatX.value() * formatMult )
		formatY      = int( arg.intfield_formatY.value() * formatMult )
		pixelSample  = arg.intfield_pixelSample.value()
		bucketSize   = arg.intfield_bucketSize.value()
		textureCache = arg.intfield_textureCache.value()
		filterType   = arg.dropmenus_filterType.value()
		filterSize   = arg.floatfield_filterSize.value()

		# define file content
		globalString  =  '\n#Black Cog Rib\n\n'
		globalString  += '\nFormat %i %i 1' %( formatX, formatY )
		globalString  += '\nPixelSamples %s %s' %( pixelSample, pixelSample )

		globalString  += '\nProjection "perspective" "fov" [ 60 ]'
		globalString  += '\nScale 1 1 -1'
		globalString  += '\nTranslate 0 0 -5'
		globalString  += '\nRotate 0 0 1 0'

		globalString  += '\nHider "raytrace"'
		globalString  += '\nOrientation "rh"'
		globalString  += '\nOption "trace" "integer diffuseraycache" [ 1 ]'

		globalString  += '\nOption "limits" "integer[2] bucketsize" [ %s %s ]' %( bucketSize, bucketSize )
		globalString  += '\nOption "limits" "integer texturememory" [ %s ]' %( textureCache )		
		globalString  += '\nOption "limits" "color othreshold" [ 0.996 0.996 0.996 ] "color zthreshold" [ 0.996 0.996 0.996 ]'

		globalString  += '\nDisplay "+image/%s_0001.exr" "exr" "rgba"' %( passname )
		globalString  += '\n    "float[4] quantize" [ 0 0 0 0 ]'
		globalString  += '\n    "string filter" [ "%s" ]' %( filterType )
		globalString  += '\n    "float[2] filterwidth" [ %s %s ]' %( filterSize, filterSize )
		globalString  += '\n    "string exrpixeltype" [ "float" ]'
		globalString  += '\nOption "statistics" "integer endofframe" [ 3 ] "string filename" [ "stat/%s_0001.txt" ]' %( passname )

		globalString  += '\n'
		return globalString

	@staticmethod
	def getMayaMesh( arg ):
		import maya.cmds

		path  = arg.textfield_pathWorkspace.text()
		meshs = maya.cmds.ls( type='mesh' )

		return meshs

	@staticmethod
	def getMesh( arg ):
		path  = arg.textfield_pathWorkspace.text()
		meshs = Forge.core.System().list( path=path, file=True, folder=False )

		return meshs

	def setMeshRib( self, arg ):
		"""Write Mesh Rib"""
		'@parameter string mesh Name of the shape.'
		import maya.cmds

		path  = arg.textfield_pathWorkspace.text()
		meshs = self.getMayaMesh( arg )

		for mesh in meshs:
			# init var
			filename   = '%s/object/%s.rib' %( path, mesh )
			face       = ' '
			vtxPerFace = ' '
			vtxIndex   = ' '
			vtxP       = ' '
			vtxN       = ' '
			stP        = ' '

			# init file
			rib = open( filename, 'w' )
			rib.write( '\n#Black Cog Rib\n\n' )
			rib.write( '\nObjectBegin "%s"' % ( mesh ) )
			rib.write( '\n  SubdivisionMesh "catmull-clark"' )
			rib.close()

			# vtxPerFace
			rib = open( filename, 'a' )
			rib.write( ' [ ' )
			countLine = 0
			countOp   = 0
			for i in maya.cmds.polyInfo( mesh, fv=True ):
				countVtx = 0
				item = i.split( ' ' )
				item.reverse()
				for j in item :
					if j.isdigit():
						countVtx += 1
				rib.write( '%i ' % ( countVtx ) )
				countLine += 1
				if countLine == 18 :
					countLine = 0
					countOp += 0.001
					rib.write( '\n    ' )
				if countOp > 10 :
					countOp = 0
					rib.close()
					rib = open( filename, 'a' )
			rib.write( ']\n' )
			rib.close()


			# vtxIndex
			rib = open( filename, 'a' )
			rib.write( '\n  [ ' )
			countLine = 0
			countOp   = 0
			for i in maya.cmds.polyInfo( mesh, fv=True ):
				item = i.split( ' ' )
				item.reverse()
				for j in item :
					if j.isdigit():
						rib.write( '%s ' % ( j ) )
						countLine += 1
						if countLine == 18 :
							countLine = 0
							countOp += 0.001
							rib.write( '\n    ' )
						if countOp > 10 :
							countOp = 0
							rib.close()
							rib = open( filename, 'a' )
			rib.write( ']\n' )
			rib.close()



			# interp
			rib = open( filename, 'a' )
			rib.write( '\n[ "interpolateboundary" "facevaryinginterpolateboundary" ] [ 1 0 1 0 ] [ 2 1 ] [ ]\n' )
			rib.close()

			# vtxP
			rib = open( filename, 'a' )
			rib.write( '\n  "vertex point P" [ ' )
			countLine = 0
			countOp   = 0
			for i in maya.cmds.getAttr( '%s.vrts' % ( mesh ), mi=True ):
				tmpP = maya.cmds.xform( '%s.pnts[%i]' % ( mesh, i ), q=True, t=True, ws=True )
				rib.write( '%s %s %s ' % ( str(round(tmpP[0], 7)), str(round(tmpP[1], 7)), str(round(tmpP[2], 7)) ) )
				countLine += 1
				if countLine == 4 :
					countLine = 0
					countOp += 0.001
					rib.write( '\n    ' )
				if countOp > 20 :
					countOp = 0
					rib.close()
					rib = open( filename, 'a' )
			rib.write( ']\n' )
			rib.close()

			# stP
			'''
			rib = open( filename, 'a' )
			rib.write( '\n  "facevarying float[2] st" [ ' )
			countLine = 0
			countOp   = 0
			for i in range( maya.cmds.polyEvaluate( mesh, uvcoord=True ) ):
				tmpST = maya.cmds.polyEditUV( '%s.map[%i]' % ( mesh, i ), q=True )
				rib.write( '%s %s ' % ( str(round(tmpST[0], 7)), str(round(tmpST[1], 7)) ) )
				countLine += 1
				if countLine == 6 :
					countLine = 0
					countOp += 0.001
					rib.write( '\n    ' )
				if countOp > 20 :
					countOp = 0
					rib.close()
					rib = open( filename, 'a' )
			rib.write( ']\n' )
			rib.close()
			'''

			# close file
			rib = open( filename, 'a' )
			rib.write( '\nObjectEnd\n' )
			rib.write( '\nAttributeBegin' )
			rib.write( '\n  ObjectInstance "%s"' % ( mesh ) )
			rib.write( '\nAttributeEnd' )
			rib.write( '\n' )
			rib.close()
