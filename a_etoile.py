from time import time
t0 = time()
Graph = {
    'A': [('D', 5), ('C', 5)],
    'D': [('C', 6),('E', 2)],
    'C': [('H', 3),('F', 2),('B', 3)],
    'E': [('B', 5)],
    'B': [('C', 3),('F', 3),('G', 4),('I', 5)],
    'F': [('C', 2),('G', 3),('B', 3)],
    'G': [('B', 4),('F', 3),('I', 3)],
    'H': [('I', 4)],  
}

def heuristic(noeud):
        H = {
        'A': 10,
        'B': 4,
        'C': 5,
        'D': 10,
        'E': 10,
        'F': 3,
        'G': 3,
        'H': 4,
        'I': 0,
            } 
        return H[noeud]
#define fuction to return neighbor and its distance
#from the passed node
def noeudsFils(sommet):
    if sommet in Graph:
        return Graph[sommet]
    else:
        return None  
print(noeudsFils('A'))
def A_etoile(depart, destination):
        '''
        Initialise Liste ouverte 
        et Liste fermée tant que des listes vides
        Initialise Liste ouverte en tant liste 
        de départ
        '''
        listeOuv = [depart] 
        listeFerm = []

        '''
        Coût g[départ] = 0 
        '''
        g = {} 
        g[depart] = 0
        '''
        Parents[départ] = départ 
        '''
        parents = {}
        parents[depart] = depart
         
        while len(listeOuv) > 0:
            noeudActuel = None
 
            #Trouver le nœud avec min(f)
            for sommet in listeOuv:
                if noeudActuel == None or g[sommet] + heuristic(sommet) < g[noeudActuel] + heuristic(noeudActuel):
                    noeudActuel = sommet
            if noeudActuel == destination or Graph[noeudActuel] == None:
                pass
            else:
                for (m, weight) in noeudsFils(noeudActuel):
                    #nodes 'm' not in first and last set are added to first
                    #noeudActuel is set its parent
                    if m not in listeOuv and m not in listeFerm:
                        listeOuv.append(m)
                        parents[m] = noeudActuel
                        g[m] = g[noeudActuel] + weight
    
                    #for each node m,compare its distance from depart i.e g(m) to the
                    #from depart through noeudActuel node
                    else:
                        if g[m] > g[noeudActuel] + weight:
                            #update g(m)
                            g[m] = g[noeudActuel] + weight
                            #change parent of m to noeudActuel
                            parents[m] = noeudActuel
                            #if m in closed set,remove and add to open
                            if m in listeFerm:
                                listeFerm.remove(m)
                                listeOuv.append(m)
 
            if noeudActuel == None:
                print('Path does not exist!')
                return None
 
            # if the noeudActuel node is the destination
            # then we begin reconstructin the path from it to the depart
            if noeudActuel == destination:
                path = []
 
                while parents[noeudActuel] != noeudActuel:
                    path.append(noeudActuel)
                    noeudActuel = parents[noeudActuel]
 
                path.append(depart)
 
                path.reverse()
 
                print('le chemin est: {}'.format(path))
                return path
 
 
            # remove noeudActuel from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            listeOuv.remove(noeudActuel)
            listeFerm.append(noeudActuel)
        print('Impossible de trouver le chemin!')
        return None


A_etoile('A', 'I')
t1 = time ()

print('A* function takes ', (t1-t0), 'seconds and ',round((t1-t0)*1000, 0), ' milliseconds')
