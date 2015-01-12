
import Anvil.core
import Coal

class Main():
	"""docstring for Main"""
	def __init__( self ):

		self.ribPath = 'E:/141031_defaultProject/maya/3delight/rib_scene_001/rib/rib_python2.rib'

		# define ui vars
		self.__boxSize = [ 1900, 100 ]

		# define class
		Awindow    = Anvil.core.Window
		Alayout    = Anvil.core.Layout

		# window init
		self.window = Awindow( title='Coal', size=[ 1980, 1080 ] )
		self.layout_main = Alayout( parent=self.window, x= 10, y=20 )

		# build ui
		self.ribExport()
		self.ribRender()
		self.render()


	def ribExport( self ):
		# define class
		Abox       = Anvil.core.Box
		Alayout    = Anvil.core.Layout
		Atext      = Anvil.core.Text
		Atextfield = Anvil.core.Textfield
		Abutton    = Anvil.core.Button

		# boxs init
		box_ribExport = Abox( name='Rib Export', w=self.__boxSize[0], h=self.__boxSize[1] )
		layout_main   = Alayout( parent=box_ribExport )

		# texts init
		text_pathRib = Atext( text='Path rib :' )

		# textfields init
		self.textfield_pathRib = Atextfield( text=self.ribPath )

		# buttons init
		button_ribExport = Abutton( name='Export', cmd=self.foo)

		# definf layouts content
		self.layout_main.add( box_ribExport )
		layout_main.add( [ text_pathRib, self.textfield_pathRib ] )
		layout_main.add( button_ribExport )


	def ribRender( self ):
		# define class
		Abox       = Anvil.core.Box
		Alayout    = Anvil.core.Layout
		Atext      = Anvil.core.Text
		Atextfield = Anvil.core.Textfield
		Abutton    = Anvil.core.Button

		Cactions   = Coal.core.CoalActions()

		# boxs init
		box_renderRib = Abox( name='Render Rib', w=self.__boxSize[0], h=self.__boxSize[1] )
		layout_main   = Alayout( parent=box_renderRib )

		# texts init
		text_pathRender = Atext( text='Path render :' )

		# textfields init
		self.textfield_pathRender = Atextfield( text='' )

		# buttons init
		button_ribRender        = Abutton( name='Render Rib', cmd=Cactions.render, w=150 )
		button_ribRenderPreview = Abutton( name='Render Rib Preview', cmd=Cactions.renderPreview, w=200 )

		# definf layouts content
		self.layout_main.add( box_renderRib )
		layout_main.add( [text_pathRender, self.textfield_pathRender] )
		layout_main.add( [button_ribRender, button_ribRenderPreview] )

	def render( self ):
		# define class
		Abox    = Anvil.core.Box
		Alayout = Anvil.core.Layout
		Abutton = Anvil.core.Button

		Cactions   = Coal.core.CoalActions()

		# boxs init
		box_render    = Abox( name='Render',     w=self.__boxSize[0], h=self.__boxSize[1] )
		layout_main   = Alayout( parent=box_render )

		# buttons init
		button_render        = Abutton( name='Render', cmd=Cactions.render, w=150 )
		button_renderPreview = Abutton( name='Render Preview', cmd=Cactions.renderPreview, w=200 )

		# definf layouts content
		self.layout_main.add( box_render )
		layout_main.add( [button_render, button_renderPreview] )


	def foo( self ):
		print 'exec'