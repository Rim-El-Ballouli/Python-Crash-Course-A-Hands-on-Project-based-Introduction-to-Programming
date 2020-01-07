import matplotlib.pyplot as plt
from random import choice


def get_step():
    direction = choice([1, -1])
    distance = choice([0, 1, 2, 3, 4])
    step = direction * distance
    return step

class RandomWalk():
    """A class to generate random walks."""
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction.

            x_step = get_step()
            y_step = get_step()
            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue
            # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)


while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, lineWidth=1)

    # Remove the axes.
    plt.axis('off')

    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6))

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break