import mesa

class VaccumAgent(mesa.Agent):
    """An agent representing. """

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.cleaning = False

    def move(self):
        if self.cleaning:
            self.cleaning = False
        else:
            possible_steps = self.model.grid.get_neighborhood(
                self.pos, moore=True, include_center=False
            )
            new_position = self.random.choice(possible_steps)
            self.model.grid.move_agent(self, new_position)

    def clean(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        dirtList = [obj for obj in cellmates if isinstance(obj, DirtAgent)]
        isDirty = len(dirtList) > 0
        if(isDirty):
            self.cleaning = True
            dirtList[0].clean()

    def step(self):
        self.move()
        self.clean()
        
class DirtAgent(mesa.Agent):
    """An agent representing. """

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.cleaning = False

    def clean(self):
        self.model.grid.remove_agent(self)
        self.model.schedule.remove(self)

    def step(self):
        return

