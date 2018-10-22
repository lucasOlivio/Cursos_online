import folium
import pandas

data = pandas.read_csv("world_volcanoes.csv", sep=";")

lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
nam = list(data["NAME"])

def color_producer(elev):
    if elev <= 1000:
        return "green"
    elif 1000 < elev <= 3000:
        return "orange"
    else:
        return "red"

map=folium.Map(location=[48.7767982,-121.8109970], zoom_start=6, tiles="Mapbox Bright")

fg_volcanoes = folium.FeatureGroup(name="Volcanoes")

for lt, ln, nm, el in zip(lat, lon, nam, elev):
    pop = str(nm)+" - "+str(el)
    fg_volcanoes.add_child(folium.CircleMarker(location=[lt, ln], popup=pop, color='grey', radius=6, fill=True, fill_color=color_producer(el), fill_opacity=0.8))

fg_population = folium.FeatureGroup(name="Population")

fg_population.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg_volcanoes)
map.add_child(fg_population)
map.add_child(folium.LayerControl())

map.save("Map1.html")
