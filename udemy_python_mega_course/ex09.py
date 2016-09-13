from bokeh.plotting import figure, output_file, show
import pandas

df=pandas.read_excel("http://pythonhow.com/verlegenhuken.xlsx", sheetname=0)
df["Temperature"]=df["Temperature"]/10
df["Pressure"]=df["Pressure"]/10

p=figure(plot_width=500, plot_height=400, tools='pan,resize', logo=None)

p.title.text="Temperature and Air Pressure"
p.xaxis.axis_label="Temperature (°C)"
p.yaxis.axis_label="Pressure (hPa)"
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None

p.circle(df["Temperature"],df["Pressure"],size=0.5)

output_file("ex09.html")

show(p)