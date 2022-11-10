import mesa
from vaccum_model import *
def agent_portrayal(agent):
    portrayal = {
        "Shape":"circle",
        "Filled":"true",
        "r":0.4
    }

    if isinstance(agent, DirtAgent):
        portrayal["r"] = 0.6
        portrayal["Color"] = "brown"
        portrayal["Layer"] = 0
    else:
        portrayal["r"] = 0.4
        portrayal["Color"] = "red"
        portrayal["Layer"] = 1

    return portrayal

grid = mesa.visualization.CanvasGrid(agent_portrayal, 10, 10, 500, 500)
chart = mesa.visualization.ChartModule([{"Label": "DirtyTiles",
                      "Color": "Black"}],
                    data_collector_name='datacollector')
server = mesa.visualization.ModularServer(
    VaccumModel, [grid, chart], "Vaccum Model", {"V": 3, "width": 10, "height": 10, "D":10}
)
server.port = 8521  # The default
server.launch()