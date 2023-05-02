import tkinter as tk
import matplotlib.pyplot as plt
import networkx as nx
from urllib.request import urlopen
import json
import random

# Create the main window
root = tk.Tk()
root.title("Flight Search")

# Create the labels and entry widgets for City1 and City2
city1_label = tk.Label(root, text="City 1:")
city1_label.pack()
city1_entry = tk.Entry(root)
city1_entry.pack()
city2_label = tk.Label(root, text="City 2:")
city2_label.pack()
city2_entry = tk.Entry(root)
city2_entry.pack()

# Create a function to search for flights when the user clicks the "Search" button
def search_flights():
    # Read from URL
    file = urlopen("https://data.transportation.gov/resource/4f3n-jbg2.json?year=2022")
    Read = file.read()
    
    # Parse JSON
    flights = json.loads(Read)
    
    # Create NetworkX graph
    G = nx.Graph()
    for flight in flights:
        if city1_entry.get().lower() in flight["city1"].lower() and  city2_entry.get().lower() in flight["city2"].lower():
            G.add_edge(flight["city1"],flight["city2"], weight = flight["fare"])
    
    # Find minimum fare
  #Big O of this is O(N^2)
    ConnectingFlights = {}
    for flight1 in flights:
        for flight2 in flights:
            if city1_entry.get().lower() in flight1["city1"].lower() and city2_entry.get().lower() in flight2["city2"].lower() and flight1["city2"] == flight2["city1"]:
                G.add_edge(flight1["city1"],flight1["city2"])
                G.add_edge(flight2["city1"],flight2["city2"])
                ConnectingFlights[flight2["city1"]] = flight2["fare"]
    if ConnectingFlights:
        min_fare = min(ConnectingFlights.values())
        for d,a in ConnectingFlights.items():
            if float(a) == min_fare:
                low_cost_flight = d
                print(f"The Cheapest flights from {low_cost_flight} and costs ${min_fare}")
  
      # Cheapest flight first
  #Big O of this is O(n)
    if ConnectingFlights:
      min_fare = min(ConnectingFlights.values())
      for d,a in sorted(ConnectingFlights.items(), key=lambda x: x[1]):
            print(f"The Cheapest flights from {d} and costs ${a}")
    if ConnectingFlights:
        print("Indirect flights:")
        for flight, cost in ConnectingFlights.items():
            print(flight + " costs $" + str(cost))
    else:
        print("No indirect flights found.")
  ## display the resulting indirect flights that reach the destination
    if ConnectingFlights:
        min_fare = min(ConnectingFlights.values())
        for d,a in ConnectingFlights.items():
            if float(a) == min_fare:
                low_cost_flight = d
                print(f"The Cheapest flights from {low_cost_flight} and costs ${min_fare}")
    else:
        print("No flights found.")
    
    # Draw the graph
    pos_spaced = nx.fruchterman_reingold_layout(G, k=0.5, iterations=100)
    plt.figure(figsize=(6,10)) # 6x10 inches
    nx.draw(G, pos=pos_spaced, with_labels=True) 
    nx.draw_networkx_edge_labels(G, pos_spaced, edge_labels=nx.get_edge_attributes(G,"weight"))
    plt.show(block=False)

# Create the Search button
search_button = tk.Button(root, text="Search", command=search_flights)
search_button.pack()

# Create a button to generate random flights
def generate_random_flights():
   # Read from URL
    file = urlopen("https://data.transportation.gov/resource/4f3n-jbg2.json?year=2022")
    Read = file.read()
    
    # Parse JSON
    flights = json.loads(Read)
    
    # Select a random flight
    random_flight = random.choice(flights)
    
    # Set the cities in the entry widgets
    city1_entry.delete(0, tk.END)
    city1_entry.insert(0, random_flight["city1"])
    city2_entry.delete(0, tk.END)
    city2_entry.insert(0, random_flight["city2"])

random_button = tk.Button(root, text="Random Flights", command=generate_random_flights)
random_button.pack()

# Start the main event loop
root.mainloop()

