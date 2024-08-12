from sentence_transformers import SentenceTransformer

def embed_text(text: str):
    embed_model = SentenceTransformer("sentence-transformers/msmarco-MiniLM-L12-cos-v5", trust_remote_code=True)
    embed_model_dims = embed_model.get_sentence_embedding_dimension()
    
    #Put the prompt stuff here
    
    return embed_model.encode(text)

def get_embed_model_dims():
    embed_model = SentenceTransformer("sentence-transformers/msmarco-MiniLM-L12-cos-v5", trust_remote_code=True)
    embed_model_dims = embed_model.get_sentence_embedding_dimension()
    
    return embed_model_dims