import networkx as nx
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))
plt.title('Attractions in Chiang Mai', size=10)
G = nx.Graph()


locations = ["Nimman Day", "Chiang Mai Zoo", "Wat Phra That Doi Suthep", "Wat Phra That Doi Kham", 
             "Botanical Garden Queen Sirikit", "Moncham", "Grand Canyon Mae Jo", "Mae Kampong", 
             "Tha Phae Gate", "Chiang Mai Municipality", "Warorot Market", "Wat Umong",
             "Wat Phra Singh Woramahaviharn", "Doi Luang Chiang Dao", "Maesa Elephant Camp"]
for location in locations:
    G.add_node(location)

edges = [("Chiang Mai Municipality", "Nimman Day", 3.1),
         ("Nimman Day", "Chiang Mai Zoo", 3.6),
         ("Chiang Mai Zoo", "Wat Phra That Doi Suthep", 11.6),
         ("Wat Phra That Doi Suthep", "Wat Phra That Doi Kham", 8.5),
         ("Wat Phra That Doi Kham", "Botanical Garden Queen Sirikit", 12.1),
         ("Botanical Garden Queen Sirikit", "Moncham", 11.6),
         ("Moncham", "Grand Canyon Mae Jo", 18.7),
         ("Grand Canyon Mae Jo", "Mae Kampong", 28.8),
         ("Mae Kampong", "Tha Phae Gate", 36.9),
         ("Tha Phae Gate", "Chiang Mai Municipality", 2.1),
         ("Chiang Mai Municipality", "Warorot Market", 0.9),
         ("Warorot Market", "Wat Umong", 4.7),
         ("Wat Umong", "Wat Phra Singh Woramahaviharn", 5.2),
         ("Wat Phra Singh Woramahaviharn", "Chiang Mai Zoo", 3.1),
         ("Chiang Mai Zoo", "Doi Luang Chiang Dao", 62.6),
         ("Doi Luang Chiang Dao", "Maesa Elephant Camp", 51.5),
         ("Maesa Elephant Camp", "Botanical Garden Queen Sirikit", 17.8)]

for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2]) 

color_map = {"Nimman Day": "blue",
             "Chiang Mai Zoo": "orange",
             "Wat Phra That Doi Suthep": "green",
             "Wat Phra That Doi Kham": "purple",
             "Botanical Garden Queen Sirikit": "pink",
             "Moncham": "brown",
             "Grand Canyon Mae Jo": "grey",
             "Mae Kampong": "red",
             "Tha Phae Gate": "cyan",
             "Chiang Mai Municipality": "magenta",
             "Warorot Market": "blue",
             "Wat Umong": "orange",
             "Wat Phra Singh Woramahaviharn": "green",
             "Doi Luang Chiang Dao": "purple",
             "Maesa Elephant Camp": "pink"}

for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

def continues():
    while True:
        choice = input("Do you want to continue (C) or stop (S)? ").lower()
        if choice == "c":
            return main()
        elif choice == "s":
            return False
        else:
            print("Invalid choice. Please enter either C or S.")


def main():
    #อินพุท ว่าอยากเริ่มจุดไหน และ เอาพุท จบจุดไหน เพื่อหาระยะทางที่สั้นที่สุด
    print("Please select a starting location:")
    for i, location in enumerate(locations):
        print(f"{i+1}. {location}")
    start = input("Enter the starting point: ")

    print("\nPlease select an ending location:")
    for i, location in enumerate(locations):
        print(f"{i+1}. {location}")

    destination = input("Enter the destination: ")

    path = nx.shortest_path(G, start, destination)

    print("Shortest path from", start, "to", destination, ":", path)
    distances = []
    for i in range(len(path)-1):
        distance = G[path[i]][path[i+1]]['weight']
        distances.append(distance)

    print("Total distance:", sum(distances), "km")


    pos = nx.spring_layout(G, seed=42)
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_nodes(G, pos, node_color=list(color_map.values()))
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edge_color=[G[u][v]['weight'] for u, v in G.edges()])
    nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1]) for i in range(len(path)-1)], edge_color='r', width=2)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()
    continues()

main()