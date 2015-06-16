
import Forge
import Anvil.core
import Coal

class Main():
	"""docstring for Main"""
	def __init__( self ):

		# define interpreter
		self.interpreter = Forge.core.System().interpreter()

		self.workspacePath = 'F:/test/rnd/scene_001'
		self.lightRigPath  = 'F:/test/light/rig_001/light.rib'
		# define ui vars
		self.__boxSize = [ 1860, 100 ]

		# define class
		Awindow = Anvil.core.Window
		Alayout = Anvil.core.Layout

		# window init
		self.window = Awindow( title='Coal', size=[ 1980, 1080 ] )
		self.layout_main = Alayout( parent=self.window, y=10, w=1940, scroll=True )

		# build ui
		self.workspace()
		# self.ribExport()
		self.render()
		self.settings()
		# self.hierarchy()
		# self.light()
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
		box_workspace = Abox( name='Workspace', w=self.__boxSize[0], h=self.__boxSize[1]/1.5 )
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
		Abutton    = Anvil.core.Button
		Cactions   = Coal.core.CoalActions()

		# boxs init
		box_render  = Abox( name='Render', w=self.__boxSize[0], h=self.__boxSize[1] )
		layout_main = Alayout( parent=box_render )

		# actions init
		renderLocal   = lambda: Cactions.renderLocal( self )
		renderPreview = lambda: Cactions.renderLocal( self, type='preview' )

		# buttons init
		button_render        = Abutton( name='Render', cmd=renderLocal, w=250, h=50 )
		button_renderPreview = Abutton( name='Render Preview', cmd=renderPreview, w=250, h=50 )

		# define layouts content
		self.layout_main.add( box_render )
		layout_main.add( [button_render, button_renderPreview] )

	def hierarchy( self ):
		# define class
		Abox       = Anvil.core.Box
		Alayout    = Anvil.core.Layout
		Atree      = Anvil.core.Tree

		# boxs init
		box_render  = Abox( name='Render', w=self.__boxSize[0], h=self.__boxSize[1]*3 )
		layout_main = Alayout( parent=box_render )


		hierarchyList = [
			{ 'name':'object_001', 'id':1, 'iconPath':'F:/dev/BCgit/icons/master.png', 'tooltip':'Information about object', 'iconTooltip':'Information about object icon', 'parentId':None, },
			{ 'name':'object_002', 'id':2, 'iconPath':'F:/dev/BCgit/icons/master.png', 'tooltip':'Information about object', 'iconTooltip':'Information about object icon', 'parentId':None, },
			{ 'name':'object_003', 'id':3, 'iconPath':'F:/dev/BCgit/icons/master.png', 'tooltip':'Information about object', 'iconTooltip':'Information about object icon', 'parentId':None, },
			{ 'name':'object_004', 'id':4, 'iconPath':'F:/dev/BCgit/icons/master.png', 'tooltip':'Information about object', 'iconTooltip':'Information about object icon', 'parentId':None, },
			{ 'name':'object_005', 'id':5, 'iconPath':'F:/dev/BCgit/icons/master.png', 'tooltip':'Information about object', 'iconTooltip':'Information about object icon', 'parentId':None, },
			{ 'name':'object_006', 'id':6, 'iconPath':'F:/dev/BCgit/icons/master.png', 'tooltip':'Information about object', 'iconTooltip':'Information about object icon', 'parentId':None, },
			{ 'name':'object_007', 'id':7, 'iconPath':'F:/dev/BCgit/icons/master.png', 'tooltip':'Information about object', 'iconTooltip':'Information about object icon', 'parentId':1, },
			{ 'name':'object_008', 'id':8, 'iconPath':'F:/dev/BCgit/icons/master.png', 'tooltip':'Information about object', 'iconTooltip':'Information about object icon', 'parentId':7, },
			{ 'name':'object_009', 'id':9, 'iconPath':'F:/dev/BCgit/icons/master.png', 'tooltip':'Information about object', 'iconTooltip':'Information about object icon', 'parentId':8, },
			{ 'name':'object_010', 'id':10, 'iconPath':'F:/dev/BCgit/icons/master.png', 'tooltip':'Information about object', 'iconTooltip':'Information about object icon', 'parentId':8, },
			{ 'name':'object_011', 'id':11, 'iconPath':'F:/dev/BCgit/icons/master.png', 'tooltip':'Information about object', 'iconTooltip':'Information about object icon', 'parentId':7, },
			{ 'name':'object_012', 'id':12, 'iconPath':'F:/dev/BCgit/icons/master.png', 'tooltip':'Information about object', 'iconTooltip':'Information about object icon', 'parentId':2, },
			{ 'name':'object_013', 'id':13, 'iconPath':'F:/dev/BCgit/icons/master.png', 'tooltip':'Information about object', 'iconTooltip':'Information about object icon', 'parentId':2, },
			{ 'name':'object_014', 'id':14, 'iconPath':'F:/dev/BCgit/icons/master.png', 'tooltip':'Information about object', 'iconTooltip':'Information about object icon', 'parentId':16, },
			{ 'name':'object_015', 'id':15, 'iconPath':'F:/dev/BCgit/icons/master.png', 'tooltip':'Information about object', 'iconTooltip':'Information about object icon', 'parentId':16, },
			{ 'name':'light_001', 'id':16, 'iconPath':'F:/dev/BCgit/icons/new.png', 'tooltip':'Information about light', 'iconTooltip':'Information about light icon', 'parentId':None, },
			{ 'name':'light_002', 'id':17, 'iconPath':'F:/dev/BCgit/icons/new.png', 'tooltip':'Information about light', 'iconTooltip':'Information about light icon', 'parentId':None, },
			{ 'name':'camera_001', 'id':18, 'iconPath':'F:/dev/BCgit/icons/edit.png', 'tooltip':'Information about camera', 'iconTooltip':'Information about camera icon', 'parentId':None, },
				]

		# tree init
		tree_hierarchy = Atree()
		tree_hierarchy.add( hierarchyList )

		# define layouts content
		self.layout_main.add( box_render )
		layout_main.add( tree_hierarchy )

	def light( self ):
		# define class
		Abox        = Anvil.core.Box
		Alayout     = Anvil.core.Layout
		Atext       = Anvil.core.Text
		Atextfield  = Anvil.core.Textfield
		Acheckbox   = Anvil.core.Checkbox

		# boxs init
		box_lighting  = Abox( name='Lighting', w=self.__boxSize[0], h=self.__boxSize[1] )
		layout_main   = Alayout( parent=box_lighting )

		# texts init
		text_enableLightRig = Atext( text='Enable light rig :' )
		text_lightRigPath   = Atext( text='Light rig path :' )

		# checkboxs init
		checkbox_enableLightRig = Acheckbox( value=True )

		# textfields init
		self.textfield_pathLightRig = Atextfield( text=self.lightRigPath )

		# define layouts content
		self.layout_main.add( box_lighting )
		layout_main.add( [text_enableLightRig, checkbox_enableLightRig] )
		layout_main.add( [text_lightRigPath, self.textfield_pathLightRig] )

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
		box_settings  = Abox( name='Settings', w=self.__boxSize[0], h=self.__boxSize[1]*3 )
		layout_main   = Alayout( parent=box_settings )

		# texts init
		text_passname         = Atext( text='Pass name :' )
		text_format           = Atext( text='Format :' )
		text_formatMult       = Atext( text='Multiply format by :' )
		text_pixelSample      = Atext( text='Pixel sample :' )
		text_bucketSize       = Atext( text='Bucket size :' )
		text_textureCache     = Atext( text='Texture cache :' )
		text_filterType       = Atext( text='Filter Type :' )
		text_filterSize       = Atext( text='Filter size :' )
		text_indirectDiffuse  = Atext( text='Indirect Diffuse :'   , w=80 )
		text_indirectSpecular = Atext( text='Indirect Specular :'  , w=80 )
		text_lazy             = Atext( text='Lazy :'  , w=35 )
		text_crop             = Atext( text='Crop :'  , w=35 )
		text_cropMinX         = Atext( text='min x :' , w=35 )
		text_cropMaxX         = Atext( text='max x :' , w=35 )
		text_cropMinY         = Atext( text='min y :' , w=35 )
		text_cropMaxY         = Atext( text='max y :' , w=35 )

		# textfields init
		self.textfield_passname = Atextfield( text='beauty' )

		# ints init
		self.intfield_formatX      = Aintfield( value=1920,      min=1,    max=4096 )
		self.intfield_formatY      = Aintfield( value=1080,      min=1,    max=4096 )
		self.intfield_pixelSample  = Aintfield( value=6,         min=1,    max=16 )
		self.intfield_bucketSize   = Aintfield( value=16,        min=2,    max=256 )
		self.intfield_textureCache = Aintfield( value=1024000,   min=1024, max=65536000 )

		# floats int
		self.floatfield_formatMult = Afloatfield( value=0.25, min=0, max=4 )
		self.floatfield_filterSize = Afloatfield( value=4, min=0, max=32 )
		self.floatfield_cropMinX   = Afloatfield( value=0, min=0, max=1 , w=35 )
		self.floatfield_cropMaxX   = Afloatfield( value=1, min=0, max=1 , w=35 )
		self.floatfield_cropMinY   = Afloatfield( value=0, min=0, max=1 , w=35 )
		self.floatfield_cropMaxY   = Afloatfield( value=1, min=0, max=1 , w=35 )
		
		# dropmenus init
		self.dropmenus_filterType = Adropmenu(
			items=[
				{ 'mitchell':'Mitchell' },
				{ 'blackman-harris':'Blackman Harris' },
				{ 'box':'Box' },
				{ 'triangle':'Triangle' },
				{ 'catmull-rom':'Catmull Rom' },
				{ 'b-spline':'b-spline' },
				{ 'gaussian':'Gaussian' },
				{ 'sinc':'sinc' },
				{ 'bessel':'Bessel' },
					]
					)

		# checkboxs init
		self.checkbox_indirectDiffuse  = Acheckbox( value=True )
		self.checkbox_indirectSpecular = Acheckbox( value=True )
		self.checkbox_lazy             = Acheckbox( value=True )
		self.checkbox_crop                  = Acheckbox( value=False )

		# define layouts content
		self.layout_main.add( box_settings )
		layout_main.add( [text_passname, self.textfield_passname] )
		layout_main.add( [	text_format, self.intfield_formatX, self.intfield_formatY,
							text_formatMult, self.floatfield_formatMult] )
		layout_main.add( [text_pixelSample, self.intfield_pixelSample] )
		layout_main.add( [	text_bucketSize, self.intfield_bucketSize,
							text_textureCache, self.intfield_textureCache] )
		layout_main.add( [	text_filterType, self.dropmenus_filterType,
							text_filterSize, self.floatfield_filterSize] )
		layout_main.add( [text_lazy, self.checkbox_lazy] )
		layout_main.add( [text_indirectDiffuse, self.checkbox_indirectDiffuse, text_indirectSpecular, self.checkbox_indirectSpecular] )
		layout_main.add( [	text_crop, self.checkbox_crop,
							text_cropMinX, self.floatfield_cropMinX,
							text_cropMaxX, self.floatfield_cropMaxX,
							text_cropMinY, self.floatfield_cropMinY,
							text_cropMaxY, self.floatfield_cropMaxY
							] )


	def shading( self ):
		# define class
		Abox         = Anvil.core.Box
		Alayout      = Anvil.core.Layout
		Abutton      = Anvil.core.Button
		Atextfield   = Anvil.core.Textfield
		CfnShader    = Coal.core.FnShader()

		# boxs init
		box_shading            = Abox( name='Shading', w=self.__boxSize[0], h=self.__boxSize[1]*6 )
		self.layout_shaderAttr = Alayout( parent=box_shading, scroll=True )

		# actions init
		lsShader = lambda: self.shadingAttributUI( attrs=CfnShader.queryShader(self) )
		test = lambda: self.queryShading()

		# buttons init
		# button_lsShader = Abutton( name='Query', cmd=lsShader )
		button_lsShader = Abutton( name='Query', cmd=test )

		# define layouts content
		self.layout_main.add( box_shading )
		self.layout_shaderAttr.add( [button_lsShader] )
		lsShader()

	def shadingAttributUI( self, attrs ):
		# define class
		Atext        = Anvil.core.Text
		Atextfield   = Anvil.core.Textfield
		Afloatfield  = Anvil.core.Floatfield
		Acolorpicker = Anvil.core.Colorpicker

		# delete old item of the UI
		# for i in self.layout_shaderAttr.children():
		# 	if not 'Button' in str(i):
		# 		i.deleteLater()

		# build UI
		for attr in attrs:
			text = Atext( text='%s :' %(attr[0]), w=200 )

			if attr[1] == 'string':
				field = Atextfield( text=eval( attr[2] ), w=100 )
			elif attr[1] == 'float':
				field = Afloatfield( value=eval( attr[2] ), w=100)
			if attr[1] == 'color':
				tmpColor = eval(attr[2])
				if not isinstance( tmpColor, list ) : tmpColor = [ tmpColor, tmpColor, tmpColor ]
				field = Acolorpicker( color=tmpColor )

			self.layout_shaderAttr.add( [text, field] )

	def queryShading( self ):
		layout = self.layout_shaderAttr.children()[0].children()[0].children()[0].children()
		for i in range( len(layout) ):
			if isinstance( layout[i], Anvil.core.Textfield ):
				print layout[i].getValue()
				print layout[i-1].text()
			elif isinstance( layout[i], Anvil.core.Floatfield ):
				print layout[i].getValue()
				print layout[i-1].text()
			elif isinstance( layout[i], Anvil.core.Colorpicker ):
				print layout[i].getValue()
				print layout[i-1].text()


	def foo( self ):
		print 'exec'

