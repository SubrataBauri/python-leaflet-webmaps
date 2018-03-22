import folium
import pandas

dataFrame = pandas.read_csv("data_CSV.csv")

# create a terrain map
map = folium.Map(location=[45.372, -121.697], zoom_start=5, tiles="Stamen Terrain")

for lat,lon,name,elev in zip(dataFrame["LAT"], dataFrame["LON"], dataFrame["NAME"], dataFrame["ELEV"]):

    folium.Marker(location = [lat, lon],
                  popup = name,
                  icon = folium.Icon(color='green' if elev in range(0, 1000) else 'orange' if elev in range(1000, 3000) else 'red', icon='info-sign')
                  ).add_to(map)

map.save("multi-marker-map.html") # create map file