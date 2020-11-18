# input must be via ', '
import networkx as nx
lst = []
with open('facebook_combined.txt','r') as file:
    for row in file:
        lst.append(tuple(map(int, row.split())))
G = nx.Graph()
G.add_edges_from(lst)
nodes = list(map(int, input().split(', ')))
for i in nodes:
    nodes_new = list(set(nodes)-set([i])) 
    for j in list(set(nodes)-set([i])) :
        nodes_new += list(G.neighbors(j))
    if set(nodes_new) == set(G.nodes()):
        print(i)
