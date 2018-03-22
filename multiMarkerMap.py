import folium
import pandas

dataFrame = pandas.read_csv("data_CSV.csv")

# create a terrain map
#map = folium.Map(location=[45.372, -121.697], zoom_start=5, tiles="Stamen Terrain")
map = folium.Map(location=[dataFrame["LAT"].mean(), dataFrame["LON"].mean()], zoom_start=5, tiles="Stamen Terrain")

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


for lat, lon, name, elev in zip(dataFrame["LAT"], dataFrame["LON"], dataFrame["NAME"], dataFrame["ELEV"]):

    folium.Marker(location=[lat, lon],
                  popup=name,
                  icon=folium.Icon(color=color(elev), icon='info-sign')
                  ).add_to(map)

map.save("multi-marker-map.html") # create map file