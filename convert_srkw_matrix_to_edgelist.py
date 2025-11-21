import pandas as pd

# Paths
matrix_path = r"C:\Users\srava\Desktop\Random\Codes\Python\Sem 5\code hr\srkw_contact.csv"
output_path = r"C:\Users\srava\Desktop\Random\Codes\Python\Sem 5\code hr\srkw_contacts_edgelist.csv"

print("Loading contact matrix...")
df = pd.read_csv(matrix_path)

# Extract whale IDs (column names)
whales = df.columns.tolist()

edges = []

# Convert matrix → edge list
for i, w1 in enumerate(whales):
    for j, w2 in enumerate(whales):
        if j <= i:
            continue  # avoid duplicates + diagonal
        
        weight = df.iloc[i, j]
        if weight > 0:
            edges.append([w1, w2, int(weight)])

# Create edge DataFrame
edge_df = pd.DataFrame(edges, columns=["from", "to", "count"])

# Save file
edge_df.to_csv(output_path, index=False)

print("\nConverted successfully!")
print(f"Rows generated: {len(edge_df)}")
print("Saved to:", output_path)
