import pandas
import folium

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def icon_color(elevation):
    if elevation >= 3000:
        return "darkred"
    elif elevation in range(2000, 3000):
        return "orange"
    elif elevation in range(0, 2000):
        return "green"


map = folium.Map(location=[lat[0], lon[0]], tiles="Stamen Toner", zoom_start=6)

fg_1 = folium.FeatureGroup(name="Volcanoes")

for lt, ln, ele, nam in zip(lat, lon, elev, name):
    fg_1.add_child(folium.CircleMarker(location=[lt, ln],
                                 popup=f"{nam} \n {ele}m",
                                 radius=10,
                                 fill_color=icon_color(ele), color= "black", opacity= 0.8))

fg_2 = folium.FeatureGroup(name="Population")

fg_2.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
                              style_function=lambda x: {"fillColor": "pink" if x["properties"]["POP2005"] < 10000000
                                                        else "purple" if x["properties"]["POP2005"] in range(10000000, 20000001) else "beige"}))
map.add_child(fg_1)
map.add_child(fg_2)
map.add_child(folium.LayerControl())

map.save("Map.html")