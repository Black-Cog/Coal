
import os
import Forge
import Coal

class CoalActions( object ):
	"""docstring for CoalActions"""

	def renderLocal( self, arg, type='local', rib='classic' ):

		# define class
		CfnRib = Coal.core.FnRib()

		# get rib path
		ribRoot = arg.textfield_pathWorkspace.text()
		ribPath = '%s/beauty.rib' %( ribRoot )

		# write rib
		CfnRib.setCameraRib( arg )
		CfnRib.setObjectRib( arg )
		CfnRib.setShaderRib( arg )
		CfnRib.setLightRib( arg )
		CfnRib.setWorldRib( arg )
		# if rib == 'classic':
		# 	CfnRib.setMeshRib( arg )
		# 	CfnRib.setWorldRib( arg )
		# 	print 'ok'
		# elif rib == 'lazy':
		# 	CfnRib.setWorldRib( arg )
		# elif rib == 'full':
		# 	CfnRib.setMeshRib( arg )
		# 	CfnRib.setWorldRib( arg )

		# launch render
		self.render( rib=ribPath, type=type )

	@staticmethod
	def render( renderer='C:/Program Files/3Delight/bin/renderdl.exe', rib=None, type='local' ):
		if rib:
			ribFrag  = rib.replace( '\\', '/' ).split( '/' )
			file     = ribFrag[-1]
			path     = '/'.join( ribFrag[:-1] )
			flag     = ''

			# preview render
			if type == 'preview' : flag = '-id'

			# define command
			command  = '%s %s %s' %( renderer, flag, file )

			# define class
			Fprocess = Forge.core.Process()

			# set env
			os.chdir( path )

			# launch command
			Fprocess.launch( command=command )

