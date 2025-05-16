
import get_data as dg
import heapq
import osmnx as ox
class Graph:

    def __init__(self):
        self.geo=dg.Geo()
        self.source=0
        self.INF=1e16
        #Se crea la lista de nodos
        self.list_nodes=[]
        #Se le asigna un id a cada nodo
        self.id={}
        #Se crea una lista de adyacencia
        self.adj=[]
        #Se crea un vector para guardar las distancias mínimas
        self.dist=[]
        #Se crea un vector para guardar los caminos
        self.path=[]
        #Se crea un vector para los caminos con aristas
        self.path_edge=[]
        #Inicializacion de lista de nodos y id
        self.list_nodes=list(self.geo.generate_nodes())
        for i in range(len(self.list_nodes)):
            self.id[self.list_nodes[i]]=i
        #Diccionario del id de la arista
        #Creación de la lista de adyacencia en base al id
        self.adj=[[] for _ in self.id]
        for a,b,at in self.geo.generate_edges():
            self.adj[self.id[a]].append((b,float(at["length"])))
            
        #Inicialización de los vectores
        self.clean()
        #Vector de colores de los nodos
        self.color_nodes=[None for nodo in self.list_nodes]
        #Vector de colores de las aristas
        self.color_edges=[None for nodo in self.geo.generate_edges()]

    def clean(self):
        self.dist=[self.INF for _ in self.id]
        self.path=[0 for _ in self.id]
        self.path_edge=[0 for _ in self.id]

    def query_distance(self,direction):
        node=self.geo.get_Node(direction=direction)
        return self.dist[self.id[node]]

    def query_path(self,direction):
        node=self.geo.get_Node(direction=direction)
        stack_node=[]
        stack_edge=[]
        while self.path[self.id[node]]!=-1:
            stack_node.append(node)
            stack_edge.append(self.path_edge[self.id[node]])
            node=self.path[self.id[node]]
        return stack_node,stack_edge

    def dijkstra(self,s):
        self.dist[self.id[s]]=0
        self.path[self.id[s]]=-1
        priority_queue=[]
        heapq.heappush(priority_queue,(0,s))
        while priority_queue:
            current_distance,current_node=heapq.heappop(priority_queue)
            id_cur=self.id[current_node]
            if current_distance>self.dist[id_cur]:
                continue
            for adjnode,weight in self.adj[id_cur]:
                id_adj=self.id[adjnode]
                if(current_distance+weight<self.dist[id_adj]):
                    self.path_edge[id_adj]=(current_node,adjnode)
                    self.path[id_adj]=current_node
                    self.dist[id_adj]=current_distance+weight
                    heapq.heappush(priority_queue,(self.dist[id_adj],adjnode))

    def set_source(self,direction):
        self.clean()
        direction=f"{direction}, Coyoacán, Ciudad de México, México"
        self.source=self.geo.get_Node(direction)
        for i in range(len(self.list_nodes)):
            if(self.list_nodes[i]==self.source):
                self.color_nodes[i]='red'
            elif(self.list_nodes[i] in self.geo.general_rest):
                self.color_nodes[i]='orange'
            else:
                self.color_nodes[i]='blue'
        self.dijkstra(self.source)

    def print_graph(self):
        ox.plot_graph(self.geo.G,node_color=self.color_nodes,node_size=10)

    def print_path(self,destiny):
        path_node,path_edge=self.query_path(destiny)
        for node in path_node:
            self.color_nodes[self.id[node]]='red'
        for i, (u, v, k) in enumerate(self.geo.G.edges(keys=True)):
            if (u, v) in path_edge or (v, u) in path_edge:
                self.color_edges[i] = 'red'
            else:
                self.color_edges[i]='white'
        ox.plot_graph(self.geo.G,node_color=self.color_nodes,edge_color=self.color_edges,node_size=10)

    
        
if __name__=='__main__':
    grafica=Graph()
    grafica.set_source("Clavel 68")
    #grafica.set_source("Museo 150,San Pablo Tepetlapa")
    #grafica.print_graph()
    grafica.print_path("Museo 150,San Pablo Tepetlapa")


    


    

            



