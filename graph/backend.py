
import get_data as dg
import heapq
class graph:

    INF=0

    

    def __init__(self):
        INF=1e16
        #Se crea la lista de nodos
        list_nodes=[]
        #Se le asigna un id a cada nodo
        node_id={}
        #Se crea una lista de adyacencia
        adj=[]
        #Se crea un vector para guardar las distancias mínimas
        dist=[]
        #Se crea un vector para guardar los caminos
        path=[]

        #Inicializacion
        #Inicializacion de lista de nodos y id
        list_nodes=dg.generate_nodes()
        for i in range(len(list_nodes)):
            self.node_id[list_nodes[i]]=i
        #Creación de la lista de adyacencia en base al id
        adj=[[] for _ in self.node_id]
        for a,b,c in dg.generate_edges():
            adj[a].append((c,b))
        #Inicialización del vector de distancias
        self.clean()
        #Inicialización del vector de caminos

    #Vector dist
    def clean(self):
        self.dist=[self.INF for _ in self.node_id]
        self.path=[0 for _ in self.node_id]

    
    def dijkstra(self,s):
        self.dist[s]=0
        self.path[s]=0
        priority_queue=[]
        heapq.heappush(priority_queue,(0,s))
        while priority_queue:
            current_distance,current_node=heapq.heappop(priority_queue)
            if current_distance>self.dist[current_node]:
                continue
            for adjnode,weight in self.adj[current_node]:
                if(current_distance+weight<self.dist[adjnode]):
                    self.dist[adjnode]=current_distance+weight
                    heapq.heappush(priority_queue,(self.dist[adjnode],adjnode))

    


            
            



