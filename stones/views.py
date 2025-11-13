from django.shortcuts import render
import folium

def index(request):
    m = folium.Map([45.35, -121.6972], zoom_start=12)
    
    folium.Marker(
        location=[45.3288, -121.6625],
        tooltip="Click me!",
        popup="Mt. Hood Meadows",
        icon=folium.Icon(icon="cloud"),
    ).add_to(m)

    folium.Marker(
        location=[45.3311, -121.7113],
        tooltip="Click me!",
        popup="Timberline Lodge",
        icon=folium.Icon(color="green"),
    ).add_to(m)
    html_string = m._repr_html_()

    return render(request, "maps.html", {'map': html_string})