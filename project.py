import folium

# create map object
map = folium.Map(location=[22.622033, 88.450197], zoom_start=13)

# map.create_map(path="index.html") # doesn't have it anymore

map.save("index.html") # create map file

# create a terrain map
map2 = folium.Map(location=[22.622033, 88.450197], zoom_start=13, tiles="Stamen Terrain")
map2.save("terrain-map.html")