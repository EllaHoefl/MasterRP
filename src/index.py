import pyglet	# import libary pyglet by pip 

window = pyglet.window.Window(fullscreen=True)


image = pyglet.resource.image('Gate.jpg')

@window.event
def on_draw():
	window.clear()
	image.blit(0,0, width=window.width, height=window.height)

pyglet.app.run()
