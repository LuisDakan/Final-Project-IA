import osmnx as ox
import geopandas as gpd
import os
import googlemaps

class Geo:
    
    def __init__(self):
        self.place="Coyoacán,Ciudad de México,México" #Lugar de la gráfica
        #Obtención de la información del lugar
        gdf=ox.geocode_to_gdf(self.place)
        polygon = gdf.iloc[0].geometry

        #Creación del grafo
        self.G = ox.graph_from_polygon(polygon, network_type='drive')


        #Creación de un gdf con restaurantes
        self.restaurantes = ox.features_from_place(self.place, {'amenity': 'restaurant'})
        print(ox.distance.nearest_nodes(self.G,X=-99.1850155,Y=19.3136655))

        #Mapa para guardar el restaurante, se guardarán los ínidces en el gdf
        self.general_rest={}
        for index,row in self.restaurantes.iterrows():
            geom=row["geometry"]
            if(geom.geom_type=='Point'):
                rest_id=ox.distance.nearest_nodes(self.G,X=geom.x,Y=geom.Y)
            else:
                centro=geom.centroid
                rest_id=ox.distance.nearest_nodes(self.G,X=centro.x,Y=centro.Y)
            self.general_rest[rest_id]=index
        
        #Creación de gmaps para convertir lugares en coordenadas

        self.gmaps = googlemaps.Client(key=os.getenv("API_KEY_GOOGLE"))

    def generate_nodes(self):
        return self.G.nodes()

    def generate_edges(self):
        return self.G.edges()

    def get_Node(self,direction):
        result=self.gmaps.geocode(direction)
        ubi=result[0]['geometry']['location']
        return ox.distance.nearest_nodes(self.G,X=ubi["lng"],Y=ubi["lat"])
