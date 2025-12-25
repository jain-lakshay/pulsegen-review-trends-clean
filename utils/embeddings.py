from sentence_transformers import SentenceTransformer

# Load the model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings(texts):
    """
    Generates embeddings locally (no API key, no cost)
    """
    return model.encode(texts, convert_to_tensor=False)


