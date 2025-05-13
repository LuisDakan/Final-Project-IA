
import get_data as dg
import heapq
class graph:

    INF=0

    

    def __init__(self):
        source=0
        INF=1e16
        #Se crea la lista de nodos
        list_nodes=[]
        #Se le asigna un id a cada nodo
        id={}
        #Se crea una lista de adyacencia
        adj=[]
        #Se crea un vector para guardar las distancias mínimas
        dist=[]
        #Se crea un vector para guardar los caminos
        path=[]
        #Inicializacion de lista de nodos y id
        list_nodes=dg.generate_nodes()
        for i in range(len(list_nodes)):
            self.id[list_nodes[i]]=i
        #Creación de la lista de adyacencia en base al id
        adj=[[] for _ in self.id]
        for a,b,c in dg.generate_edges():
            adj[a].append((c,b))
        #Inicialización de los vectores
        self.clean()

    def clean(self):
        self.dist=[self.INF for _ in self.id]
        self.path=[0 for _ in self.id]

    def query_distance(self,node):
        return self.dist[node]

    def query_path(self,node):
        stack=[]
        while self.path[node]!=-1:
            stack.push(node)
            node=self.path[node]
        return stack

    def dijkstra(self,s):
        self.dist[self.id[s]]=0
        self.path[self.id[s]]=-1
        priority_queue=[]
        heapq.heappush(priority_queue,(0,self.id[s]))
        while priority_queue:
            current_distance,current_node=heapq.heappop(priority_queue)
            if current_distance>self.dist[current_node]:
                continue
            for adjnode,weight in self.adj[current_node]:
                if(current_distance+weight<self.dist[adjnode]):
                    self.dist[adjnode]=current_distance+weight
                    heapq.heappush(priority_queue,(self.dist[adjnode],adjnode))

    def change_source(self,s):
        self.clean()
        self.dijkstra(s)

    
    


            
            



