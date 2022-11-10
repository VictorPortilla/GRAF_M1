import mesa
from vaccum_agents import *

class VaccumModel(mesa.Model):
    def __init__(self, V, width, height):
        self.num_vacs = V
        self.num_dirt = 1
        self.grid = mesa.space.MultiGrid(width, height, False)
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True
        self.current_id = 0
        self.n_id = 0

        for i in range(self.num_vacs):
            sheep = VaccumAgent(self.next_id(), self)
            self.grid.place_agent(sheep, (1, 1))
            self.schedule.add(sheep)

        # Create wolves
        for i in range(self.num_dirt):
            wolf = DirtAgent(self.next_id(), self)
            self.grid.place_agent(wolf, (2, 2))
            self.schedule.add(wolf)
    
    def step(self):
        self.schedule.step()