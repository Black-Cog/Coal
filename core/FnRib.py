
import Forge
import Coal
import Anvil.core

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

	def setWorldRib( self, arg ):

		# define filename
		passname = arg.textfield_passname.text()
		path     = arg.textfield_pathWorkspace.text()
		filename = '%s/%s.rib' %( path, passname )
		shaders  = ['BCmonolithic']

		# define class
		Fsystem = Forge.core.System()

		# define meshs
		meshs = self.getMesh( arg )

		# define global inside content
		content  = self.ribGlobal( arg=arg, passname=passname )

		# define frame inside content
		content += '\nFrameBegin 1'
		content += '\n    WorldBegin'
		content += '\n'
		content += '\nAttribute "visibility" "integer camera" [ 1 ]'
		content += '\nAttribute "visibility" "integer transmission" [ 1 ]'
		content += '\nAttribute "visibility" "integer diffuse" [ 1 ]'
		content += '\nAttribute "visibility" "integer specular" [ 1 ]'
		content += '\n'
		for mesh in meshs:
			content += '\n        AttributeBegin'
			content += '\n            ReadArchive "shader/shader.rib"'
			content += '\n            ReadArchive "object/%s"' %( mesh )
			content += '\n        AttributeEnd'
			content += '\n'
		content += '\n    WorldEnd'
		content += '\nFrameEnd'
		content += '\n'

		Fsystem.setFile( path=filename, content=content, type='w' )

	@staticmethod
	def ribGlobal( arg, passname ):
		"""Return string global"""

		formatMult   = arg.floatfield_formatMult.getValue()
		formatX      = int( arg.intfield_formatX.getValue() * formatMult )
		formatY      = int( arg.intfield_formatY.getValue() * formatMult )
		pixelSample  = arg.intfield_pixelSample.getValue()
		bucketSize   = arg.intfield_bucketSize.getValue()
		textureCache = arg.intfield_textureCache.getValue()
		filterType   = arg.dropmenus_filterType.getValue()
		filterSize   = arg.floatfield_filterSize.getValue()

		indirectDiffuse  = int( arg.checkbox_indirectDiffuse.getValue() )
		indirectSpecular = int( arg.checkbox_indirectSpecular.getValue() )
		cropEnable = arg.checkbox_crop.getValue()
		if cropEnable:
			cropMinX = arg.floatfield_cropMinX.getValue()
			cropMaxX = arg.floatfield_cropMaxX.getValue()
			cropMinY = arg.floatfield_cropMinY.getValue()
			cropMaxY = arg.floatfield_cropMaxY.getValue()
		else:
			cropMinX = 0
			cropMaxX = 1
			cropMinY = 0
			cropMaxY = 1

		# define file content
		globalString  =  '\n#Black Cog Rib\n\n'
		globalString  += '\nFormat %i %i 1' %( formatX, formatY )
		globalString  += '\nPixelSamples %s %s' %( pixelSample, pixelSample )
		globalString  += '\nCropWindow %s %s %s %s' %( cropMinX, cropMaxX, cropMinY, cropMaxY )

		globalString  += '\nHider "raytrace"'
		# globalString  += '\nOrientation "rh"'
		globalString  += '\nOption "trace" "integer diffuseraycache" [ 1 ]'

		globalString  += '\nOption "limits" "integer[2] bucketsize" [ %s %s ]' %( bucketSize, bucketSize )
		globalString  += '\nOption "limits" "integer texturememory" [ %s ]' %( textureCache )		
		globalString  += '\nOption "limits" "color othreshold" [ 0.996 0.996 0.996 ] "color zthreshold" [ 0.996 0.996 0.996 ]'

		globalString  += '\nOption "user" "integer diffuseIndirectEnable" [ %s ]' %( indirectDiffuse )
		globalString  += '\nOption "user" "integer specularIndirectEnable" [ %s ]' %( indirectSpecular )

		globalString  += '\nDisplay "+image/%s_0001.exr" "exr" "rgba"' %( passname )
		globalString  += '\n    "float[4] quantize" [ 0 0 0 0 ]'
		globalString  += '\n    "string filter" [ "%s" ]' %( filterType )
		globalString  += '\n    "float[2] filterwidth" [ %s %s ]' %( filterSize, filterSize )
		globalString  += '\n    "string exrpixeltype" [ "float" ]'
		globalString  += '\nOption "statistics" "integer endofframe" [ 3 ] "string filename" [ "stat/%s_0001.txt" ]' %( passname )

		globalString  += '\nReadArchive "camera/camera.rib"'
		globalString  += '\nReadArchive "light/light.rib"'

		globalString  += '\n'
		return globalString


	@staticmethod
	def getMayaMesh( arg ):
		import maya.cmds

		path  = arg.textfield_pathWorkspace.text()
		meshsFullname = maya.cmds.ls( type='mesh', long=True, visible=True )
		meshs = []

		for mesh in meshsFullname:
			splitName = mesh.split('|')
			if len( splitName ) > 1 : meshs.append( splitName[-1] )

		return meshs

	@staticmethod
	def getMesh( arg ):
		path  = '%s/object' %( arg.textfield_pathWorkspace.text() )
		meshs = Forge.core.System().list( path=path, file=True, folder=False )

		return meshs

	def setCameraRib( self, arg ):
		import math
		import maya.cmds

		# define filename
		passname = 'camera/camera'
		path     = arg.textfield_pathWorkspace.text()
		filename = '%s/%s.rib' %( path, passname )


		cameraName = 'persp'

		fl  = maya.cmds.getAttr( cameraName + '.focalLength' )
		hfa = maya.cmds.getAttr( cameraName + '.hfa' ) *  25.4

		frameaspectratio = float( arg.intfield_formatX.getValue() ) / float( arg.intfield_formatY.getValue() )

		left   = -1.0
		right  =  1.0
		bottom = -1.0 / frameaspectratio
		top    =  1.0 / frameaspectratio

		fov = math.degrees( 2 * math.atan(hfa / (2 * fl)) )
		tx  = maya.cmds.getAttr( '%s.translateX' %(cameraName) ) * -1
		ty  = maya.cmds.getAttr( '%s.translateY' %(cameraName) ) * -1
		tz  = maya.cmds.getAttr( '%s.translateZ' %(cameraName) ) * -1
		rx  = maya.cmds.getAttr( '%s.rotateX'    %(cameraName) )
		ry  = maya.cmds.getAttr( '%s.rotateY'    %(cameraName) )
		rz  = maya.cmds.getAttr( '%s.rotateZ'    %(cameraName) ) * -1

		# define frame inside content
		content   = '\nProjection "perspective" "fov" [ %s ]' %( fov )
		content  += '\nScreenWindow %s %s %s %s' %( left, right, bottom, top  )
		content  += '\nRotate %s 1 0 0' %( rx )
		content  += '\nRotate %s 0 1 0' %( ry )
		content  += '\nRotate %s 0 0 1' %( rz )
		content  += '\nScale 1 1 -1' 
		content  += '\nTranslate %s %s %s' %( tx, ty, tz )
		content  += '\n'

		# TODO : use matrix for transformation "ConcatTransform [ 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 ]"

		Forge.core.System().setFile( path=filename, content=content, type='w' )

	def setObjectRib( self, arg ):

		# define class
		Fsystem = Forge.core.System()

		path  = arg.textfield_pathWorkspace.text()
		basepath = '%s/object/' %( path )

		# clean up folder
		Fsystem.cleanFolder( path=basepath )


		# export start
		import maya.cmds
		meshs = self.getMayaMesh( arg )

		for mesh in meshs:
			# init var
			filename   = '%s/object/%s.rib' %( path, mesh.replace( ':', '-' ) )
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

	def setShaderRib( self, arg ):
		# define filename
		passname = 'shader/shader'
		path     = arg.textfield_pathWorkspace.text()
		filename = '%s/%s.rib' %( path, passname )

		# define class
		Fsystem = Forge.core.System()

		# define frame inside content
		content   = '\nSurface "F:/software/bcShading_0.0.0.1dev/sdl/BCmonolithic"'


		layout = arg.layout_shaderAttr.children()[0].children()[0].children()[0].children()
		for i in range( len(layout) ):
			if isinstance( layout[i], Anvil.core.Textfield ):
				argtype  = 'string'
				argname  = layout[i-1].text().split(' :')[0]
				argvalue = '"%s"' %( layout[i].getValue() )
				content  += '\n    "%s %s" %s' %( argtype, argname, argvalue )
			elif isinstance( layout[i], Anvil.core.Floatfield ):
				argtype  = 'float'
				argname  = layout[i-1].text().split(' :')[0]
				argvalue = layout[i].getValue()
				content  += '\n    "%s %s" %s' %( argtype, argname, argvalue )
			elif isinstance( layout[i], Anvil.core.Colorpicker ):
				argtype  = 'color'
				argname  = layout[i-1].text().split(' :')[0]
				argvalue = str( layout[i].getValue() ).replace( ',', '')
				content  += '\n    "%s %s" %s' %( argtype, argname, argvalue )

		content  += '\n'

		Fsystem.setFile( path=filename, content=content, type='w' )

	def setLightRib( self, arg ):
		# define filename
		passname = 'light/light'
		path     = arg.textfield_pathWorkspace.text()
		filename = '%s/%s.rib' %( path, passname )

		# define class
		Fsystem = Forge.core.System()

		# define frame inside content
		content   = '\n'
		content  += '\nOption "user" "string environnementMap" "E:/140817_tools/envLight/out/monumentValley/001/test_002.tif"'
		content  += '\nOption "user" "color environnementTint" [1 1 1]'
		content  += '\nOption "user" "color environnementShadowTint" [0 0 0]'
		content  += '\nOption "user" "float environnementRadius" 100'
		content  += '\nOption "user" "float environnementSample" 128'
		content  += '\n'
		content  += '\nAttributeBegin'
		content  += '\n    Translate 0 0 0'
		content  += '\n    Rotate 0 0 1 0'
		content  += '\n    Scale 1 1 1'
		content  += '\n    Translate 10 10 0'
		content  += '\n    LightSource "E:/141031_defaultProject/maya/3delight/rib_scene_001/shaders/OBJ/light.sdl" "lightKey"'
		content  += '\n        "color lightcolor" [0 0 0]'
		content  += '\nAttributeEnd'
		content  += '\n'
		content  += '\nIlluminate "lightKey" 1'
		content  += '\n'

		Fsystem.setFile( path=filename, content=content, type='w' )


