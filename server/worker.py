from embedding import embed_text, embed_text_list, get_embed_model_dims
from github_api import get_issue, get_issues
from prompts import issue_body_and_title
from tidb_api import query_data, store_data

async def worker_store_repo_issues(user_name: str, repo_name: str):
    issues = get_issues(user_name, repo_name)
    print("Fetched issues")

    issue_texts = [issue_body_and_title(issue) for issue in issues]
    print(f"Extracted {len(issue_texts)} issue texts")
    
    embeddings = embed_text_list(issue_texts)
    embed_model_dims = get_embed_model_dims()
    print(f"Created {len(embeddings)} embeddings")
    
    store_data(user_name, repo_name, issue_texts, embeddings, embed_model_dims)
    print("Stored data")
    
async def worker_submit_issue(user_name: str, repo_name: str, issue_no: int, k:int = 3):
    current_issue = get_issue(user_name, repo_name, issue_no)
    print("Fetched issue")
    
    issue_text = issue_body_and_title(current_issue)
    print("Created issue text")
    
    embedding = embed_text(issue_text)
    embed_model_dims = get_embed_model_dims()
    print("Embedded query")
    
    query_result = query_data(user_name, repo_name, embedding, embed_model_dims, k)
    print("Queried data")
    
    
    return query_result