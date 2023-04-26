import pygame as pg
core = None



class ThatLevelAgain:
	def __init__(self):
		self.window = pg.display.set_mode((100, 100))		

		global core
		import core

		self.window = pg.display.set_mode(core.const.WINDOW_SIZE, pg.FULLSCREEN)
		self.frame  = pg.Surface(core.const.RENDER_SCALE)
		self.clock  = pg.time.Clock()

		pg.display.set_caption(core.const.TITLE)


	def run(self):
		self.start()

		self.running = True
		while self.running:
			self.frame.fill((0, 0, 0))

			for event in pg.event.get():
				match event.type:
					case pg.QUIT:
						self.running = False

			self.update()
			self.render()

			self.window.blit(pg.transform.scale(self.frame, core.const.WINDOW_SIZE), (0, 0))
			pg.display.flip()


	def update(self):
		self.player.update()


	def render(self):
		self.player.render(self.frame)


	def start(self):
		self.player = core.player.Player()



if __name__ == '__main__' :
	pg.mixer.init()
	pg.font.init()
	pg.init()

	ThatLevelAgain().run()

	pg.mixer.quit()
	pg.font.quit()
	pg.quit()