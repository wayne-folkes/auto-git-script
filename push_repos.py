import os
from git import Repo
from datetime import datetime

# Path to repo directory
REPOS_DIR = os.path.expanduser('/Users/eric_dav/Desktop/repos')

def push_repos(repo_path):
    try:
        repo = Repo(repo_path)
        # Check if the repo has a remote set up
        if repo.remotes:
            # Add all changes, commit and push
            repo.git.add(A=True)
            repo.index.commit(f"Auto-commit on {datetime.now().strftime(f'%a %b-%d-%y %H:%M %p')}")
            repo.remotes.origin.push()
            print(f'Successfully pushed {repo_path}')
        else:
            prit(f'No remote found for {repo_path}')
    except Exception as e:
        print(f'Failed to push {repo_path}: {e}')

def find_and_push_repos(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
    # Check if the current directory is a Git repo
        if os.path.exists(os.path.join(dirpath, '.git')):
            print(f'Pushing repo: {dirpath}')
            push_repos(dirpath)

if __name__ == "__main__":
    find_and_push_repos(REPOS_DIR)