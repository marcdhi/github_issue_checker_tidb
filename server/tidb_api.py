from dotenv import load_dotenv
import os
from tidb_vector.integrations import TiDBVectorClient

def store_data(user_name,repo_name,issue_texts,embeddings,embed_model_dims):
    load_dotenv()
    tidb_api_key = os.getenv('TIDB_DATABASE_URL')
    
    tidb_vector_store = TiDBVectorClient(table_name=f"user__{user_name}__repo__{repo_name}",
                                         connection_string=os.environ.get('TIDB_DATABASE_URL'),
                                         vector_dimension=embed_model_dims,drop_existing_table=True)
    
    tidb_vector_store.insert(texts=issue_texts, embeddings=embeddings, metadatas=[{"user_name": user_name, "repo_name": repo_name} for _ in range(len(issue_texts))])