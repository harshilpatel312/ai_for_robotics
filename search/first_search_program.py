# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

class Node:
    def __init__(self, x, y, g_cost = 0):
        self.x = x
        self.y = y
        self.g_cost = g_cost

    def __repr__(self):
        return str([self.g_cost, self.x, self.y])

def in_closed_list(closed_list, node):
    ret_val = False

    for item in closed_list:
        if (item.x == node.x and item.y == node.y):
            ret_val = True

    return ret_val

def search(grid, init, goal, cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    open_list = []
    closed_list = []

    open_list.append(Node(init[0], init[1], 0))
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    action_mat = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

    count = 0

    while(1):
        # if open_list is empty, i.e. all nodes on the open_list
        # are explored, then no path found
        if not open_list:
            print('Fail')
            return None

        # find the node with minimum g_cost
        min_g_cost = 1000
        for item in open_list:
            if item.g_cost < min_g_cost:
                min_g_cost = item.g_cost
                node = item

        open_list[:] = [open_list[idx] for idx, tup in enumerate(open_list) if not (tup == node)]
        # for i in range(len(open_list)):
        #     if open_list[i] == node:
        #         del open_list[i]

        closed_list.append(node)

        if (node.x == goal[0] and node.y == goal[1]):
            for i in range(len(expand)):
                print(expand[i])
            print('\n')
            return action_mat

        for idx, action in enumerate(delta):
            neighbour = Node(node.x + action[0], node.y + action[1], node.g_cost + 1)

            # if neighbour outside grid, in collision or
            # already present in closed_list/open_list, then continue
            if (neighbour.x < 0 or neighbour.x > len(grid) - 1 or
                neighbour.y < 0 or neighbour.y > len(grid[0]) - 1 or
                grid[neighbour.x][neighbour.y] == 1 or
                in_closed_list(closed_list, neighbour)):
                continue
            else:
                open_list.append(neighbour)
                action_mat[neighbour.x][neighbour.y] = idx
                if expand[node.x][node.y] == -1:
                    expand[node.x][node.y] = count
                    count += 1

        # for item in open_list:
        #     print([item.x, item.y, item.g_cost])
        # print("\n")

actions = search(grid, init, goal, cost)

if actions:
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    x = goal[0]
    y = goal[1]
    policy[x][y] = '*'
    while x != init[0] or y != init[1]:
        x2 = x - delta[actions[x][y]][0]
        y2 = y - delta[actions[x][y]][1]
        policy[x2][y2] = delta_name[actions[x][y]]
        x = x2
        y = y2

    for i in range(len(policy)):
        print(policy[i])