import networkx as nx

import matplotlib.pyplot as plt

pipeline = nx.DiGraph()
pos = nx.spring_layout(pipeline)

nodes = ["task1","task2","task3","task4"]


for x in range(0,len(nodes)-1):
	pipeline.add_edge(nodes[x],nodes[x+1])


p=nx.drawing.nx_pydot.to_pydot(pipeline)
p.write_png('teste.png')

print(list(nx.bfs_edges(pipeline,"task1", reverse=False)))
