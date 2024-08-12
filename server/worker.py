from embedding import embed_text, get_embed_model_dims
from github_api import get_issues
from prompts import issue_body_and_title
from tidb_api import store_data

async def worker_store_repo_issues(user_name: str, repo_name: str):
    issues = get_issues(user_name, repo_name)
    print("Fetched issues")

    issue_texts = [issue_body_and_title(issue) for issue in issues]
    print(f"Extracted {len(issue_texts)} issue texts")
    
    embeddings = [embed_text(issue_text) for issue_text in issue_texts]
    embed_model_dims = get_embed_model_dims()
    print(f"Created {len(embeddings)} embeddings")
    
    store_data(user_name, repo_name, issue_texts, embeddings, embed_model_dims)
    print("Stored data")