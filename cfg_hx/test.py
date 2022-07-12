import networkx as nx
from networkx.readwrite import json_graph
import networkx.drawing.nx_agraph as nxdraw
import os
import json

dotfile = "cfg/setpriority.dot"
outfolder = "out"

grph=nxdraw.read_dot(dotfile)
print ("nodes:", nx.number_of_nodes(grph))
print ("edges:", nx.number_of_edges(grph))


node1 = grph.nodes()["0xffffffff810b9440"]

node2 = grph.nodes()["0xffffffff810b94fc"]


shfile = open("dotsh.sh", "w")


paths = list(nx.all_simple_paths(grph, "0xffffffff810b9440", "0xffffffff810b94d2"))
count = 0
for path in paths:
	count = count+1
	for node in path:
		nx.set_node_attributes(grph, {node:"red"}, "fillcolor")
	if(count<10):
		dotname=outfolder+"/test"+"0"+str(count)+".dot"
	else:
		dotname=outfolder+"/test"+str(count)+".dot"
	nxdraw.write_dot(grph, dotname)
	if(count<10):
		pngname=outfolder+"/test"+"0"+str(count)+".png"
	else:
		pngname=outfolder+"/test"+str(count)+".png"
	cmdline="dot -Tpng -o "+pngname + " " + dotname
	shfile.write(cmdline)
	shfile.write("\n")

	for node in path:
		nx.set_node_attributes(grph, {node:"gray"}, "fillcolor")

shfile.close()
