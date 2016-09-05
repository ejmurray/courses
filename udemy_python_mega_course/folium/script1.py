import folium
import pandas

df=pandas.read_csv("Volcanoes-USA.txt")
map=folium.Map(location=[df['LAT'].mean(),df['LON'].mean()], zoom_start=6, tiles="Stamen Terrain")
# deprecated #
#map.simple_marker(location=[45.3288, -121.6625], popup="Mt. Hood Meadows", marker_color="red");
#map.create_map(path="test.html")

def color(elev):
   minimum=int(min(df['ELEV']))
   step=int((max(df['ELEV'])-(minimum))/3)
   if elev in range(minimum,minimum+step):
      col = 'green'
   elif elev in range(minimum+step,minimum+step*2):
      col='orange'
   else:
      col='red'
   
   return col;

for lat,lon,name,elev in zip(df['LAT'],df['LON'], df['NAME'], df['ELEV']):
   map.add_child(folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color=color(elev))))

map.save(outfile="test.html", close_file=True)