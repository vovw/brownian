import math
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# setup vars 
ARENA = 5
INITIAL_X = ARENA / 2
INITIAL_Y = ARENA / 2
INITIAL_DIRECTION = 0  

# robot's step size and rotation range
STEP_SIZE = 0.1
ROTATION_RANGE = (0, 2 * math.pi)

class BrownianMotion:
    def __init__(self):
        self.x = INITIAL_X
        self.y = INITIAL_Y
        self.direction = INITIAL_DIRECTION

    def move(self):
        dx = STEP_SIZE * math.cos(self.direction)
        dy = STEP_SIZE * math.sin(self.direction)
        new_x = self.x + dx
        new_y = self.y + dy

        # collision detection
        if not (0 <= new_x <= ARENA and 0 <= new_y <= ARENA):
            # Rotate the robot by a angle
            self.direction = random.uniform(*ROTATION_RANGE)
        else:
            self.x = new_x
            self.y = new_y

    def simulate(self, num_steps):
        positions = []
        for _ in range(num_steps):
            positions.append((self.x, self.y))
            self.move()
        return np.array(positions)

# display the simulation
def vis_sim(positions):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(0, ARENA)
    ax.set_ylim(0, ARENA)
    line, = ax.plot([], [], 'r-', lw=2)
    def animate(i):
        x, y = positions[i]
        line.set_data(positions[:i+1, 0], positions[:i+1, 1])
        return line,
    ani = animation.FuncAnimation(fig, animate, frames=len(positions), interval=50, blit=True)
    plt.show()
