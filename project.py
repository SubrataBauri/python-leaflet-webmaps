import folium

# create map object
map = folium.Map(location=[22.622033, 88.450197], zoom_start=14)

# create a terrain map
map2 = folium.Map(location=[22.622033, 88.450197], zoom_start=13, tiles="Stamen Terrain")

# map.simple_marker(location=[22.622033, 88.450197], popup="City Center 2", marker_color="red")
# map.simple_marker(location=[22.621086, 88.458555], popup="NKDA Stadium", marker_color="green")

folium.Marker(location=[22.622033, 88.450197],
              popup="City Center 2, \n New Town",
              icon=folium.Icon(color='red', icon='info-sign')
              ).add_to(map)
folium.Marker(location=[22.621086, 88.458555],
              popup="NKDA Stadium",
              icon=folium.Icon(color='green', icon='info-sign')
              ).add_to(map)

# map.create_map(path="index.html") # doesn't have it anymore

map.save("index.html") # create map file

map2.save("terrain-map.html")
