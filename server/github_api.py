from dotenv import load_dotenv
import os
from github import Github
from github import Auth

def get_issues(owner: str, repo: str):
    load_dotenv()
    github_api_key = os.getenv('GITHUB_API_KEY')

    auth = Auth.Token(github_api_key)

    g = Github(auth=auth)

    repo_obj = g.get_repo(f"{owner}/{repo}")

    issues = repo_obj.get_issues()

    g.close()

    return issues

def get_issue(owner: str, repo: str, issue_no: int):
    load_dotenv()
    github_api_key = os.getenv('GITHUB_API_KEY')

    auth = Auth.Token(github_api_key)

    g = Github(auth=auth)

    repo_obj = g.get_repo(f"{owner}/{repo}")

    issue = repo_obj.get_issue(number=issue_no)

    g.close()

    return issue

#Just for testing
if __name__ == "__main__":
    print(get_issues('csking101', 'AutoML'))