def freischnitt_lagerreaktionen(plot1):
    plot2 = plot1
    plot2.set_save_path('Plot2')
    
    plot2.set_bearings(False)

    node_info = plot2.get_knoten()
    for node in node_info:
        if node['name'] == 'A':
            xa = node['x']
            ya = node['y']

    plot2.add_force(xa, ya, 0, 1, 'AFV')
    plot2.add_force(xa, ya, 1, 0, 'AFH')

    for node in node_info:
        if node['name'] == 'B':
            xb = node['x']
            yb = node['y']

    plot2.add_force(xb, yb, 0, 1, 'FBV')

    
    F = plot1.get_force('F')
    x1 , y1, x2, y2, name = F.get_kraft()
    F = y2
    nF = -1 * F
    AFV = F/2 * -1
    BFV = F/2 * -1

    plot2.add_force_none(xa, ya, x2, AFV, 'AFV')
    plot2.add_force_none(xb, yb, x2, BFV, 'BFV')

    markdown_text = f"""
# Aufgabe 1
![Alternativer Text](frameworks/../Plot1.png)
![Alternativer Text](frameworks/../Plot2.png)
Aus der Geometrie des Fachwerks folgt:

$F_{{AV}} = F_{{BV}}$

$\\rightarrow: 0 = F_{{AH}}$

$\\uparrow: 0 = F_{{AV}} + F_{{BV}} + F$

$\\Rightarrow F_{{AV}} = F_{{BV}} = -F/2 = {nF}/2 = {BFV}$

Zur berechnung des Stabkräfte werden folgende Definitionen vorgenommen:

$F_{{S1}}$: AE

$F_{{S2}}$: AC

$F_{{S3}}$: CE

$F_{{S4}}$: DE
    """
    output_file_path = 'frameworks/task/task.md'
    with open(output_file_path, 'w') as markdown_file:
        markdown_file.write(markdown_text)
    return(plot2)