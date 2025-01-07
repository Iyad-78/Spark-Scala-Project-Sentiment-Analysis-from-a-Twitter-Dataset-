import pandas as pd
import plotly.express as px

# Charger les résultats des clusters
clusters = pd.read_csv("C:/Users/iyadb/OneDrive/Documents/Tweets.csv/clusters4.csv/part-00000-9495f2c7-99ba-463e-930a-4b7222abb6c7-c000.csv")

# Visualiser les clusters (on utilise la colonne "word" pour l'axe des x)
fig = px.scatter(clusters, x="word", y="kmeansPrediction", color="kmeansPrediction",
                 title="Clusters de mots", labels={"kmeansPrediction": "Cluster"})
fig.show()


import pandas as pd
import networkx as nx
import plotly.graph_objects as go

# Charger les nœuds et les arêtes
vertices = pd.read_csv("C:/Users/iyadb/OneDrive/Documents/Tweets.csv/vertices4.csv/part-00000-afd5acfa-0ac8-430d-9e52-f580607d87d2-c000.csv")
edges = pd.read_csv("C:/Users/iyadb/OneDrive/Documents/Tweets.csv/edges4.csv/part-00000-8358e4f9-b35b-4d21-ac8e-bb0c8839c2d7-c000.csv")

# Créer le graphe NetworkX
G = nx.DiGraph()
for _, row in vertices.iterrows():
    G.add_node(row["id"], label=row["word"])  # Utiliser "word" comme label
for _, row in edges.iterrows():
    G.add_edge(row["src"], row["dst"], weight=row["weight"])

# Obtenir les positions pour la visualisation
pos = nx.spring_layout(G)

# Préparer les données pour Plotly
edge_trace = go.Scatter(
    x=[], y=[], line=dict(width=0.5, color='#888'), hoverinfo='none', mode='lines')
for edge in G.edges(data=True):
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_trace['x'] += (x0, x1, None)
    edge_trace['y'] += (y0, y1, None)

node_trace = go.Scatter(
    x=[], y=[], text=[], mode='markers+text',
    marker=dict(size=10, color='lightblue', line=dict(width=2)))
for node in G.nodes(data=True):
    x, y = pos[node[0]]
    node_trace['x'] += (x,)
    node_trace['y'] += (y,)
    node_trace['text'] += (node[1]['label'],)  # Afficher le label du nœud

# Créer la figure
fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(title="Graphe des mots",
                             showlegend=False,
                             margin=dict(b=0, l=0, r=0, t=0),
                             xaxis=dict(showgrid=False, zeroline=False),
                             yaxis=dict(showgrid=False, zeroline=False)))
fig.show()
fig.show(renderer="browser")