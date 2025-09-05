import tkinter as tk

# coded by Zenet

class Dijkstras:
    def __init__(self, root):
        self.root = root

        self.root_height = self.root_width = 660
        self.root.geometry(f"{self.root_height}x{self.root_width}")
        self.root.title("Maze")

        self.columns = 33
        self.rows = 33

        self.pixel_p_cell = self.root_height / self.columns

        self.grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



        ]

        self.directions = {
            "Left" : (-1, 0),
            "Right" : (1, 0),
            "Up" : (0, -1),
            "Down" : (0, 1)

        }

        self.canvas = tk.Canvas(self.root, height=f"{self.root_height}", width=f"{self.root_width}", bg="white" )
        self.canvas.pack()

        self.queue = []

        self.distance = []

        self.visited = []

        self.shortest_path = {}

        for y in range(0, self.rows):
            for x in range(0, self.columns):
                if self.grid[y][x] == 1:
                    self.distance.append([(y, x), float('inf')])

        # initialise all nodes as having 'infinity' edge cost


    def dijkstras_shortest_path(self):
        # start and end POS are hardcoded but can be randomly chosen too
        start_y, start_x = 15, 15
        end_y, end_x = 1, 31,

        self.queue.append( ( 0, (start_y, start_x) ) )
        self.visited.append((start_y, start_x))

        self.distance.remove([(start_y, start_x), float('inf')])
        self.distance.append([(start_y, start_x), 0])
        # update the start node's distance to 0 (as this is the starting node)
        # to get to the start node from the start node is 0


        while self.queue:

            distance, (y, x) = self.queue.pop(self.queue.index(min(self.queue)))
            # pop the node with the smallest weight

            smallest_node = [(y, x), distance]

            self.visited.append((smallest_node[0]))
            # mark it as visited
            
            current_distance = smallest_node[1]
            # get the current distance of the chosen node

            if smallest_node[0] == (end_y, end_x):
                # if this node is the end node: end the loop -> else continue
                break

            for y, x in self.directions.values():
                ne_y, ne_x = smallest_node[0][0] + y, smallest_node[0][1] + x

                if 0 <= ne_y < self.rows and 0 <= ne_x < self.columns and (ne_y, ne_x) not in self.visited and self.grid[ne_y][ne_x] == 1:
                    # check all valid neighbours of the node
                    new_distance = current_distance + 1
                    # increment the current distance by 1

                    check_distance = None

                    for value in self.distance:
                        if value[0] == (ne_y, ne_x):
                            check_distance = value[1]
                    # update the neighbours distance 

                    if new_distance < check_distance:
                        for value in self.distance:
                            if value[0] == (ne_y, ne_x):
                                value[1] = new_distance
                    # if we find a node with a shorter distance from the current node: update the distance

                    self.shortest_path[(ne_y, ne_x)] = (smallest_node[0][0], smallest_node[0][1])

                    self.queue.append((new_distance, (ne_y, ne_x)))
                    # add the neighbour to the queue

        path = []
        node = (end_y, end_x)
        if node in self.shortest_path:
            while node != (start_y, start_x):
                path.append(node)
                node = self.shortest_path[node]
                y, x = node
                self.grid[y][x] = 7
                # mark the path to goal as a 7: this will be useful in the draw_grid method
            path.append((start_y, start_x))
            path.reverse()
        # reconstruct path
        
        print("path")
        print(path)


    def draw_grid(self):
        for y in range(self.rows):
            for x in range(self.columns):
                colour = "black" if self.grid[y][x] == 0 else "white"
                if self.grid[y][x] == 7:
                    colour = "green"
                # if the path is a 7, then make it green to show the path

                self.canvas.create_rectangle(x * self.pixel_p_cell, y * self.pixel_p_cell,

                x * self.pixel_p_cell + self.pixel_p_cell , y * self.pixel_p_cell + self.pixel_p_cell,
                fill=colour, outline="")

                if y == 15 and x == 15:
                    self.canvas.create_rectangle(x * self.pixel_p_cell, y * self.pixel_p_cell,

                                                 x * self.pixel_p_cell + self.pixel_p_cell,
                                                 y * self.pixel_p_cell + self.pixel_p_cell,
                                                 fill="red", outline="")
                if y == 1 and x == 31:
                    self.canvas.create_rectangle(x * self.pixel_p_cell, y * self.pixel_p_cell,

                                                 x * self.pixel_p_cell + self.pixel_p_cell,
                                                 y * self.pixel_p_cell + self.pixel_p_cell,
                                                 fill="blue", outline="")
                # mark the start and end POS as different colours

if __name__ == "__main__":
    root = tk.Tk()
    run_maze = Dijkstras(root)
    run_maze.dijkstras_shortest_path()
    run_maze.draw_grid()
    root.mainloop()


