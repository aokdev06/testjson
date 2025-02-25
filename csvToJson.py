import pandas as pd
import json
import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser
import os

# Create a Tkinter root window (it will not be shown)
root = tk.Tk()
root.withdraw()

# Open a file dialog to select the CSV file
file_path = filedialog.askopenfilename(
    title="Select CSV file",
    filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
)

# Load the selected CSV file
df = pd.read_csv(file_path, delimiter=';')

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

# Open a file dialog to select the save location for the JSON file
save_path = filedialog.asksaveasfilename(
    title="Save JSON file",
    defaultextension=".json",
    filetypes=(("JSON files", "*.json"), ("All files", "*.*"))
)

# Save the JSON to the selected file
with open(save_path, 'w') as f:
    f.write(nodes_json)

# Show an alert with the file path and provide a clickable link
messagebox.showinfo("Dosya Kaydedildi", f"Dosya Kaydedildi: {save_path}")

# Open the directory containing the saved file in the default file manager
directory = os.path.dirname(save_path)
webbrowser.open(f"file://{directory}")

print(f"JSON file created successfully: {save_path}")