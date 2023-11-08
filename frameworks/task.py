import matplotlib
matplotlib.use('Qt5Agg')


from public.classes.Plot import Plot
from public.functions.generate import generate
from public.functions.lagerreaktionen_freischnitt import freischnitt_lagerreaktionen
from public.functions.knoten_freischnitt import freischnitt_knoten

plot1 = generate()
plot1.plot()

plot2 = freischnitt_lagerreaktionen(plot1)
plot2.plot()

plot3 = freischnitt_knoten(plot2, 'A', 'Plot3')
plot3.plot()

plot4 = freischnitt_knoten(plot2, 'C', 'Plot4')
plot4.plot() 