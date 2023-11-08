from public.classes.Plot import Plot

def freischnitt_knoten(plot2, knoten, plot_name):
    plot3 = Plot(False, plot_name)

    target_knoten = plot2.get_knoten_name(knoten)

    plot3.add_knoten(target_knoten.get_x(), target_knoten.get_y(), target_knoten.get_name())

    connections = plot2.get_connections()

    connections_with_target = []

    for connection in connections:
        if knoten in connection:
            connections_with_target.append(connection)

    for connection in connections_with_target:
        other_knoten_name = connection[0] if connection[1] == knoten else connection[1]
        other_knoten = plot2.get_knoten_name(other_knoten_name)
        plot3.add_node_none(other_knoten.get_x(), other_knoten.get_y(), other_knoten.get_name())
    
    for connection in connections_with_target:
        plot3.add_connection(connection[0], connection[1])

    for connection in connections_with_target:
        if connection[0] != knoten:
            connection = (connection[1], connection[0])

        plot3.norm_connection(connection[0], connection[1])
        plot3.add_force(plot3.get_node_none_name(connection[1]).get_x(), plot3.get_node_none_name(connection[1]).get_y(), -1 * (plot3.get_knoten_name(connection[0]).get_x() - plot3.get_node_none_name(connection[1]).get_x()), -1 * (plot3.get_knoten_name(connection[0]).get_y()- plot3.get_node_none_name(connection[1]).get_y()), f'Kraft_{connection[1]}')
    
    kraft = plot2.get_force_by_point(knoten)
    try:
        kx1, ky1, kx2, ky2, name = kraft.get_kraft()
        plot3.add_force(kx1, ky1, kx2, ky2, name)
    except:
        b = 0

    kraft = plot2.get_force_none_by_point(knoten)
    try:
        kx1, ky1, kx2, ky2, name = kraft.get_kraft()
        plot3.add_force_none(kx1, ky1, kx2, ky2, name)
    except:
        b = 0

    

    

    markdown_text = f"""

![Alternativer Text](frameworks/../{plot_name}.png)
    """
    output_file_path = 'frameworks/task/task.md'
    with open(output_file_path, 'a') as markdown_file:
        markdown_file.write(markdown_text)
    return(plot3)