import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Dimensiones de la cuadrícula
width, height = 50, 50
prob_spread = 0.4  # Probabilidad de propagación del fuego

# Estados de las celdas
EMPTY = 0      # Sin vegetación
TREE = 1       # Vegetación sana
BURNING = 2    # En llamas
ASH = 3        # Cenizas

# Inicialización de la cuadrícula
def initialize_grid():
    grid = np.random.choice([EMPTY, TREE], size=(height, width), p=[0.2, 0.8])
    # Inicia el fuego en un punto central
    grid[height // 2, width // 2] = BURNING
    return grid

# Función para actualizar la cuadrícula
def update_grid(grid):
    new_grid = grid.copy()
    for y in range(height):
        for x in range(width):
            if grid[y, x] == TREE:
                # Verifica vecinos para propagación del fuego
                neighbors = grid[max(0, y-1):min(height, y+2), max(0, x-1):min(width, x+2)]
                if BURNING in neighbors and np.random.random() < prob_spread:
                    new_grid[y, x] = BURNING
            elif grid[y, x] == BURNING:
                new_grid[y, x] = ASH  # Celda se convierte en cenizas
    return new_grid

# Configuración para la visualización
def animate(i):
    global grid
    im.set_array(grid)
    grid = update_grid(grid)
    return [im]

# Colores para los estados
colors = ['black', 'green', 'red', 'gray']
cmap = plt.cm.colors.ListedColormap(colors)
bounds = [0, 1, 2, 3, 4]
norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)

# Inicialización del gráfico
grid = initialize_grid()
fig, ax = plt.subplots()
im = ax.imshow(grid, cmap=cmap, norm=norm)
ax.axis('off')

# Animación
ani = animation.FuncAnimation(fig, animate, frames=100, interval=1000, blit=True)
plt.show()