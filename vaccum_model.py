import mesa
from vaccum_agents import *
import numpy as np

def agentTypeInGrid(model):
    agent_counts = np.zeros((model.grid.width, model.grid.height))
    for cell in model.grid.coord_iter():
        cell_content, x, y = cell
        agent_count = sum(isinstance(agent, VaccumAgent) for agent in cell_content)
        agent_counts[x][y] = agent_count
    return agent_counts

class VaccumModel(mesa.Model):
    def __init__(self, V, D, width, height):
        self.num_vacs = V
        self.num_dirt = D
        self.grid = mesa.space.MultiGrid(width, height, False)
        self.schedule = mesa.time.RandomActivationByType(self)
        self.running = True
        self.current_id = 0
        self.current_it = 0
        self.datacollector = mesa.DataCollector(
            {
                "DirtyTiles": lambda m: m.schedule.get_type_count(DirtAgent),
                "matrix": lambda m: agentTypeInGrid(m)
            }
        )
        self.currentPositions = mesa.DataCollector(
            {
                
            }
        )

        for i in range(self.num_vacs):
            v = VaccumAgent(self.next_id(), self)
            self.schedule.add(v)
            self.grid.place_agent(v, (1,1))

        for i in range(self.num_dirt):
            d = DirtAgent(self.next_id(), self)
            self.schedule.add(d)
            self.grid.place_agent(d, (self.random.randrange(self.grid.height), self.random.randrange(self.grid.height)))

        self.datacollector.collect(self)

    def step(self):
        if self.current_it > 110:
            self.running = False
            self.current_it = 0
        else:
            self.schedule.step()
            self.datacollector.collect(self)
            self.current_it += 1