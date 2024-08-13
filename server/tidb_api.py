from dotenv import load_dotenv
import os
from tidb_vector.integrations import TiDBVectorClient

def map_repo_name(repo_name):
    return repo_name.replace(".", "DOT")

def store_data(user_name,repo_name,issue_texts,embeddings,embed_model_dims):
    load_dotenv()
    
    repo_name = repo_name.replace(".", "DOT")
    
    tidb_vector_store = TiDBVectorClient(table_name=f"user__{user_name}__repo__{repo_name}",
                                         connection_string=os.environ.get('TIDB_DATABASE_URL'),
                                         vector_dimension=embed_model_dims,drop_existing_table=True)
    
    tidb_vector_store.insert(texts=issue_texts, embeddings=embeddings, metadatas=[{"user_name": user_name, "repo_name": repo_name} for _ in range(len(issue_texts))])
    
def query_data(user_name, repo_name, embedding,embed_model_dims, k):
    load_dotenv()    
    
    repo_name = repo_name.replace(".", "DOT")
    
    tidb_vector_store = TiDBVectorClient(table_name=f"user__{user_name}__repo__{repo_name}",
                                         connection_string=os.environ.get('TIDB_DATABASE_URL'),
                                         vector_dimension=embed_model_dims)
    
    query_result = tidb_vector_store.query(embedding, k)
    
    return query_result