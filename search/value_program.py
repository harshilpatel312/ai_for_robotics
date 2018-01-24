# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0]]

goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def compute_value(grid, goal, cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------

    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]

    change = True
    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):

                if x == goal[0] and y == goal[1]:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        change = True

                elif grid[x][y] == 0: # i.e. not an obstacle
                    for action in delta:
                        neighbour_x = x + action[0]
                        neighbour_y = y + action[1]

                        # find value function of neighbours that are inside the grid and not obstacles
                        if not (neighbour_x < 0 or neighbour_x > len(grid) - 1 or
                                neighbour_y < 0 or neighbour_y > len(grid[0]) - 1 or
                                grid[neighbour_x][neighbour_y] == 1):

                            v2 = value[neighbour_x][neighbour_y] + cost

                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2

    for i in range(len(value)):
        print(value[i])

compute_value(grid, goal, cost)