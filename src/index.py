import pyglet	# import libary pyglet by pip 
from pyglet.window import key

mainWindow = pyglet.window.Window(fullscreen=True)


backgroundImage = pyglet.resource.image('Gate.jpg')
dwarfImage = pyglet.resource.image('Dwarf.png')
dwarfImageRight = pyglet.resource.image('Dwarf.png', flip_x=True)
dwarfXPosition = 0
dwarfYPosition = 0
dwarfLooksRight = True
inverseDwarfScale = 2

@mainWindow.event
def on_key_press(symbol, modifiers):
	global dwarfXPosition
	global dwarfYPosition
	global dwarfLooksRight
	global inverseDwarfScale
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
		inverseDwarfScale = inverseDwarfScale + 0.15
	elif symbol == key.DOWN:
		print 'The DOWN key was pressed'
		dwarfYPosition = dwarfYPosition - dwarfImage.height//10
		inverseDwarfScale = inverseDwarfScale - 0.15


	else: 
		print 'A key was pressed'

@mainWindow.event
def on_draw():
	mainWindow.clear()
	backgroundImage.blit(0,0, width=mainWindow.width, height=mainWindow.height)
	if dwarfLooksRight:
		dwarfImageRight.blit(dwarfImage.width + dwarfXPosition,
			dwarfYPosition, 
			width=dwarfImage.width//(inverseDwarfScale*inverseDwarfScale), 
			height=dwarfImage.height//(inverseDwarfScale*inverseDwarfScale))
	else:
		dwarfImage.blit(dwarfXPosition,
			dwarfYPosition, 
			width=dwarfImage.width//(inverseDwarfScale*inverseDwarfScale), 
			height=dwarfImage.height//(inverseDwarfScale*inverseDwarfScale))
	dwarfScaleLabel = pyglet.text.Label(str(inverseDwarfScale))
	dwarfScaleLabel.draw()

pyglet.app.run()
