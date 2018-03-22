import folium
import pandas

dataFrame = pandas.read_csv("data_CSV.csv")

# create a terrain map
map = folium.Map(location=[dataFrame["LAT"].mean(), dataFrame["LON"].mean()], zoom_start=2, tiles="Mapbox Bright")

# create method for conditional colouring
def color(elev):
    minimum=int(min(dataFrame["ELEV"]))
    step=int((max(dataFrame["ELEV"]) - min(dataFrame["ELEV"]))/3)
    if elev in range(minimum, minimum+step):
        col = "green"
    elif elev in range(minimum+step, minimum+step*2):
        col = "blue"
    else:
        col="red"
    return col

fg = folium.FeatureGroup(name='Volcano Locations')

for lat, lon, name, elev in zip(dataFrame["LAT"], dataFrame["LON"], dataFrame["NAME"], dataFrame["ELEV"]):
    fg.add_child(folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color=color(elev), icon='info-sign')))

# add marker layer
map.add_child(fg)

# add population layer
map.add_child(folium.GeoJson(open('world_population.json',encoding = "utf-8-sig").read(),
                             name='World Population',
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] <= 10000000 else 'orange' if 10000000 < x['properties']['POP2005'] <= 20000000 else 'red'}))

# option to toggle layers
map.add_child(folium.LayerControl())

map.save("world-map.html") # create map file