import pandas as pd
import json

# Load your data
df = pd.read_csv('1.csv', delimiter=';')

# Initialize variables
id_counter = 1
nodes = []
node_map = {}

# Function to add nodes to the list
def add_node(name, parent_id):
    global id_counter
    node = {
        "id": id_counter,
        "name": name,
        "parent": parent_id,
        "size": 1  # Assuming size is 1 for each node
    }
    nodes.append(node)
    node_map[name] = id_counter
    id_counter += 1
    return node["id"]

# Process the CSV data
for _, row in df.iterrows():
    parent_id = None
    for level in ['level 1', 'level 2', 'level 3', 'level 4', 'level 5', 'level 6']:
        if pd.isna(row[level]):
            continue
        name = row[level]
        if name not in node_map:
            parent_id = add_node(name, parent_id)
        else:
            parent_id = node_map[name]

# Convert the list of nodes to JSON
nodes_json = json.dumps(nodes, indent=4)

# Save the JSON to a file
with open('tree3.json', 'w') as f:
    f.write(nodes_json)

print("JSON file created successfully.")