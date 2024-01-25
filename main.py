import requests


def get_repo_files(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents"
    response = requests.get(url)

    if response.status_code == 200:
        files = response.json()
        return files
    else:
        return None


# Example usage
repo_owner = "HeavyLvy"
repo_name = "PyUpdater"
files = get_repo_files(repo_owner, repo_name)

# If you want the content of a specific file
if files:
    for file in files:
        file_content_url = file["download_url"]
        content_response = requests.get(file_content_url)

        if content_response.status_code == 200:
            file_content = content_response.text
            print(f"Content of {file['name']}:\n{file_content}")
