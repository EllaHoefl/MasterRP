import pyglet	# import libary pyglet by pip 
from pyglet.window import key

mainWindow = pyglet.window.Window(fullscreen=True)


backgroundImage = pyglet.resource.image('Gate.jpg')
dwarfImage = pyglet.resource.image('Dwarf.png')
dwarf = pyglet.sprite.Sprite(dwarfImage)
dwarfImageRight = pyglet.resource.image('Dwarf_right.png')
dwarfRight = pyglet.sprite.Sprite(dwarfImageRight)
dwarfImageStraight = pyglet.resource.image('Dwarf_straight.png')
dwarfStraight = pyglet.sprite.Sprite(dwarfImageStraight)
dwarfXPosition = 0
dwarfYPosition = 0
dwarfLooksRight = True
dwarfScale = 0.3
dwarfLooksStraight = False
dwarfShrinkPoint = 700

@mainWindow.event
def on_key_press(symbol, modifiers):
	global dwarfXPosition
	global dwarfYPosition
	global dwarfLooksRight
	global dwarfScale
	global dwarfLooksStraight
	if symbol == key.LEFT:
		print 'The LEFT key was pressed'
		dwarfXPosition = dwarfXPosition - dwarfImage.width//10
		dwarfLooksRight =  False
		dwarfLooksStraight = False
	elif symbol == key.RIGHT:
		print 'The RIGHT key was pressed'
		dwarfXPosition = dwarfXPosition + dwarfImage.width//10
		dwarfLooksRight = True
		dwarfLooksStraight = False
	elif symbol == key.UP:
		print 'The UP key was pressed'
		dwarfYPosition = dwarfYPosition + dwarfImage.height//15
	elif symbol == key.DOWN:
		print 'The DOWN key was pressed'
		dwarfYPosition = dwarfYPosition - dwarfImage.height//15
	elif symbol == key.SPACE:
		print 'The SPACE key was pressed'
		dwarfLooksStraight = True
		dwarfLooksRight = False
	else:
		print 'A key was pressed'
	# dwarfYPosition == 0 dann dwarfScale soll 0.3 sein
	# dwarfYPosition == dwarfShrinkPoint dann dwarfScale soll 0 sein
	# Anforderungen:
	# a) ??? ist 1 bei dwarfYPosition = 0
	# b) ??? ist 0 bei dwarfYPosition = dwarfShrinkPoint
	distanceToShrinkPoint = dwarfShrinkPoint - dwarfYPosition
	relativeDistanceToShrinkPoint = distanceToShrinkPoint / float(dwarfShrinkPoint)
	dwarfScale = max(0, relativeDistanceToShrinkPoint * 0.3)


@mainWindow.event
def on_draw():
	mainWindow.clear()
	backgroundImage.blit(0,0, width=mainWindow.width, height=mainWindow.height)
	if dwarfLooksRight:
		dwarfRight.set_position(dwarfXPosition, dwarfYPosition)
		dwarfRight.scale = dwarfScale
		dwarfRight.draw()
	elif dwarfLooksStraight:
		dwarfStraight.set_position(dwarfXPosition, dwarfYPosition)
		dwarfStraight.scale = dwarfScale
		dwarfStraight.draw()
	else:
		dwarf.set_position(dwarfXPosition, dwarfYPosition)
		dwarf.scale = dwarfScale
		dwarf.draw()
	dwarfScaleLabel = pyglet.text.Label(str(dwarfScale))
	dwarfLooksStraightLabel = pyglet.text.Label(str(dwarfLooksStraight), y=50)
	dwarfLooksRightLabel = pyglet.text.Label(str(dwarfLooksRight), y=100)
	dwarfScaleLabel.draw()
	dwarfLooksStraightLabel.draw()
	dwarfLooksRightLabel.draw()


pyglet.app.run()
