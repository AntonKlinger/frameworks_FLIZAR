import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms

import numpy as np
import math

import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import numpy as np
import math

class Plot:
    def __init__(self, bearings, save_path):
        self.save_path = save_path
        self.bearings = bearings
        self.nodes = []
        self.connections = []
        self.forces = []
        self.bars = []
        self.forces_none = []
        self.nodes_none = []

    def plot(self):
        fig1 = plt.figure(figsize=(8, 8))
        x_values = [knoten.x for knoten in self.nodes]
        y_values = [knoten.y for knoten in self.nodes]

        plt.scatter(x_values, y_values, label="Knotenpunkte", color='white', s=50)
        plt.xlabel("X-Koordinate")
        plt.ylabel("Y-Koordinate")
        plt.xlim(-5, 5)
        plt.ylim(0, 10)
        plt.gca().set_facecolor('none')

        plt.gca().spines['top'].set_color('white')
        plt.gca().spines['right'].set_color('white')
        plt.gca().spines['left'].set_color('white')
        plt.gca().spines['bottom'].set_color('white')
        plt.gca().xaxis.label.set_color('none')
        plt.gca().yaxis.label.set_color('none')
        plt.gca().set_xticks(np.arange(-5, 5, 1))
        plt.gca().set_yticks(np.arange(0, 10, 1))
        plt.gca().grid(which='both', color='white', linewidth=0.5)
        plt.gca().tick_params(axis='both', colors='none')

        for source, target in self.connections:
            source_x, source_y = source.x, source.y
            target_x, target_y = target.x, target.y
            plt.plot([source_x, target_x], [source_y, target_y], color='white', linewidth='3')

        for knoten in self.nodes:
            plt.annotate(knoten.name, (knoten.x + 0.2, knoten.y), textcoords="offset points", xytext=(0, 10), ha='center', color='#1E90FF', fontsize=12)            #if knoten.name == 'A':

        for balken in self.bars:
            plt.fill(balken.x, balken.y, color='white')

        if self.bearings == True:
            for knoten in self.nodes:
                if knoten.name == 'A':
                    x = knoten.x - 0.5
                    y = knoten.y - 0.6
                    break

            festlager_img1 = mpimg.imread('frameworks/public/festlager.png')

            festlager_img_rotated1 = np.rot90(festlager_img1, k=0)

            plt.imshow(festlager_img_rotated1, extent=[x, x + 1, y, y + 1])

            for knoten in self.nodes:
                if knoten.name == 'B':
                    x = knoten.x - 0.5
                    y = knoten.y - 0.7
                    break

            festlager_img1 = mpimg.imread('frameworks/public/loslager.png')

            festlager_img_rotated1 = np.rot90(festlager_img1, k=0)

            plt.imshow(festlager_img_rotated1, extent=[x, x + 1, y, y + 1])

        for force in self.forces:
            plt.quiver(force.x1, force.y1, force.x2, force.y2, angles='xy', scale_units='xy', scale=1, color='r', label='Vektor', zorder=4)

        save_path = 'frameworks/task/' + self.save_path
        fig1.savefig(save_path, bbox_inches=mtransforms.Bbox([[0, 0], [1, 1]]).transformed(fig1.transFigure - fig1.dpi_scale_trans), transparent=True)
  
    def add_knoten(self, x, y, name):
        knoten = Knoten(x, y, name)
        self.nodes.append(knoten)

    def add_connection(self, source_name, target_name):
        source_node = next((node for node in self.nodes if node.name == source_name), None)
        if source_node is None:
            source_node = next((node for node in self.nodes_none if node.name == source_name), None)

        target_node = next((node for node in self.nodes if node.name == target_name), None)
        if target_node is None:
            target_node = next((node for node in self.nodes_none if node.name == target_name), None)

        if source_node is not None and target_node is not None:
            self.connections.append((source_node, target_node))

    def add_force(self, x1, y1, x2, y2, name):
        force = Kraft(x1, y1, x2, y2, name)
        self.forces.append(force)

    def add_balken(self, x1, y1, x2, y2):
        balken = Balken(x1, y1, x2, y2)
        self.bars.append(balken)
        print(balken)

    def add_force_none(self, x1, y1, x2, y2, name):
        force = Kraft(x1, y1, x2, y2, name)
        self.forces_none.append(force) 

    def add_node_none(self, x, y, name):
        knoten = Knoten(x, y, name)
        self.nodes_none.append(knoten)
             
    def get_knoten(self):
        node_info = []
        for knoten in self.nodes:
            node_info.append({
                'name': knoten.name,
                'x': knoten.x,
                'y': knoten.y
            })
        return node_info
    
    def get_node_none(self):
        node_none_info = []
        for knoten in self.nodes_none:
            node_none_info.append({
                'name': knoten.name,
                'x': knoten.x,
                'y': knoten.y
            })
        return node_none_info
    
    def get_knoten_name(self, name):
        knoten_with_name = next((knoten for knoten in self.nodes if knoten.name == name), None)
        
        return knoten_with_name
    
    def get_node_none_name(self, name):
        knoten_with_name = next((knoten for knoten in self.nodes_none if knoten.name == name), None)
        
        return knoten_with_name
    
    def get_connections(self):
        connections_list = [(source.name, target.name) for source, target in self.connections]
        return connections_list
    
    def get_force(self, name):
        for force in self.forces:
            if force.name == name:
                return force
        return None
    
    def get_force_by_point(self, point):
        for force in self.forces:
            if force.name.startswith(point):
                return force
    
    def get_force_none(self, name):
        for force in self.forces_none:
            if force.name == name:
                return force
    
    def get_force_none_by_point(self, point):
        for force in self.forces_none:
            if force.name.startswith(point):
                return force
   
    def set_bearings(self, bool):
        self.bearings = bool

    def set_save_path(self, name):
        self.save_path = name

    def norm_connection(self, start, end):
        start_node = next((node for node in self.nodes if node.name == start), None)
        end_node = next((node for node in self.nodes_none if node.name == end), None)

        if start_node is not None and end_node is not None:
            direction_x = end_node.x - start_node.x
            direction_y = end_node.y - start_node.y

            direction_length = math.sqrt(direction_x**2 + direction_y**2)

            new_end_x = start_node.x + direction_x / direction_length
            new_end_y = start_node.y + direction_y / direction_length

            end_node.x = new_end_x
            end_node.y = new_end_y

class Kraft:
    def __init__(self, x1, y1, x2, y2, name):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.name = name
        direction_x = x2 - x1
        direction_y = y2 - y1
        self.lenght = math.sqrt((direction_x)**2 + (direction_y)**2)
        direction_length = math.sqrt(direction_x**2 + direction_y**2)

        self.x3 = x1 + direction_x / direction_length
        self.y3 = y1 + direction_y / direction_length
    def __str__(self):
        return f"Name:{self.name} Start:({self.x1}, {self.y1}) Ende:({self.x2}, {self.y2}) Länge:({self.lenght}), normierter Endpunkt:({self.x3}, {self.y3})"
    def get_kraft(self):
        return self.x1, self.y1, self.x2, self.y2, self.name
    def get_kraft_normiert(self):
        return self.x1, self.y1, self.x3, self.y3, self.name

class Balken:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x = [x1, x1, x2, x2, x1]
        self.y = [y1 -0.2, y1 + 0.2, y2 + 0.2, y2 - 0.2, y1 - 0.2]
    def __str__(self):
        return f"X:{self.x}, Y:{self.y}"
    
class Knoten:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def __str__(self):
        return f"Knoten {self.name}:(x={self.x}, y={self.y})"
    
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_name(self):
        return self.name
            