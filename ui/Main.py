
import Forge
import Anvil.core
import Coal

class Main():
	"""docstring for Main"""
	def __init__( self ):

		# define interpreter
		self.interpreter = Forge.core.System().interpreter()

		self.workspacePath = 'F:/test/rnd/scene_001'
		# define ui vars
		self.__boxSize = [ 1900, 100 ]

		# define class
		Awindow = Anvil.core.Window
		Alayout = Anvil.core.Layout

		# window init
		self.window = Awindow( title='Coal', size=[ 1980, 1080 ] )
		self.layout_main = Alayout( parent=self.window, x= 10, y=20 )

		# build ui
		self.workspace()
		self.ribExport()
		self.render()
		self.settings()
		self.shading()

	def workspace( self ):
		# define class
		Abox       = Anvil.core.Box
		Alayout    = Anvil.core.Layout
		Atext      = Anvil.core.Text
		Atextfield = Anvil.core.Textfield
		Abutton    = Anvil.core.Button
		CfnRib     = Coal.core.FnRib()

		# boxs init
		box_workspace = Abox( name='Workspace', w=self.__boxSize[0], h=self.__boxSize[1] )
		layout_main   = Alayout( parent=box_workspace )

		# texts init
		text_pathWorkspace = Atext( text='Path Workspace :' )

		# textfields init
		self.textfield_pathWorkspace = Atextfield( text=self.workspacePath )

		# actions init
		setWorkspace = lambda: CfnRib.structFolders( path=self.textfield_pathWorkspace.text() )

		# buttons init
		button_workspaceExport = Abutton( name='Set', cmd=setWorkspace )

		# define layouts content
		self.layout_main.add( box_workspace )
		layout_main.add( [ text_pathWorkspace, self.textfield_pathWorkspace, button_workspaceExport] )

	def ribExport( self ):
		# define class
		Abox       = Anvil.core.Box
		Alayout    = Anvil.core.Layout
		Atext      = Anvil.core.Text
		Atextfield = Anvil.core.Textfield
		Abutton    = Anvil.core.Button
		CfnRib     = Coal.core.FnRib()

		# boxs init
		box_ribExport = Abox( name='Rib Export', w=self.__boxSize[0], h=self.__boxSize[1] )
		layout_main   = Alayout( parent=box_ribExport )

		# actions init
		setRibWorld = lambda: CfnRib.setRibWorld( self )
		setRibMesh  = lambda: CfnRib.setMeshRib( self )

		# buttons init
		button_ribWorld  = Abutton( name='Export rib World',  cmd=setRibWorld, w=150 )
		button_ribShader = Abutton( name='Export rib Shader', cmd=self.foo,    w=150 )
		if self.interpreter == 'maya':
			button_ribObject = Abutton( name='Export rib Object', cmd=setRibMesh,  w=150 )
			button_ribLight  = Abutton( name='Export rib Light',  cmd=self.foo,    w=150 )
			button_ribCamera = Abutton( name='Export rib Camera', cmd=self.foo,    w=150 )

		# define layouts content
		self.layout_main.add( box_ribExport )
		layout_main.add( [button_ribWorld, button_ribShader] )
		if self.interpreter == 'maya':
			layout_main.add( [button_ribObject, button_ribLight, button_ribCamera] )

	def render( self ):
		# define class
		Abox       = Anvil.core.Box
		Alayout    = Anvil.core.Layout
		Atext      = Anvil.core.Text
		Atextfield = Anvil.core.Textfield
		Abutton    = Anvil.core.Button
		Cactions   = Coal.core.CoalActions()

		# boxs init
		box_render  = Abox( name='Render', w=self.__boxSize[0], h=self.__boxSize[1] )
		layout_main = Alayout( parent=box_render )

		# texts init
		text_pathRender = Atext( text='Path render :' )

		# textfields init
		self.textfield_pathRender = Atextfield( text='' )

		# actions init
		rib = 'lazy'
		if self.interpreter == 'maya' : rib = 'classic'
		renderLocal   = lambda: Cactions.renderLocal( self, rib=rib )
		renderPreview = lambda: Cactions.renderLocal( self, type='preview', rib=rib )

		# buttons init
		button_render        = Abutton( name='Render', cmd=renderLocal, w=150 )
		button_renderPreview = Abutton( name='Render Preview', cmd=renderPreview, w=200 )

		# define layouts content
		self.layout_main.add( box_render )
		layout_main.add( [text_pathRender, self.textfield_pathRender] )
		layout_main.add( [button_render, button_renderPreview] )

	def settings( self ):
		# define class
		Abox        = Anvil.core.Box
		Alayout     = Anvil.core.Layout
		Atext       = Anvil.core.Text
		Atextfield  = Anvil.core.Textfield
		Abutton     = Anvil.core.Button
		Aintfield   = Anvil.core.Intfield
		Afloatfield = Anvil.core.Floatfield
		Adropmenu   = Anvil.core.Dropmenu
		Acheckbox   = Anvil.core.Checkbox
		Cactions    = Coal.core.CoalActions()

		# boxs init
		box_settings  = Abox( name='Settings', w=self.__boxSize[0], h=self.__boxSize[1]*2 )
		layout_main   = Alayout( parent=box_settings )

		# texts init
		text_format       = Atext( text='Format :' )
		text_lockRatio    = Atext( text='Lock aspect ratio :' )
		text_formatMult   = Atext( text='Multiply format by :' )
		text_pixelSample  = Atext( text='Pixel sample :' )
		text_bucketSize   = Atext( text='Bucket size :' )
		text_textureCache = Atext( text='Texture cache :' )
		text_filterType   = Atext( text='Filter Type :' )
		text_filterSize   = Atext( text='Filter size :' )
		text_crop         = Atext( text='Crop :' )

		# ints init
		self.intfield_formatX      = Aintfield( value=1920,      min=1,    max=4096 )
		self.intfield_formatY      = Aintfield( value=1080,      min=1,    max=4096 )
		self.intfield_pixelSample  = Aintfield( value=6,         min=1,    max=16 )
		self.intfield_bucketSize   = Aintfield( value=16,        min=2,    max=256 )
		self.intfield_textureCache = Aintfield( value=1024000,   min=1024, max=65536000 )

		# floats int
		self.floatfield_formatMult = Afloatfield( value=0.25, min=0, max=4 )
		self.floatfield_filterSize = Afloatfield( value=4, min=0, max=32 )
		
		# dropmenus init
		self.dropmenus_filterType = Adropmenu( items=['mitchell', 'box', 'triangle', 'catmull-rom', 'b-spline', 'gaussian', 'sinc', 'bessel'] )

		# checkboxs init
		checkbox_lockRatio = Acheckbox( value=True )
		checkbox_crop      = Acheckbox( value=True )

		# define layouts content
		self.layout_main.add( box_settings )
		layout_main.add( [	text_format, self.intfield_formatX, self.intfield_formatY,
							text_lockRatio, checkbox_lockRatio,
							text_formatMult, self.floatfield_formatMult] )
		layout_main.add( [text_pixelSample, self.intfield_pixelSample] )
		layout_main.add( [	text_bucketSize, self.intfield_bucketSize,
							text_textureCache, self.intfield_textureCache] )
		layout_main.add( [	text_filterType, self.dropmenus_filterType,
							text_filterSize, self.floatfield_filterSize] )
		layout_main.add( [text_crop, checkbox_crop] )

	def shading( self ):
		# define class
		Abox         = Anvil.core.Box
		Alayout      = Anvil.core.Layout
		Abutton      = Anvil.core.Button
		Atextfield   = Anvil.core.Textfield
		Acolorpicker = Anvil.core.Colorpicker
		CfnShader    = Coal.core.FnShader()

		# boxs init
		box_shading            = Abox( name='Shading', w=self.__boxSize[0], h=self.__boxSize[1]*2 )
		self.layout_shaderAttr = Alayout( parent=box_shading )

		# actions init
		lsShader = lambda: self.shadingAttributUI( attrs=CfnShader.queryShader(self) )

		# buttons init
		button_lsShader = Abutton( name='Query', cmd=lsShader )

		# colorpickers init
		colorTest = Acolorpicker( color=[.5, .5, .5] )

		# define layouts content
		self.layout_main.add( box_shading )
		self.layout_shaderAttr.add( [button_lsShader] )
		self.layout_shaderAttr.add( [colorTest] )

	def shadingAttributUI( self, attrs ):
		# define class
		Atext       = Anvil.core.Text
		Atextfield  = Anvil.core.Textfield
		Afloatfield = Anvil.core.Floatfield

		field = Atextfield( text='new' )

		# self.field.deleteLater()

		self.layout_shaderAttr.add( field )
		# from PySide import QtCore, QtGui
		# for i in self.layout_shaderAttr.findChildren( QtGui.QLineEdit ):
		# 	print i.text()

		for attr in attrs : print attr

		# print self.layout_shaderAttr
		# text = Atext( text='sfsf :' )
		# field = Atextfield( text='attr[2]' )
		# self.layout_shaderAttr.add( [text, field] )

		# for attr in attrs:
		# 	if attr[1] == 'string':
		# 		print 'ok'
		# 		text = Atext( text='%s :' %(attr[0]) )
		# 		field = Atextfield( text=attr[2] )
		# 	# if attr[1] == 'float':
		# 	# 	Afloatfield( value=attr[2] )
		# 	# if attr[1] == 'color':
		# 	# 	Atextfield( text=attr[2] 
		# 		self.layout_shaderAttr.add( [text, field] )
		# 		break

	def foo( self ):
		print 'exec'

