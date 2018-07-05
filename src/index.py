import pyglet	# import libary pyglet by pip 
from pyglet.window import key
import math

platform = pyglet.window.get_platform()
display = platform.get_default_display()
screens = display.get_screens()
screenid=min(len(screens)-1,1)
mainWindow = pyglet.window.Window(fullscreen=True, screen=screens[screenid])
keys = key.KeyStateHandler()
mainWindow.push_handlers(keys)

backgroundImage = pyglet.resource.image('Gate.jpg')
dwarfRight = pyglet.resource.image('Dwarf.png')
dwarfStraight = pyglet.resource.image('Dwarf_straight.png')
dwarfLeft = pyglet.resource.image('Dwarf.png', flip_x=True)
dwarfImage = [dwarfLeft.get_region(x=0, y=0, width=dwarfLeft.width, height=dwarfLeft.height), dwarfStraight , dwarfRight] 

shrinkPoint = mainWindow.height * 0.65
slots=6
time = 0

class Puppet:
	direction=[1,1]
	speed=[300,150]
	newPosition=[0,0]
	stepSize=[mainWindow.width//slots,mainWindow.height//15]

	def __init__(self):
		self.sprite=pyglet.sprite.Sprite(dwarfImage[2])
		self.sprite.scale=(self.stepSize[0]) / float(dwarfImage[2].width)
		self.baseScale=self.sprite.scale

	def changePosition(self, axis, direction):
		self.newPosition[axis] += direction*self.stepSize[axis]	

	def changeDirection(self, axis, direction):
		self.direction[axis]=direction
		if axis == 0:
			self.sprite.image=dwarfImage[self.direction[0]+1]


	def move(self, dt, time):
		pos = list(self.sprite.position)

		key_pressed=[False, False]
		if(self.direction[0]==-1):
			key_pressed[0]=keys[key.LEFT]
		elif(self.direction[0]==1):
			key_pressed[0]=keys[key.RIGHT]
		if(self.direction[1]==-1):
			key_pressed[1]=keys[key.UP]
		elif(self.direction[1]==1):
			key_pressed[1]=keys[key.DOWN]

		continue_bounce=True

		for i in range(2):
			if pos[i] != self.newPosition[i]:
				pos[i] += self.speed[i] * dt * self.direction[i]
				if pos[i] * self.direction[i] < self.newPosition[i] * self.direction[i]:
					self.sprite.scale_y = 1 + 0.04 * math.sin(time * 10)
				elif key_pressed[i]:
					self.changePosition(i,self.direction[i])
				else:
					pos[i] = self.newPosition[i]

				if i==1:
					self.sprite.scale = max(0, self.baseScale * (1 - pos[1]/shrinkPoint))
				continue_bounce = False
		self.sprite.position = pos

		if(self.sprite.scale_y != 1 and continue_bounce):
			before = self.sprite.scale_y
			self.sprite.scale_y = 1 + 0.04 * math.sin(time * 10)
			if (before - 1) * (self.sprite.scale_y - 1) <= 0 :
				self.sprite.scale_y = 1

puppet=Puppet()


def on_key_press(symbol, modifiers):

	global puppet

	if symbol == key.LEFT:
		if puppet.direction[0] == -1:
			puppet.changePosition(0,-1)
		else:
			puppet.changeDirection(0,-1)

	elif symbol == key.RIGHT:
		if puppet.direction[0] == 1:
			puppet.changePosition(0,1)
		else:
			puppet.changeDirection(0,1)

	elif symbol == key.UP:
		puppet.changePosition(1,1)
		puppet.changeDirection(1,1)

	elif symbol == key.DOWN:
		puppet.changePosition(1,-1)
		puppet.changeDirection(1,-1)

	elif symbol == key.SPACE:
		puppet.changeDirection(0,0)

mainWindow.push_handlers(on_key_press)


def update(dt):
	global time
	global puppet

	time += dt
	puppet.move(dt,time)


pyglet.clock.schedule_interval(update, 1/60.)


@mainWindow.event
def on_draw():
	mainWindow.clear()
	backgroundImage.blit(0,0, width=mainWindow.width, height=mainWindow.height)

	puppet.sprite.draw()

	dwarfScaleLabel = pyglet.text.Label(str(puppet.baseScale))
	dwarfDirectionLabel = pyglet.text.Label(str(puppet.sprite.scale_y), y=50)
	dwarfScaleLabel.draw()
	dwarfDirectionLabel.draw()

pyglet.app.run()