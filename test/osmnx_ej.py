import osmnx as ox
import matplotlib.pyplot as plt
import os
import googlemaps


def get_nodes(G):
    # Extraer y mostrar información de nodos
    for nodo, atributos in G.nodes(data=True):
        print("Nodo:", nodo)
        print("Atributos:", atributos)
        print("----------------")

def get_edges(G):
    
# Extraer y mostrar información de aristas
# En un MultiDiGraph, cada arista puede tener una clave adicional, así que podemos usar keys=True
    for origen, destino, clave, atributos in G.edges(keys=True, data=True):
        print("Desde nodo:", origen, "hasta nodo:", destino)
        print("Clave de la arista:", clave)
        print("Atributos:", atributos)
        print("----------------")

def remove_cache():
    dir_name="cache"
    for doc in os.listdir(os.path.join(os.getcwd(),dir_name)):
        os.remove(os.path.join(os.getcwd(),dir_name,doc))

#remove_cache()

place = "Coyoacán,Ciudad de México,México"
tags = {'amenity': 'restaurant'}
gdf=ox.geocode_to_gdf(place)

polygon = gdf.iloc[0].geometry



# Generamos el grafo usando el polígono
G = ox.graph_from_polygon(polygon, network_type='drive')

target_node = list(G.nodes())[5]  # Ejemplo: elegimos el sexto nodo
node_colors = ['red' if nodo == target_node else 'blue' for nodo in G.nodes()]

#fig, ax = ox.plot_graph(G,node_color=node_colors)
get_nodes(G)

#restaurantes = ox.features_from_place(place, tags)
#print(restaurantes[['name','amenity']])

#El usuario debe meter su calle


