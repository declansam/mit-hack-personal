
# conda install omegacen/label/broken::asciinet

import networkx as nx
from asciicode import graph_to_ascii

def connect(q0, qx, graph, potential_node_dic):
    
    graph.add_edge(q0, qx)
    
    if qx in potential_node_dic.keys():   
        for node in potential_node_dic[qx]:
            potential_node_dic[q0].append(node)
            graph.add_node(node)

    potential_node_dic[q0].remove(qx)

def createGraph():
    return nx.Graph()


def initGraph(graph):
    potential_node_dic = {'q0' : ['q1', 'q2'], 'q1' : ['q3', 'q4']}

    graph.add_node("q0")
    graph.add_node("q1")
    graph.add_node("q2")

    return potential_node_dic


def logging(graph, log = False):
    ascii_art = graph_to_ascii(graph)

    if log:
        print(ascii_art)


def getPotentialNodeDic():
    return potential_node_dic


def setConnection(qx):
    connect('q0', qx, graph, potential_node_dic)
    logging(graph, True)


graph = createGraph()
potential_node_dic = initGraph(graph)


## TESTING (MODULAR)
# print(getPotentialNodeDic())
# setConnection('q1')
# print(getPotentialNodeDic())


## TESTING
# connect('q0', 'q1', graph ,potential_node_dic)
# print("2:\n", potential_node_dic)
# connect('q0', 'q2', graph ,potential_node_dic)
# connect('q0', 'q3', graph ,potential_node_dic)
