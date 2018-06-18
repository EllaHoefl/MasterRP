import pyglet	# import libary pyglet by pip 
from pyglet.window import key

mainWindow = pyglet.window.Window(fullscreen=True)


backgroundImage = pyglet.resource.image('Gate.jpg')
dwarfImage = pyglet.resource.image('Dwarf.png')
dwarf = pyglet.sprite.Sprite(dwarfImage)
dwarfImageRight = pyglet.resource.image('Dwarf_right.png')
dwarfRight = pyglet.sprite.Sprite(dwarfImageRight)
dwarfXPosition = 0
dwarfYPosition = 0
dwarfLooksRight = True
dwarfScale = 0.3

@mainWindow.event
def on_key_press(symbol, modifiers):
	global dwarfXPosition
	global dwarfYPosition
	global dwarfLooksRight
	global dwarfScale
	if symbol == key.LEFT:
		print 'The LEFT key was pressed'
		dwarfXPosition = dwarfXPosition - dwarfImage.width//10
		dwarfLooksRight =  False
	elif symbol == key.RIGHT:
		print 'The RIGHT key was pressed'
		dwarfXPosition = dwarfXPosition + dwarfImage.width//10
		dwarfLooksRight = True
	elif symbol == key.UP:
		print 'The UP key was pressed'
		dwarfYPosition = dwarfYPosition + dwarfImage.height//10
		dwarfScale = dwarfScale - 0.05
	elif symbol == key.DOWN:
		print 'The DOWN key was pressed'
		dwarfYPosition = dwarfYPosition - dwarfImage.height//10
		dwarfScale = dwarfScale + 0.05
	else:
		print 'A key was pressed'

@mainWindow.event
def on_draw():
	global dwarfScale
	mainWindow.clear()
	backgroundImage.blit(0,0, width=mainWindow.width, height=mainWindow.height)
	if dwarfLooksRight:
		dwarfRight.set_position(dwarfXPosition, dwarfYPosition)
		dwarfRight.scale = dwarfScale
		dwarfRight.draw()
	else:
		dwarf.set_position(dwarfXPosition, dwarfYPosition)
		dwarf.scale = dwarfScale
		dwarf.draw()
	dwarfScaleLabel = pyglet.text.Label(str(dwarfScale))
	dwarfScaleLabel.draw()

pyglet.app.run()
