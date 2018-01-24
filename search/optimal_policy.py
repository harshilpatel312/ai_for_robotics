grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

goal = [2, 0]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def compute_policy(grid, goal, cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------

    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    change = True
    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):

                if x == goal[0] and y == goal[1]:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        policy[x][y] = '*'
                        change = True

                elif grid[x][y] == 0: # i.e. not an obstacle
                    for idx, action in enumerate(delta):
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
                                policy[x][y] = delta_name[idx]

    return policy

policy = compute_policy(grid, goal, cost)

for i in range(len(policy)):
    print(policy[i])
