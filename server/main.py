from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from worker import worker_store_repo_issues

app = FastAPI()

"""
Workflow:
1) Take repository link as input
2) Get the list of issues (paginate if too long)
3) Parse and store the issues in TiDB

"""

class RepoIssueStoreRequest(BaseModel):
    #Assuming the repository link is in the format "https://github.com/csking101/SocialRoots -> user_name: csking101, repo_name: SocialRoots"
    user_name: str
    repo_name: str

@app.post("/repo/submit")
async def store_repo_issues(request: RepoIssueStoreRequest):
    # Store information about user if needed

    user_name = request.user_name
    repo_name = request.repo_name

    try:
        await worker_store_repo_issues(user_name, repo_name)
        return {"message": "Issues storage request submitted" }
    except Exception as e:
        return {"message": f"An error occurred while processing the request-{e}"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=6969)