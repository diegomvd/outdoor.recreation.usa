import pandas as pd

import json
 
# Opening JSON file
f = open('./networks/subgraphs/network_test_CA,NV,AZ.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
print(data)

nodes = data.get("nodes")
nodeDf = pd.DataFrame(nodes)
print(nodeDf)
# nodeDf.to_csv('/home/dibepa/.klab/export/network_utah_nevada_nodes.csv',index=False)

edges = data.get("edges")
edgeDf = pd.DataFrame(edges)
print(edgeDf)
# edgeDf.to_csv('/home/dibepa/.klab/export/network_utah_nevada_edges.csv',index=False)