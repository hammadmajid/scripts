# This script deletes a GitHub user's repositories. It lists all repositories, asks the user
# to confirm deletion of each one, and then deletes it if confirmed.

import requests

GITHUB_USERNAME = 'your_username_here'
GITHUB_TOKEN = 'github_token_with_permission_to_delete_repos'
HEADERS = {'Authorization': f'token {GITHUB_TOKEN}'}

def get_repos():
    page = 1
    repos = []
    while True:
        response = requests.get(f'https://api.github.com/user/repos?page={page}&per_page=100', headers=HEADERS)
        if response.status_code != 200:
            print(f"Error fetching repositories: {response.status_code}")
            break
        batch = response.json()
        if not batch:
            break
        repos.extend(batch)
        page += 1
    return repos

def delete_repo(repo_name):
    response = requests.delete(f'https://api.github.com/repos/{repo_name}', headers=HEADERS)
    if response.status_code == 204:
        print(f'Repo {repo_name} deleted successfully.')
    else:
        print(f'Failed to delete {repo_name}. Status code: {response.status_code}')

def main():
    repos = get_repos()
    for repo in repos:
        repo_name = f"{repo['owner']['login']}/{repo['name']}"
        user_input = input(f"Do you want to delete the repository '{repo_name}'? (yes/no): ").strip().lower()
        if user_input == 'yes':
            delete_repo(repo_name)
        else:
            print(f"Skipped deletion of repository '{repo_name}'.")

if __name__ == "__main__":
    main()