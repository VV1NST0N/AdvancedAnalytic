#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 12:23:15 2018

@author: guckert
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def rowSum(m, row):
    total = 0
    for col in range(len(m[row])):
        total += m[row][col]
    return total


def pagerank(g,v):
    alpha=0.85
    n=len(v)    
    m=nx.to_numpy_array(g)
    for i in range (len(m)):
        t=rowSum(m,i)
        if t!=0:
            m[i]=m[i]/t        
    a=np.transpose(m)
    one=[]
    for i in range(len(v)):
        one.append(1)
    for i in range(100):
        v2=[(1-alpha)/n * i for i in one]+alpha*a@v
        v=v2
    return v

# Erzeuge Graph und Startvektor
g=nx.Graph()
v=[0,0,1,0,0,0,0,0,0,0,0]
for n in ['A','B','C','D','E','F','G','H','I','J','K']:
    g.add_node(n)
g.add_edges_from([('C','B'),('B','C'),('D','A'),('D','B'),('E','B'),('E','D'),('E','F'),('F','B'),('F','E'),('G','B'),('G','E'),('H','B'),('H','E'),('I','B'),('I','E'),('J','E'),('K','E')])
nx.draw_shell(g, with_labels=True, font_weight='bold')
v=pagerank(g,v)
print(v)

# Kopiere Grpah und passe Größe der Knotn dem Pagerank an
g2=nx.Graph()
g2.add_nodes_from(g.nodes())
g2.add_edges_from(g.edges())
sizes=[10000 * i for i in v]
nx.draw_shell(g2, with_labels=True, font_weight='bold',node_size=sizes)