import os
import json
import time
import numpy as np
import faiss  # FAISS library for similarity search
from sentence_transformers import SentenceTransformer

# File to store the FAISS index
INDEX_FILE = "tool_index.faiss"

# Sample tool metadata (extend this list as needed)
from test_closed_source_select import available_tools

# Initialize the embedding model (e.g., a Sentence Transformer)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create a list of text representations from tool metadata.
tool_texts = [
    f"{tool['function']['name']}: {tool['function']['description']}"
    for tool in available_tools
]

# Compute embeddings for each tool
embeddings = model.encode(tool_texts, convert_to_numpy=True)
embedding_dim = embeddings.shape[1]

# Normalize embeddings for cosine similarity search
faiss.normalize_L2(embeddings)

# Check if the index file exists; if so, load the index; otherwise, build it.
if os.path.exists(INDEX_FILE):
    print(f"Loading index from {INDEX_FILE}")
    index = faiss.read_index(INDEX_FILE)
else:
    print("Building a new index...")
    start_time = time.time()
    # Create a FAISS index using HNSW (native implementation)
    index = faiss.IndexHNSWFlat(embedding_dim, 32)  # 32 is the M parameter for HNSW
    index.hnsw.efConstruction = 200  # Construction trade-off parameter
    index.hnsw.efSearch = 50  # Search trade-off parameter

    # Add embeddings to the index
    index.add(embeddings)

    # Save the index to disk for future use
    faiss.write_index(index, INDEX_FILE)
    elapsed_time = time.time() - start_time
    print(f"Index built in {round(elapsed_time, 2)}s "
          f"and saved to {INDEX_FILE}")

# Now, suppose we have a query representing a task requirement
query_text = "Get the weather alerts in California."
# query_text = "Get an object from AWS S3."
# query_text = "Change branch in Git from main to dev"
query_embedding = model.encode([query_text], convert_to_numpy=True)
faiss.normalize_L2(query_embedding)

# Perform nearest-neighbor search (e.g., retrieve top-1 match)
k = 5
distances, indices = index.search(query_embedding, k)

# Output the result
print("Query:", query_text)
for rank, idx in enumerate(indices[0]):
    display_dict = {
        "name": available_tools[idx]['function']["name"],
        "description": available_tools[idx]['function']["description"],
    }
    print(f"Matched top {rank+1} tool "
          f"(dist={distances[0][np.where(indices[0] == idx)][0]}): "
          f"{json.dumps(display_dict, indent=4)}")
