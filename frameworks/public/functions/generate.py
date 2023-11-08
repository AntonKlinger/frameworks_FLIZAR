from public.classes.Plot import Plot

import random

def generate():

    plot1 = Plot(True, 'Plot1')

    x1 = 0
    y1 = random.randint(1, 7)
    plot1.add_knoten(x1, y1, 'E')

    x2 = random.randint(-2, -1)
    y_alt = y1
    while True:
        y2 = random.randint(3, 7)
        if y2 != y_alt:
            break
    plot1.add_knoten(x2, y2, 'C')
    plot1.add_knoten(abs(x2), y2, 'D')

    x4 = random.randint(-4, -2)
    if y1 > y2:
        while True:
            y4 = random.randint(1, y1 + 2)
            if y4 > ((y1-y2)/(x1-x2)*x4+y1):
                break
    else:
        while True:
            y4 = random.randint(1, y1 + 2)
            if y4 < ((y1-y2)/(x1-x2)*x4+y1):
                break
    plot1.add_knoten(x4, y4, 'A')
    plot1.add_knoten(abs(x4), y4, 'B')

    plot1.add_connection('E', 'C')
    plot1.add_connection('C', 'D')
    plot1.add_connection('D', 'E')
    plot1.add_connection('A', 'E')
    plot1.add_connection('A', 'C')
    plot1.add_connection('B', 'E')
    plot1.add_connection('D', 'B')

    direction = 1
    if y1 < y2:
        direction = -1
    lenght = random.randint(1,3)
    plot1.add_force(x1, y1, 0, direction*lenght, 'F')

    return(plot1)
