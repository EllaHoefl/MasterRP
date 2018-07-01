import pyglet	# import libary pyglet by pip 
from pyglet.window import key

platform = pyglet.window.get_platform()
display = platform.get_default_display()
screens = display.get_screens()
screenid=min(len(screens)-1,1)
mainWindow = pyglet.window.Window(fullscreen=True, screen=screens[screenid])

backgroundImage = pyglet.resource.image('Gate.jpg')
dwarfRight = pyglet.resource.image('Dwarf.png')
dwarfStraight = pyglet.resource.image('Dwarf_straight.png')
dwarfLeft = pyglet.resource.image('Dwarf.png', flip_x=True)
dwarfImage = [dwarfLeft.get_region(x=0, y=0, width=dwarfLeft.width, height=dwarfLeft.height), dwarfStraight , dwarfRight]
dwarf = pyglet.sprite.Sprite(dwarfImage[2])
dwarfPosition = [0,0]
dwarfNewPosition = [0,0]
dwarfDirection=[1,1]
dwarfScale = 0.3
dwarfShrinkPoint = 700
dwarfSpeed = [300,150]

@mainWindow.event
def on_key_press(symbol, modifiers):
	global dwarfPosition
	global dwarfNewPosition
	global dwarfDirection

	if symbol == key.LEFT:
		print 'The LEFT key was pressed'
		if dwarfDirection[0] == -1 and dwarfNewPosition[0] > 0:
			dwarfNewPosition[0] = dwarfNewPosition[0] - dwarfImage[2].width//10
		else:
			dwarfDirection[0] = -1
	elif symbol == key.RIGHT:
		print 'The RIGHT key was pressed'
		if dwarfDirection[0] == 1:
			dwarfNewPosition[0] = dwarfNewPosition[0] + dwarfImage[2].width//10
		else:
			dwarfDirection[0] = 1
	elif symbol == key.UP:
		print 'The UP key was pressed'
		dwarfNewPosition[1] = dwarfNewPosition[1] + dwarfImage[2].height//15
		dwarfDirection[1] = 1
	elif symbol == key.DOWN:
		print 'The DOWN key was pressed'
		dwarfNewPosition[1] = dwarfNewPosition[1] - dwarfImage[2].height//15
		dwarfDirection[1] = -1
	elif symbol == key.SPACE:
		print 'The SPACE key was pressed'
		dwarfDirection[0]=0
	else:
		print 'A key was pressed'


def update(dt):
	global dwarfPosition
	global dwarfNewPosition
	global dwarfDirection
	global dwarfScale

	for i in range(2):
		if dwarfPosition[i] != dwarfNewPosition[i]:
			newPos = dwarfPosition[i] + dwarfSpeed[i] * dt * dwarfDirection[i]
			if newPos * dwarfDirection[i] < dwarfNewPosition[i] * dwarfDirection[i]:
				dwarfPosition[i] = newPos
			else:
				dwarfPosition[i] = dwarfNewPosition[i]

	# dwarfPosition[1] == 0 dann dwarfScale soll 0.3 sein
	# dwarfPosition[1] == dwarfShrinkPoint dann dwarfScale soll 0 sein
	# Anforderungen:
	# a) ??? ist 1 bei dwarfPosition[1] = 0
	# b) ??? ist 0 bei dwarfPosition[1] = dwarfShrinkPoint
	distanceToShrinkPoint = dwarfShrinkPoint - dwarfPosition[1]
	relativeDistanceToShrinkPoint = distanceToShrinkPoint / float(dwarfShrinkPoint)
	dwarfScale = max(0, relativeDistanceToShrinkPoint * 0.3)

pyglet.clock.schedule_interval(update, 1/60.)

@mainWindow.event
def on_draw():
	mainWindow.clear()
	backgroundImage.blit(0,0, width=mainWindow.width, height=mainWindow.height)
	dwarf.position=dwarfPosition
	dwarf.scale = dwarfScale
	dwarf.image=dwarfImage[dwarfDirection[0]+1]
	dwarf.draw()

	dwarfScaleLabel = pyglet.text.Label(str(dwarfScale))
	dwarfDirectionLabel = pyglet.text.Label(str(dwarfDirection[0]), y=50)
	dwarfScaleLabel.draw()
	dwarfDirectionLabel.draw()

pyglet.app.run()