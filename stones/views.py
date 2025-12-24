from django.shortcuts import render
import folium
from stones.models import Stone

def index(request):
    m = folium.Map([46.8415, -122.5830], zoom_start=6)
    stones = Stone.objects.all()
    for stone in stones:
        folium.Marker(
            location=[stone.latitude, stone.longitude],
            popup=stone.name,
            tooltip=stone.name,
            icon=folium.Icon(color="gray"),
        ).add_to(m)

    m.add_child(
        folium.LatLngPopup()
    )

    html_string = m._repr_html_()

    return render(request, "maps.html", {'map': html_string})

def traffic(request):
    zoom_level = 16

    # Create the map
    map = folium.Map(
        [45.504904, -122.656131],
        zoom_start=zoom_level,
        tiles="OpenStreetMap",
    )

    html_string = map._repr_html_()

    return render(request, "maps.html", {'map': html_string})