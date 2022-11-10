import mesa
from vaccum_model import *
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
Path("/images").mkdir(parents=True, exist_ok=True)
Path("/images/dirtyTiles").mkdir(parents=True, exist_ok=True)
Path("/images/heatmaps").mkdir(parents=True, exist_ok=True)

n_vaccums = 10
n_dirty_tiles = 10
n_steps = 100
n_episodes = 50
width = 10
height = 10

params = {"V": n_vaccums, "width": width, "height": height, "D":n_dirty_tiles}

df1 = pd.DataFrame()
df2 = pd.DataFrame()
for i in range(n_episodes):
    results = mesa.batch_run(
        VaccumModel,
        parameters=params,
        iterations=1,
        max_steps=n_steps,
        number_processes=1,
        data_collection_period=1,
        display_progress=False
    )
    
    temp_df = pd.DataFrame(results)
    
    dirtyTiles = temp_df[["DirtyTiles"]]
    dirtyTiles.rename({'DirtyTiles':('DirtyTiles' + str(i))})
    df1 = pd.concat([df1, dirtyTiles], axis=1)

    positions = temp_df[["matrix"]]
    df2 = pd.concat([df2, positions])

fig, ax = plt.subplots()

matrixMean = df2['matrix'].mean()
heatmap = ax.imshow(matrixMean, interpolation='nearest', origin='lower')
plt.colorbar(heatmap)
plt.xlabel('Eje X')
plt.ylabel('EjeY')
plt.savefig('images/heatmaps/' + str(n_vaccums) +'_vaccums_imshow.png')
plt.show()

df1.plot(xlabel='Steps', ylabel='Dirt tiles', legend=False)

mean = df1.mean(axis=1)
mean.plot(label='Promedio', legend=True)
plt.savefig('images/dirtyTiles/' + str(n_vaccums) +'_vaccums.png')
plt.show()