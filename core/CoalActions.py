
import Forge
import Coal

class CoalActions( object ):
	"""docstring for CoalActions"""

	def renderLocal( self, arg, type='local' ):

		# define class
		CfnRib = Coal.core.FnRib()

		# get rib path
		ribRoot = arg.textfield_pathWorkspace.text()
		passname = arg.textfield_passname.text()
		ribPath = '%s/%s.rib' %( ribRoot, passname )

		# get options
		lazy = arg.checkbox_lazy.getValue()

		# write rib
		if arg.interpreter == 'maya':
			CfnRib.setCameraRib( arg )
			if not lazy:
				CfnRib.setObjectRib( arg )
			CfnRib.setLightRib( arg )

		CfnRib.setShaderRib( arg )
		CfnRib.setWorldRib( arg )


		# launch render
		self.render( rib=ribPath, type=type )

	@staticmethod
	def render( renderer=Forge.core.Env().renderdl, rib=None, type='local' ):
		if rib:
			ribFrag  = rib.replace( '\\', '/' ).split( '/' )
			file     = ribFrag[-1]
			path     = '/'.join( ribFrag[:-1] )
			flag     = ''

			# preview render
			if type == 'preview' : flag = '-id'

			# define command
			command  = '%s %s %s' %( renderer, flag, file )

			# set env
			Forge.core.System.setEnv( path )

			# launch command
			Forge.core.Process.execShell( command=command )

